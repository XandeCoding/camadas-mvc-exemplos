from peewee import *
from .baseModel import BaseModel
from entities.cliente import Cliente

class ClienteModel(BaseModel):
    nome = CharField()
    idade = IntegerField()
    cpf = CharField()

    @staticmethod
    def criar(clienteData: Cliente):
        return ClienteModel.create(
            nome=clienteData.nome,
            idade=clienteData.idade,
            cpf=clienteData.cpf
        )

    @staticmethod
    def buscar(cpf: str):
        try:
            return ClienteModel.get(ClienteModel.cpf == cpf)
        except:
            return None