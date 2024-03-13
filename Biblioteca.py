import livros
aux = True


while aux == True:
    print("\nMenu de opções:")
    print("1. Adicionar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Exibir livros")
    print('5. Ver os livros emprestados')
    print('6 - Ver lista de disponiveis')
    print("7 - Sair do programa")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 7:
        aux = False
        break
    elif opcao == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = int(input("Digite o ano de publicação do livro: "))
        novo_livro = livros.Livro(titulo, autor, ano_publicacao)
        livros.Biblioteca.adicionar_livro(titulo)

    elif opcao == 2:
        titulo = input("Digite o título do livro que deseja emprestar: ")
        livros.Biblioteca.emprestar_livro(titulo)
        print

    elif opcao == 3:
        titulo = input("Digite o título do livro que deseja devolver: ")
        livros.Biblioteca.devolver_livro(titulo)

    elif opcao == 4:
        livros.Biblioteca.exibir_livros()
    
    elif opcao == 5:
        livros.Biblioteca.ver_emprestados()
    
    elif opcao == 6:
        livros.Biblioteca.ver_disponiveis()

    else:
        print("Opção inválida. Tente novamente.")

