class Livro:
    def __init__(self, titulo, autor, anopublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anopublicacao = anopublicacao
        self.status = "disponível"

    def disponibilidade(self):
        return self.status == "disponível"

    def alterar_status(self, status):
        self.status = status

biblioteca_ = []
emprestados = []
disponiveis = []

class Biblioteca(Livro):
    def __init__ (self, titulo, autor, anopublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anopublicacao = anopublicacao
        self.status = "disponível"
    
    def adicionar_livro(titulo):
        disponiveis.append(titulo)
        biblioteca_.append(titulo)
        print(biblioteca_)


    def emprestar_livro(titulo):
        emprestados.append(titulo)
        print('Livro emprestado com sucesso!')

    def ver_emprestados ():
        print('Lista de emprestados: ')
        print(emprestados)



    def devolver_livro(titulo):
        disponiveis.append(titulo)
        print('Livro devolvido com sucesso!')

    def ver_disponiveis():
        print('Lista de livros disponíveis:')
        print(disponiveis)


    def exibir_livros():
        print(biblioteca_)
        