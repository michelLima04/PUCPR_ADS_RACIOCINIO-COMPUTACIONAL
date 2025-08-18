
print("----- MENU PRINCIPAL -----\n")
print("(1) Estudante.")
print("(2) Professor.")
print("(3) Disciplina.")
print("(4) Turma.")
print("(5) Matrícula.")
print("(9) Sair.")
print("--------------------------")
option = int(input("Digite uma das opções disponíveis: "))

if option == 1:
    setor = "ESTUDANTE"
elif option == 2:
    setor = "PROFESSOR"
elif option == 3:
    setor = "DISCIPLINA"
elif option == 4:
    setor = "TURMA"
elif option == 5:
    setor = "MATRÍCULA"
elif option == 9:
    print("Opção SAIR em desenvolvimento...")
else:
    print("Opção indisponível!")

if option != 9 and (option >= 1 and option <= 5):
    print(f"----- [{setor}] MENU DE OPERAÇOES -----\n")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(5) Voltar ao MENU principal.")
    print("--------------------------------------")
    option = int(input("Digite uma das opções disponíveis: "))

    if option == 1:
        operacao = "INCLUIR"
    elif option == 2:
        operacao = "LISTAR"
    elif option == 3:
        operacao = "ATUALIZAR"
    elif option == 4:
        operacao = "EXCLUIR"
    elif option == 5:
        print("Botão VOLTAR em desenvolvimento...\n")
    else:
        print("Opção indisponível...")

    if option != 5 and (option >= 1 and option <= 5):
        print(f"===== [{setor}] -> {operacao} =====\n")
        print("-> Em desenvolvimento...\n   Programa encerrado.")
    else:
        print("Programa encerrado.")
else:
    print("Programa encerrado.")