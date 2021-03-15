class Cliente():
    nome: str
    idade: int
    cpf: str

    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf