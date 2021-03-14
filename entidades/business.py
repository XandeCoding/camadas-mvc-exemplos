from entities.cliente import Cliente
from entities.contaPoupanca import ContaPoupanca
from entities.contaCorrente import ContaCorrente
from models.clienteModel import ClienteModel
from models.contaPoupancaModel import ContaPoupancaModel
from models.contaCorrenteModel import ContaCorrenteModel


class Business():

    @staticmethod
    def criarContaPoupanca(cliente: Cliente, conta: ContaPoupanca):
        existeCliente = ClienteModel.buscar(cliente.cpf)

        if (existeCliente):
            return False

        clienteCriado = ClienteModel.criar(cliente)
        ContaPoupancaModel.criar(clienteCriado.id, conta)
        return True

    @staticmethod
    def criarContaCorrente(cliente: Cliente, conta: ContaCorrente):
        existeCliente = ClienteModel.buscar(cliente.cpf)

        if (existeCliente):
            return False

        clienteCriado = ClienteModel.criar(cliente)
        ContaCorrenteModel.criar(clienteCriado.id, conta)
        return True

    @staticmethod
    def checarContaPoupanca(cpf: str):
        cliente = ClienteModel.buscar(cpf)
        if not cliente:
            None

        conta = ContaPoupancaModel.buscarPeloCliente(cliente.id)
        return ( cliente, conta )

    @staticmethod
    def checarContaCorrente(cpf: str):
        cliente = ClienteModel.buscar(cpf)
        if not cliente:
            None

        conta = ContaCorrenteModel.buscarPeloCliente(cliente.id)
        return ( cliente, conta )






