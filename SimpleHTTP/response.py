from http import HTTPStatus

class Response:
    status_code: HTTPStatus
    content_type = "text/plain"
    def __init__(self, status_code: HTTPStatus=HTTPStatus.NOT_FOUND, body="", *args, **kwargs):
        self.status_code = status_code
        self.body = body
    def code(self):
        return self.status_code.value
    def phrase(self):
        return self.status_code.phrase
    def body_as_str(self):
        if self.body:
            return str(self.body)
        return ""
    def get_content_type(self):
        return self.content_type


class HtmlResponse(Response):

    content_type = "text/html"
    def __init__(self, status_code: HTTPStatus = HTTPStatus.NOT_FOUND, html_file_path=None, *args, **kwargs):
        file_body = None
        if html_file_path is None:
            super().__init__(HTTPStatus.NOT_FOUND)
        else:
            try:
                with open(html_file_path, 'r') as file:
                    file_body = file.read()
                super().__init__(status_code, file_body, *args, **kwargs)   
            except FileNotFoundError as e:
                logging.info(e)
                super().__init__(HTTPStatus.NOT_FOUND)
            except:
                super().__init__(HTTPStatus.INTERNAL_SERVER_ERROR)
