# Instituição: Pontifícia Universidade Católica do Paraná PUCPR
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
# Aluno/Autor: Michel Urban Rosendo de Lima
# Disciplina: Raciocínio Cumputacional (1ºPeríodo)
# Tema: Sistema de Gerenciamento PUC

loop_menu = True
loop_operations = False
lista_alunos = [] #Incremento da lista que armazenará Alunos

while loop_menu == True:

    print("\n------[MENU SISTEMA PUC]------")
    print("(1) Estudante")
    print("(2) Professor")
    print("(3) Disciplina")
    print("(4) Turma")
    print("(5) Matrícula")
    print("(9) Sair")
    print("------------------------------")

    while True:
        try:
            option = int(input("Digite uma das opções disponíveis: "))
            if option <= 0 or option > 9:
                print("> Opção indisponível! Tente novamente.")    # Validação para garantir que o usuário escolha um número presente neste período.
            else:
                break
        except ValueError:
            print("> Valor inválido! Insira apenas números.") # Garante que aceite apenas números inteiros.

    if option == 1:
        section = "ESTUDANTE"
        loop_operations = True
    elif option == 2:
        section = "PROFESSOR"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. \n>> EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 3:
        section = "DISCIPLINA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. \n>> EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 4:
        section = "TURMA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. \n>> EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 5:
        section = "MATRÍCULA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. \n>> EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 9:
        loop_menu = False
    else:   # Este else existe, pois no momento não temos as opções 6,7,8 disponíveis. Futura implementação.
        print("\n> Opção indisponível! Tente novamente.")

    while loop_operations == True:
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print("(1) Incluir")
        print("(2) Listar")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(5) Voltar ao MENU principal")
        print("-----------------------------------------")

        while True:
            try:
                option = int(input("Digite uma das opções disponíveis: "))
                if option <= 0 or option > 5:
                    print("> Opção indisponível! Tente novamente.")    # Validação para garantir que o usuário escolha um número presente neste período.
                else:
                    break
            except ValueError:
                    print("> Valor inválido! Insira apenas números.") # Garante que aceite apenas números inteiros.

        if option == 1:
            operacao = "INCLUIR"

            print(f"\n-----[{section} -> {operacao}]-----")

            print("\n> [DADOS CADASTRAIS]")
            nome = input("> Digite o nome do aluno: ")
            lista_alunos.append(nome)
            input("> Aluno cadastrado com sucesso! Pressione Enter para voltar...")

        elif option == 2:
            operacao = "LISTAR"

            print(f"\n-----[{section} -> {operacao}]-----")

            print(f"\n> Qtd. de Alunos: {len(lista_alunos)}")

            if(len(lista_alunos) > 0):
                print("> Alunos cadastrados:")
                for aluno in lista_alunos:
                    print(f"  - {aluno}")

                input("\n> Pressione Enter para continuar...")

            else:
                input("> Nenhum cadastrado no sistema! Pressione Enter para continuar...")

        elif option == 3:
            operacao = "ATUALIZAR"
            print(f"\n-----[{section} -> {operacao}]-----")
            print(">> Serviço indisponível no momento \n>> EM DESENVOLVIMENTO!")
        elif option == 4:
            operacao = "EXCLUIR"
            print(f"\n-----[{section} -> {operacao}]-----")
            print(">> Serviço indisponível no momento \n>> EM DESENVOLVIMENTO!")
        elif option == 5:
            loop_operations = False
        else:
            print("> Opção indisponível! Tente novamente.")



print("\n>> ENCERRANDO SISTEMA... Até a próxima!")