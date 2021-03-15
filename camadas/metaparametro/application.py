from business import Business
from entities.contaPoupanca import ContaPoupanca
from entities.contaCorrente import ContaCorrente
from entities.cliente import Cliente


class Application():

    @staticmethod
    def instanciarConta(nome: str, idade: int, cpf: str, depositoInicial: float, tipoDeConta: str):
        if tipoDeConta.lower() == 'poupanca':
            return Application.instanciarContaPoupanca(nome, idade, cpf, depositoInicial)
        elif tipoDeConta.lower() == 'corrente':
            return Application.instanciarContaCorrente(nome, idade, cpf, depositoInicial)
        else:
            return None

    @staticmethod
    def instanciarContaPoupanca(nome: str, idade: int, cpf: str, depositoInicial: float):
        novoCliente = Cliente(nome, idade, cpf)
        novaConta = ContaPoupanca(depositoInicial)

        return Business.criarContaPoupanca(novoCliente, novaConta)

    @staticmethod
    def instanciarContaCorrente(nome: str, idade: int, cpf: str, depositoInicial: float):
        novoCliente = Cliente(nome, idade, cpf)
        novaConta = ContaCorrente(depositoInicial)

        Business.criarContaCorrente(novoCliente, novaConta)
        return True

    @staticmethod
    def checarConta(cpf: str, tipoDeConta: str):
        if not cpf: return None

        if tipoDeConta.lower() == 'poupanca':
            return Application.checarContaPoupanca(cpf)
        elif tipoDeConta.lower() == 'corrente':
            return Application.checarContaCorrente(cpf)
        else:
            return None

    @staticmethod
    def checarContaPoupanca(cpf: str):
        return Business.checarContaPoupanca(cpf)

    @staticmethod
    def checarContaCorrente(cpf: str):
        return Business.checarContaCorrente(cpf)






