#EXEMPLO DE CLASSE

class Pessoa:

    def __init__(self,nome,idade) -> None :
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e temho {self.idade} anos."
    
    

#OBJETOS -> QUALQUER COISA QUE EU POSSA REPRESENTAR NA CLASSE


pessoa1 = Pessoa("Carlos",19)
mensagem = pessoa1.saudacao()

print(mensagem)

