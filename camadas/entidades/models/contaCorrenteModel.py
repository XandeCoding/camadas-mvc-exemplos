from peewee import *
from .baseModel import BaseModel
from .clienteModel import ClienteModel
from entities.contaCorrente import ContaCorrente

class ContaCorrenteModel(BaseModel):
    clienteId = IntegerField(null=False)
    saldo = DecimalField()

    @staticmethod
    def criar(clienteId: int, contaCorrenteData: ContaCorrente):
        return ContaCorrenteModel.create(
            clienteId=clienteId,
            saldo=contaCorrenteData.saldo
        )

    @staticmethod
    def buscarPeloCliente(clienteId: int):
        return ContaCorrenteModel.get(ContaCorrenteModel.clienteId == clienteId)
