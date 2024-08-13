from .server import Server
class App(Server):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register(self, http_method, path, method):
        unique_str = http_method+"#"+path
        self.handler_db[unique_str] = method

    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
    
    def getHandlers(self):
        return self.handler_db

