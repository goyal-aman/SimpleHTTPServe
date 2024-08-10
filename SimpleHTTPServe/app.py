from .server import Server
class App(Server):

    def __init__(self):
        super().__init__()

    def register(self, http_method, path, method):
        unique_str = http_method+"#"+path
        self.handler_db[unique_str] = method

    def start(self):
        super().start()
    
    def getHandlers(self):
        return self.handler_db

