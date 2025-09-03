# Instituição: Pontifícia Universidade Católica do Paraná PUCPR
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
# Aluno/Autor: Michel Urban Rosendo de Lima
# Disciplina: Raciocínio Cumputacional (1ºPeríodo)
# Tema: Sistema de Gerenciamento PUC

loop_menu = True
loop_operations = False
list_students = [] #Incremento da lista que armazenará Alunos

while loop_menu == True:

    print("\n-------[SISTEMA PUC]-------")
    print("(1) Estudante")
    print("(2) Professor")
    print("(3) Disciplina")
    print("(4) Turma")
    print("(5) Matrícula")
    print("(9) Sair")
    print("------------------------------")

    while True:
        try:
            option = int(input("> Digite uma das opções disponíveis: "))
            if option <= 0 or option > 9:
                print("> Opção indisponível! Tente novamente.") # Validação para garantir que o usuário escolha um número presente neste período.
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
        print(">> Serviço indisponível no momento. EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 3:
        section = "DISCIPLINA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 4:
        section = "TURMA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. EM DESENVOLVIMENTO!")
        loop_operations = False
    elif option == 5:
        section = "MATRÍCULA"
        print(f"\n-----[MENU DE OPERAÇOES -> {section}]-----")
        print(">> Serviço indisponível no momento. EM DESENVOLVIMENTO!")
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
                option = int(input("> Digite uma das opções disponíveis: "))
                if option <= 0 or option > 5:
                    print("> Opção indisponível! Tente novamente.")    # Validação para garantir que o usuário escolha um número presente neste período.
                else:
                    break
            except ValueError:
                    print("> Valor inválido! Insira apenas números.") # Garante que aceite apenas números inteiros.

        if option == 1:
            operation = "INCLUIR"
            print(f"\n-----[{section} -> {operation}]-----")

            while True:
                try: # Garantir que o COD seja um número inteiro maior que zero.
                    cod = int(input("> Digite o Código do aluno: "))
                    if cod < 0:
                        print("> Valor inválido!")
                    else:
                        break
                except ValueError:
                    print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.

            while True: # Pesquisei esta função na internet, para validar um input de uma String.
                name = input("> Digite o Nome do aluno: ").strip() #.strip() -> Remove todos os possíveis espaços extras. Por exemplo no início ou final da string.
                if name.replace(" ", "").isalpha():    #.replace() -> Remove todos possíveis espaços entre strings
                    break                                           #.isalpha() -> Verifica se o conteúdo restante são apenas caracteres.
                else:
                    print("> Valor inválido! Insira apenas caracteres.")

            while True: # Pesquisei também esta função, para verificar se são digitos. *Melhoria futura* -> Validar formatação correta do CPF, para ver se é válido.
                cpf = input("> Digite o CPF do aluno: ").strip() # Remove possíveis espaços extras.
                if cpf.isdigit() and len(cpf) == 11:             #.isdigit -> Função que verifica se os caracteres são números
                    break                                        #len() -> Delimita a qtd. necessária de digitos.
                else:
                    print("> Valor inválido! O CPF É necessário conter 11 digitos")

            dictionary_students = {
                "CÓDIGO" : cod,
                "NOME" : name,
                "CPF" : cpf
            }
            list_students.append(dictionary_students)
            print("----------------------------------------------------------------")
            input("> Aluno cadastrado com sucesso! Pressione Enter para voltar...")

        elif option == 2:
            operation = "LISTAR"
            print(f"\n-----[{section} -> {operation}]-----")

            print(f"> Qtd. de Alunos: {len(list_students)}")

            if(len(list_students) > 0):
                for dictionary_students in list_students:
                    print(f"- {dictionary_students["CÓDIGO"]} | {dictionary_students["NOME"]} | {dictionary_students["CPF"]}")

                print("-----------------------------------")
                input("> Pressione Enter para continuar...")
            else:
                input("> Nenhum Aluno cadastrado no sistema! Pressione Enter para voltar...")

        elif option == 3:
            operation = "ATUALIZAR"
            print(f"\n-----[{section} -> {operation}]-----")

            if list_students == []: # Se a lista de Alunos estiver vazia, não tem como atualizar dados...
                input("> Nenhum Aluno cadastrado no sistema! Pressione Enter para voltar...")
            else:
                while True:

                    while True:
                        try:  # Garantir que o COD seja um número inteiro maior que zero.
                            cod_edit = int(input("> Digite o código do Aluno para Editar o seu perfil: "))
                            if cod_edit < 0:
                                print("> Valor inválido!")
                            else:
                                break
                        except ValueError:
                            print("> Valor inválido! Insira apenas números.")

                    student_by_edit = None

                    for dictionary_students in list_students:
                        if dictionary_students["CÓDIGO"] == cod_edit:
                            student_by_edit = dictionary_students
                            break

                    if student_by_edit == None:
                        print("> ERROR - Código incorreto ou Aluno não encontrado!")
                    else:
                        #student_by_edit["CÓDIGO"] = int(input("> Digite o Código do Aluno: "))
                        #student_by_edit["NOME"] = input("> Digite o Nome do Aluno: ")
                        #student_by_edit["CPF"] = input("> Digite o CPF do Aluno: ")

                        while True:
                            try:  # Garantir que o COD seja um número inteiro maior que zero.
                                student_by_edit["CÓDIGO"] = int(input("> Digite o NOVO Código do Aluno: "))
                                if student_by_edit["CÓDIGO"] < 0:
                                    print("> Valor inválido!")
                                else:
                                    break
                            except ValueError:
                                print("> Valor inválido! Insira apenas números.")

                        while True:  # Garantir que o input seja ums String
                            student_by_edit["NOME"] = input("> Digite o NOVO Nome do Aluno: ").strip()
                            if student_by_edit["NOME"].replace(" ", "").isalpha():
                                break
                            else:
                                print("> Valor inválido! Insira apenas caracteres.")

                        while True:  # Garantir que o input seja de 11 digitos
                            student_by_edit["CPF"] = input("> Digite o NOVO CPF do Aluno: ")
                            if student_by_edit["CPF"].isdigit() and len(student_by_edit["CPF"]) == 11:
                                break
                            else:
                                print("> Valor inválido! O CPF É necessário conter 11 digitos.")
                        print("----------------------------------------------------------------")
                        input("> Dados Atualizados com sucesso! Pressione Enter para voltar... ")
                        break

        elif option == 4:
            operation = "EXCLUIR"
            print(f"\n-----[{section} -> {operation}]-----")

            if list_students == []: # Se a lista de Alunos estiver vazia, não tem como excluir aluno...
                input("> Nenhum Aluno cadastrado no sistema! Pressione Enter para voltar...")
            else:
               while True:

                    while True:
                        try:  # Garantir que o COD seja um número inteiro maior que zero.
                            cod_delete = int(input("> Digite o código do Aluno para Excluir do sistema: "))
                            if cod_delete < 0:
                                print("> Valor inválido!")
                            else:
                                break
                        except ValueError:
                            print("> Valor inválido! Insira apenas números.")

                    student_by_delete = None

                    for dictionary_students in list_students:
                        if dictionary_students["CÓDIGO"] == cod_delete:
                            student_by_delete = dictionary_students
                            break

                    if student_by_delete == None:
                        print("> ERROR - Código incorreto ou Aluno não encontrado!")
                    else:
                        print("----------------------------------------------------------------")
                        while True:
                            resp = input(f"> Deseja excluir {student_by_delete['NOME']} do Sistema PUC? [s/n] ").lower()
                            if resp == "s":
                                list_students.remove(student_by_delete)
                                input("> Aluno Excluído com sucesso! Pressione Enter para voltar...")
                                break
                            elif resp == "n":
                                input("> Exclusão cancelada. Pressione Enter para voltar...")
                                break
                            else:
                                print("> ERROR - Opção inválida!")
                        break

        elif option == 5:
            loop_operations = False
        else:
            print("> Opção indisponível! Tente novamente.")

print("\n>> ENCERRANDO SISTEMA PUC... Até a próxima! :)")