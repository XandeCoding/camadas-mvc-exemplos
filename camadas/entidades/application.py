from business import Business
from entities.contaPoupanca import ContaPoupanca
from entities.contaCorrente import ContaCorrente
from entities.cliente import Cliente


class Application():

    @staticmethod
    def instanciarContaPoupanca(nome: str, idade: int, cpf: str, depositoInicial: int):
        novoCliente = Cliente(nome, idade, cpf)
        novaConta = ContaPoupanca(depositoInicial)

        return Business.criarContaPoupanca(novoCliente, novaConta)

    @staticmethod
    def instanciarContaCorrente(nome: str, idade: int, cpf: str, depositoInicial: int):
        novoCliente = Cliente(nome, idade, cpf)
        novaConta = ContaCorrente(depositoInicial)

        Business.criarContaCorrente(novoCliente, novaConta)
        return True

    @staticmethod
    def checarContaPoupanca(cpf: str):
        if not cpf:
            return None

        return Business.checarContaPoupanca(cpf)

    @staticmethod
    def checarContaCorrente(cpf: str):
        if not cpf:
            return None

        return Business.checarContaCorrente(cpf)






