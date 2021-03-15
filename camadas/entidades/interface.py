import typer
from application import Application

def main():
    typer.echo("Hello To Banking System\n")

    typer.echo('Voce gostaria de:\n')
    typer.echo('1) Criar uma nova conta')
    typer.echo('2) Checar conta')

    opcao = typer.prompt('Digite o número da opção desejada')

    if (opcao == '1'):
        criarConta()
    elif (opcao == '2'):
        checarConta()

def criarConta():
    nome = typer.prompt('Qual o seu nome?')
    idade = typer.prompt('Qual a sua idade?')
    cpf = typer.prompt('Qual o seu cpf?')
    tipoDeConta = typer.prompt('Qual tipo de conta deseja criar?').lower()
    depositoInicial = typer.prompt('Você deseja fazer um depósito inicial?')

    if tipoDeConta == 'poupanca':
        Application.instanciarContaPoupanca(nome, idade, cpf, depositoInicial)
    elif tipoDeConta == 'corrente':
        Application.instanciarContaCorrente(nome, idade, cpf, depositoInicial)

def checarConta():
    cpf = typer.prompt('Qual o seu cpf?')
    tipoDeConta = typer.prompt('Qual o tipo da conta?').lower()

    if tipoDeConta == 'poupanca':
        resultado = Application.checarContaPoupanca(cpf)
    elif tipoDeConta == 'corrente':
        resultado = Application.checarContaCorrente(cpf)

    if not resultado:
        typer.echo('A conta não foi encontrada')


    cliente, conta = resultado
    typer.echo(f'\nnome - { cliente.nome }\ncpf - { cliente.cpf }')
    typer.echo(f'Saldo - { conta.saldo }\n')



if __name__ == "__main__":
    typer.run(main)