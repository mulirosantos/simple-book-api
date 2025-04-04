from flask_restx import fields

from src.server import server

book = server.api.model('Book',{
    'id':fields.String(description='O ID do Registro'),
    'title':fields.String(required=True,min_length=1,max_length=200, description='O Titulo do Livro')
    
})