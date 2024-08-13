import socket, asyncio, threading, random, signal, logging, json
from contextlib import closing
from http import HTTPStatus
from .response import Response, HtmlResponse


logging.basicConfig(level=logging.INFO)

class Server:
    DEFAULT_HOST, DEFAULT_PORT = '', 8888 
    DEFAULT_BYTE_READ = 1024
    DEFAULT_SOCK_LISTEN_SIZE = 5

    def __init__(self, HOST=DEFAULT_HOST, PORT = DEFAULT_PORT):
        self.HOST, self.PORT = HOST, PORT
        self.sock = None
        self.handler_db = dict()

    def start(self, *args, **kwargs):
        logging.info(f" Starting server on {self.PORT}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.HOST, self.PORT))
        sock.listen(self.DEFAULT_SOCK_LISTEN_SIZE)
        self.sock = sock
        self.main(sock)


    def signal_handler(self, sig, frame):
        logging.INFO("Shutting down server...")
        self.sock.close()
        exit(0)

    
    def accept(self, sock):
        ccon, caddr = sock.accept()
        return ccon, caddr

    def myecho(request):
        return Response(HTTPStatus.BAD_GATEWAY, {'data':"yes"})

    def handler(self, http_method, path, body, *args, **kwargs):
        method = self.handler_db.get(http_method+"#"+path, None)
        if method==None:
            logging.warning(f"No handler for http_method: {http_method} path: {path}")
            return Response()
        response =  method({
            "http_method":http_method,
            "path":path,
            "body": None if (body is None or len(body)==0) else json.loads(body)
        }, *args, **kwargs)
        logging.info(f"[{http_method}]\t {path}\t :{response.status_code}")
        return response


    def read_from_conn(self, ccon, caddr):
        logging.debug("READ FROM CCON", ccon, caddr)
        try:
            raw_req = ccon.recv(self.DEFAULT_BYTE_READ)
            if len(raw_req) == 0:
                # for some reason when I hit from brower using localhost I am getting two hits 
                # on socket one normal as expected
                # but other container b'' raw data
                return
            req = raw_req.decode()
            logging.debug(f"raw: {raw_req}\n raw_end")
            header, body = req.split("\r\n\r\n", 1)
            logging.debug(f"headers: {header}\n headers_end")
            logging.debug(f"body: {body}\n body_end")

            total_body_len = 0
            headers = header.split("\r\n")
            for header in headers:
                if header.startswith("Content-Length"):
                    total_body_len = int(header.split(":")[1].strip())
                    break
            
            received_body_len = len(body)
            if received_body_len < total_body_len:
                body += ccon.recv(total_body_len - received_body_len).decode()
            
            line0 = headers[0].strip()
            http_method, path, _ = line0.split(" ")


            response = self.handler(http_method, path.rstrip("/"), body)
            status_line = f"HTTP/1.1 {response.code()} {response.phrase()}\r\n"
            response_str = response.body_as_str()
            resp_headers = (
                f"Content-Type: {response.get_content_type()}\r\n"
                f"Content-Length: {len(response_str)}\r\n"
                f"Connection: close\r\n" 
            )

            resp = f"{status_line}{resp_headers}\r\n{response_str}"
            ccon.sendall(resp.encode())

            
        finally:
            ccon.close()    

    def main(self, sock):
        signal.signal(signal.SIGINT, self.signal_handler)
        while True:
            ccon, caddr = sock.accept()
            t = threading.Thread(target=self.read_from_conn, args=(ccon, caddr))
            t.start()
    

