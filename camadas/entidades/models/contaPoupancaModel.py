from peewee import *
from .baseModel import BaseModel
from .clienteModel import ClienteModel
from entities.contaPoupanca import ContaPoupanca

class ContaPoupancaModel(BaseModel):
    clienteId = IntegerField(null=False)
    saldo = DecimalField()

    @staticmethod
    def criar(clienteId: int, contaPoupancaData: ContaPoupanca):
        return ContaPoupancaModel.create(
            clienteId=clienteId,
            saldo=contaPoupancaData.saldo
        )

    @staticmethod
    def buscarPeloCliente(clienteId: int):
        return ContaPoupancaModel.get(ContaPoupancaModel.clienteId == clienteId)
