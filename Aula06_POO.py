# Exercício 06  (Classes e Objetos)

class Usuários():
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
    def informacaoSaida(self):
        print(f'Olá, meu nome é: ',self.nome, 'e Sobrenome: ',self.sobrenome, 'Idade: ',self.idade,' Cidade: ',self.cidade)

usuario1 = Usuários(input('Nome: '),input('Sobrenome: '),input('Idade: '),input('Cidade: '))
usuario2 = Usuários(input('Nome: '),input('Sobrenome: '),input('Idade: '),input('Cidade: '))
usuario3 = Usuários(input('Nome: '),input('Sobrenome: '),input('Idade: '),input('Cidade: '))

usuario1.informacaoSaida()
usuario2.informacaoSaida()
usuario3.informacaoSaida()