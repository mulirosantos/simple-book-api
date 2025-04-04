'''Instância da aplicação'''

from flask import Flask
from flask_restx import Api

class Server(): 
    def __init__(self):
        self.app = Flask(__name__) # App Flask
        self.api = Api(self.app,
                       version='1.0',
                       title='Simple Book API',
                       description='A Simple book API',
                       doc='/docs',
                       ) # objeto api
    def run(self): #método para a classe Server
        self.app.run(
            debug=True
        )

server = Server()