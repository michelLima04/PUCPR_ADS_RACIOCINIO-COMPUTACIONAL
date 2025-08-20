# Aluno: Michel Urban Rosendo de Lima
# Instituição: Pontifícia Universidade Católica do Paraná PUCPR
# Disciplina: Raciocínio Cumputacional (1ºPeríodo)
# Tema: Sistema de Gerenciamento PUC

loop_menu = True
loop_operations = False

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
        loop_operations = True
    elif option == 3:
        section = "DISCIPLINA"
        loop_operations = True
    elif option == 4:
        section = "TURMA"
        loop_operations = True
    elif option == 5:
        section = "MATRÍCULA"
        loop_operations = True
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
        elif option == 2:
            operacao = "LISTAR"
        elif option == 3:
            operacao = "ATUALIZAR"
        elif option == 4:
            operacao = "EXCLUIR"
        elif option == 5:
            loop_operations = False
        else:
            print("> Opção indisponível! Tente novamente.")

        if option != 5 and (option >= 1 and option < 5):
            print(f"\n-----[{section} -> {operacao}]-----")
            print(">> Serviço indisponível no momento.")

print("\n>> ENCERRANDO SISTEMA... Até a próxima!")