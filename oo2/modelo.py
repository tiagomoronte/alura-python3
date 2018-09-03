class Programa:

    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()

print(f'Nome {atlanta.nome} - Ano {atlanta.ano} - Temporadas - {atlanta.temporadas} - Likes - {vingadores.likes} ')
print(f'Nome {vingadores.nome} - Ano {vingadores.ano} - Duração - {vingadores.duracao} - Likes - {vingadores.likes}')

