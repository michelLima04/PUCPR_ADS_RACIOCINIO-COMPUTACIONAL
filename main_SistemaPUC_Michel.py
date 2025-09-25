# Instituição: Pontifícia Universidade Católica do Paraná PUCPR
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
# Aluno/Autor: Michel Urban Rosendo de Lima
# Disciplina: Raciocínio Cumputacional (1ºPeríodo)
# Tema: Sistema de Gerenciamento PUC

import json # Importação da biblioteca JSON

loop_menu = True
file_students = "students_puc.json"    # Arquivo que armazenará Alunos
file_teachers = "teachers_puc.json"    # Arquivo que armazenará Professores
file_courses = "courses_puc.json"      # Arquivo que armazenará Disciplinas
file_classes = "classes_puc.json"      # Arquivo que armazenará Turmas
file_id_numbers = "idnumbers_puc.json" # Arquivo que armazenará Matrículas

def display_main_menu(): # Função para exibir a tela do Menu Inicial
    print("\n-------[SISTEMA PUC]-------")
    print("\n       (1) Estudante")
    print("       (2) Professor")
    print("       (3) Disciplina")
    print("       (4) Turma")
    print("       (5) Matrícula")
    print("       (9) Sair")
    print("\n------------------------------")
    return int(input("> Digite uma das opções disponíveis: "))

def display_operations_menu(section): # Função para exibir tela de Operações
    print(f"\n-------[{section}]-------")
    print("\n       (1) Cadastrar")
    print("       (2) Listar")
    print("       (3) Atualizar")
    print("       (4) Excluir")
    print("       (5) Voltar")
    print("\n------------------------------")
    return int(input("> Digite uma das opções disponíveis: "))

def create_operation(section,operation,file_name): # Função para criar/adicionar dados.

    list_for_operation = read_file(file_name) # LÊ/ABRE O RESPECTIVO ARQUIVO

    print(f"\n-----[{section} -> {operation}]-----")
    while True:
        try:  # Garantir que o COD da seção atual seja um número inteiro, ÚNICO e maior que zero.
            current_cod = int(input(f"\n> Digite o Código do(a) {section}: "))
            if current_cod <= 0:
                print("> Valor inválido!")
                continue
            for line in list_for_operation:
                if section == "ESTUDANTE":
                    if line['CODIGO_ESTUDANTE'] == current_cod:  # Garantir que o COD do ESTUDANTE seja único para cada cadastro NOVO!
                        print("> Erro - Código já cadastrado!")
                        break
                elif section == "PROFESSOR":
                    if line['CODIGO_PROFESSOR'] == current_cod:  # Garantir que o COD do PROFESSOR seja único para cada cadastro NOVO!
                        print("> Erro - Código já cadastrado!")
                        break
                elif section == "DISCIPLINA":
                    if line['CODIGO_DISCIPLINA'] == current_cod:  # Garantir que o COD da DISCIPLINA seja único para cada cadastro NOVO!
                        print("> Erro - Código já cadastrado!")
                        break
                elif section == "TURMA":
                    if line['CODIGO_TURMA'] == current_cod:  # Garantir que o COD da TURMA seja único para cada cadastro NOVO!
                        print("> Erro - Código já cadastrado!")
                        break
                else: # section == "MATRICULA"
                    if line['CODIGO_MATRICULA'] == current_cod:  # Garantir que o COD da MATRICULA seja único para cada cadastro NOVO!
                        print("> Erro - Código já cadastrado!")
                        break
            else:
                break
        except ValueError:
            print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.

    if section == "ESTUDANTE" or section == "PROFESSOR":
        if section == "ESTUDANTE":
            current_section = "ESTUDANTE"
        else:
            current_section = "PROFESSOR"
        while True:  # Validar um input de uma String.
            current_name = input(f"> Digite o Nome do {current_section}: ").strip()  # .strip() -> Remove todos os possíveis espaços extras. Por exemplo no início ou final da string.
            if current_name.replace(" ", "").isalpha():  # .replace() -> Remove todos possíveis espaços entre strings
                break  # .isalpha() -> Verifica se o conteúdo restante são apenas caracteres.
            else:
                print("> Valor inválido! Insira apenas caracteres.")
        while True:  # Verificar se são digitos. *Melhoria futura* -> Validar formatação correta do CPF, para ver se é válido.
            cpf = input(f"> Digite o CPF do {current_section}: ").strip()  # Remove possíveis espaços extras.
            if cpf.isdigit() and len(cpf) == 11:  # .isdigit -> Função que verifica se os caracteres são números
                break  # len() -> Delimita a qtd. necessária de digitos.
            else:
                print("> Valor inválido! O CPF É necessário conter 11 digitos")

        if section == "ESTUDANTE":
            dictionary = {'CODIGO_ESTUDANTE': current_cod, "NOME_ESTUDANTE": current_name, 'CPF_ESTUDANTE': cpf}
        else:
            dictionary = {'CODIGO_PROFESSOR': current_cod, "NOME_PROFESSOR": current_name, 'CPF_PROFESSOR': cpf}

    elif section == "DISCIPLINA":
        while True:  # Validar um input de uma String.
            name_course = input(f"> Digite o Nome da DISCIPLINA: ").strip()  # .strip() -> Remove todos os possíveis espaços extras. Por exemplo no início ou final da string.
            if name_course.replace(" ", "").isalpha():  # .replace() -> Remove todos possíveis espaços entre strings
                break  # .isalpha() -> Verifica se o conteúdo restante são apenas caracteres.
            else:
                print("> Valor inválido! Insira apenas caracteres.")
        dictionary = {'CODIGO_DISCIPLINA': current_cod, "NOME_DISCIPLINA": name_course}

    elif section == "TURMA":
        teachers_list = read_file(file_teachers)
        courses_list = read_file(file_courses)
        while True:
            try:  # Garantir que o COD do PROFESSOR exista, para o cadastro.
                cod_teacher = int(input("> Digite o Código do PROFESSOR: "))
                if cod_teacher <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in teachers_list:
                    if dictionary['CODIGO_PROFESSOR'] == cod_teacher: # Garantir que o COD do professor digitado exista na lista de PROFESSORES!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou PROFESSOR não encontrado!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        while True:
            try:  # Garantir que o COD da DISCIPLINA exista, para o cadastro.
                cod_course = int(input("> Digite o Código da DISCIPLINA: "))
                if cod_course <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in courses_list:
                    if dictionary['CODIGO_DISCIPLINA'] == cod_course: # Garantir que o COD da DISCIPLINA digitado exista na lista de DISCIPLINAS!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou DISCIPLINA não encontrada!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.

        # SE ambos os CÓDIGOS (professor,disciplina) existem, a TURMA será criada
        dictionary = {'CODIGO_TURMA': current_cod, 'CODIGO_PROFESSOR': cod_teacher, 'CODIGO_DISCIPLINA': cod_course}

    else: # section == "MATRICULA"
        classes_list = read_file(file_classes)
        students_list = read_file(file_students)
        while True:
            try:  # Garantir que o COD do TURMA exista, para o cadastro.
                cod_class = int(input("> Digite o Código da TURMA: "))
                if cod_class <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in classes_list:
                    if dictionary['CODIGO_TURMA'] == cod_class: # Garantir que o COD da TURMA exista na lista de TURMAS!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou TURMA não encontrado!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        while True:
            try:  # Garantir que o COD do ESTUDANTE exista, para o cadastro.
                cod_student = int(input("> Digite o Código do ESTUDANTE: "))
                if cod_student <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in students_list:
                    if dictionary['CODIGO_ESTUDANTE'] == cod_student: # Garantir que o COD do ESTUDANTE digitado exista na lista de PROFESSORES!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou ESTUDANTE não encontrada!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.

        # SE ambos os CÓDIGOS (professor,disciplina) existem, a TURMA será criada
        dictionary = {'CODIGO_MATRICULA': current_cod, 'CODIGO_TURMA': cod_class, 'CODIGO_ESTUDANTE': cod_student}


    list_for_operation.append(dictionary)
    save_file(list_for_operation, file_name) # ATUALIZA ARQUIVO
    print("\n----------------------------------------------------------------")
    input(f"> {section} cadastrado(a) com sucesso! Pressione Enter para voltar...")
    return list_for_operation # Retornando a lista de cópia, para atualizar a lista original!

def read_operation(section,operation,file_name): # Função para LER/LISTAR dados.

    list_for_operation = read_file(file_name) # LÊ/ABRE O RESPECTIVO ARQUIVO

    print(f"\n-----[{section} -> {operation}]-----")
    if(len(list_for_operation) == 0):  # Se a lista referente a seção escolhida estiver vazia, não terá como LISTAR dados...
        print("\n-----------------------------------")
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
    else:
        print(f"\n> QTD[{len(list_for_operation)}]: \n")
        for dictionary in list_for_operation:
            print(f"- {dictionary}")
        print("\n-----------------------------------")
        input("> Pressione Enter para continuar...")
    return

def update_operation(section,operation,file_name): # Função para atualizar dados.

    list_for_operation = read_file(file_name) # LÊ/ABRE O RESPECTIVO ARQUIVO

    print(f"\n-----[{section} -> {operation}]-----")
    if(len(list_for_operation) == 0):  # Se a lista referente a seção escolhida estiver vazia, não terá como ATUALIZAR dados...
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
        return list_for_operation
    while True:
        try:  # Garantir que o COD seja um número inteiro maior que zero.
            cod_edit = int(input(f"\n> Digite o código do(a) {section} para EDITAR dados: "))
            if cod_edit <= 0:
                print("> Valor inválido!")
                continue
        except ValueError:
            print("> Valor inválido! Insira apenas números.")
            continue

        dictionary_by_edit = None
        for current_dictionary in list_for_operation:
            if section == "ESTUDANTE":
                if current_dictionary['CODIGO_ESTUDANTE'] == cod_edit:
                    dictionary_by_edit = current_dictionary
                    break
            elif section == "PROFESSOR":
                if current_dictionary['CODIGO_PROFESSOR'] == cod_edit:
                    dictionary_by_edit = current_dictionary
                    break
            elif section == "DISCIPLINA":
                if current_dictionary['CODIGO_DISCIPLINA'] == cod_edit:
                    dictionary_by_edit = current_dictionary
                    break
            elif section == "TURMA":
                if current_dictionary['CODIGO_TURMA'] == cod_edit:
                    dictionary_by_edit = current_dictionary
                    break
            elif section == "MATRICULA":
                if current_dictionary['CODIGO_MATRICULA'] == cod_edit:
                    dictionary_by_edit = current_dictionary
                    break

        if dictionary_by_edit is None:
            print(f"> ERROR - Código incorreto ou {section} não encontrado(a)!")
        else:
            break
    print(f"\n> {section} encontrado(a)!")
    if section == "ESTUDANTE":
        while True:  # Validar que o input NAME seja String
            new_name = input(f"> Nome ATUAL: [{dictionary_by_edit["NOME_ESTUDANTE"]}] - Digite o novo NOME para a/o {section}: ").strip()
            if new_name.replace(" ", "").isalpha():
                dictionary_by_edit["NOME_ESTUDANTE"] = new_name
                break
            else:
                print("> Valor inválido! Insira apenas caracteres.")
        while True:  # Validar que o input CPF contenha de 11 digitos
            new_cpf = input(f"> CPF ATUAL: [{dictionary_by_edit['CPF_ESTUDANTE']}] - Digite o novo CPF para o(a) {section}: ")
            if new_cpf.isdigit() and len(new_cpf) == 11:
                dictionary_by_edit['CPF_ESTUDANTE'] = new_cpf
                break
            else:
                print("> Valor inválido! O CPF É necessário conter 11 digitos.")
    elif section == "PROFESSOR":
        while True:  # Validar que o input NAME seja String
            new_name = input(f"> Nome ATUAL: [{dictionary_by_edit["NOME_PROFESSOR"]}] - Digite o novo NOME para o(a) {section}(A): ").strip()
            if new_name.replace(" ", "").isalpha():
                dictionary_by_edit["NOME_PROFESSOR"] = new_name
                break
            else:
                print("> Valor inválido! Insira apenas caracteres.")
        while True:  # Validar que o input CPF contenha de 11 digitos
            new_cpf = input(f"> CPF ATUAL: [{dictionary_by_edit['CPF_PROFESSOR']}] - Digite o novo CPF para o(a) {section}(a): ")
            if new_cpf.isdigit() and len(new_cpf) == 11:
                dictionary_by_edit['CPF_PROFESSOR'] = new_cpf
                break
            else:
                print("> Valor inválido! O CPF É necessário conter 11 digitos.")
    elif section == "DISCIPLINA":
        while True:  # Validar que o input NAME seja String
            new_name = input(f"> Nome ATUAL: [{dictionary_by_edit['NOME_DISCIPLINA']}] - Digite o novo NOME para a {section}: ").strip()
            if new_name.replace(" ", "").isalpha():
                dictionary_by_edit["NOME_DISCIPLINA"] = new_name
                break
            else:
                print("> Valor inválido! Insira apenas caracteres.")
    elif section == "TURMA":
        teachers_list = read_file(file_teachers)
        courses_list = read_file(file_courses)
        while True:
            try:  # Garantir que o COD do PROFESSOR exista, para o ATUALIZAR o cadastro.
                cod_teacher = int(input("> Digite o Código do PROFESSOR: "))
                if cod_teacher <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in teachers_list:
                    if dictionary['CODIGO_PROFESSOR'] == cod_teacher:  # Garantir que o COD do professor digitado exista na lista de PROFESSORES!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou PROFESSOR não encontrado!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        while True:
            try:  # Garantir que o COD da DISCIPLINA exista, para ATUALIZAR o cadastro.
                cod_course = int(input("> Digite o Código da DISCIPLINA: "))
                if cod_course <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in courses_list:
                    if dictionary['CODIGO_DISCIPLINA'] == cod_course:  # Garantir que o COD da DISCIPLINA digitado exista na lista de DISCIPLINAS!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou DISCIPLINA não encontrada!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        # SE ambos os CÓDIGOS (professor,disciplina) existem, a ATUALIZAÇÃO de dados será feita!
        dictionary_by_edit['CODIGO_PROFESSOR'] = cod_teacher
        dictionary_by_edit['CODIGO_DISCIPLINA'] = cod_course
    elif section == "MATRICULA":
        classes_list = read_file(file_classes)
        students_list = read_file(file_students)
        while True:
            try:  # Garantir que o COD do TURMA exista, para ATUALIZAR dados.
                cod_class = int(input("> Digite o Código da TURMA: "))
                if cod_class <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in classes_list:
                    if dictionary['CODIGO_TURMA'] == cod_class:  # Garantir que o COD da TURMA exista na lista de TURMAS!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou TURMA não encontrado!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        while True:
            try:  # Garantir que o COD do ESTUDANTE exista, para o cadastro.
                cod_student = int(input("> Digite o Código do ESTUDANTE: "))
                if cod_student <= 0:
                    print("> Valor inválido!")
                    continue
                found = False
                for dictionary in students_list:
                    if dictionary['CODIGO_ESTUDANTE'] == cod_student:  # Garantir que o COD do ESTUDANTE digitado exista na lista de ESTUDANTES!
                        found = True
                        break
                if not found:
                    print("> Erro - Código incorreto ou ESTUDANTE não encontrada!")
                    continue
                break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")  # Garante que aceite apenas números inteiros.
        # SE ambos os CÓDIGOS (turma,estudante) existem, a ATUALIZAÇÃO de dados será feita!
        dictionary_by_edit['CODIGO_TURMA'] = cod_class
        dictionary_by_edit['CODIGO_ESTUDANTE'] = cod_student

    save_file(list_for_operation, file_name)  # ATUALIZA ARQUIVO
    print("\n----------------------------------------------------------------")
    input(f"> Dados do(a) {section} atualizados com sucesso! Pressione Enter para voltar... ")

def delete_operation(section,operation,file_name): # Função para remover/apagar dados.

    list_for_operation = read_file(file_name)  # LÊ ARQUIVO EXISTENTE

    print(f"\n-----[{section} -> {operation}]-----")
    if(len(list_for_operation) == 0):  # Se a lista referente a seção escolhida estiver vazia, não terá como DELETAR dados...
        print("\n------------------------------------------------------------------------------------------------")
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
        return list_for_operation

    while True:
        try:  # Garantir que o COD seja um número inteiro maior que zero.
            cod_delete = int(input(f"\n> Digite o código do(a) {section} para Excluir do sistema: "))
            if cod_delete <= 0:
                print("> Valor inválido!")
                continue
        except ValueError:
            print("> Valor inválido! Insira apenas números.")

        dictionary_by_delete = None
        for current_dictionary in list_for_operation:
            if section == "ESTUDANTE":
                if cod_delete == current_dictionary['CODIGO_ESTUDANTE']:
                    dictionary_by_delete = current_dictionary
                    break
            elif section == "PROFESSOR":
                if  cod_delete ==  current_dictionary['CODIGO_PROFESSOR']:
                    dictionary_by_delete = current_dictionary
                    break
            elif section == "DISCIPLINA":
                    if cod_delete == current_dictionary['CODIGO_DISCIPLINA']:
                        dictionary_by_delete = current_dictionary
                        break
            elif section == "TURMA":
                if cod_delete == current_dictionary['CODIGO_TURMA']:
                    dictionary_by_delete = current_dictionary
                    break
            else:
                if section == "MATRICULA":
                    if cod_delete == current_dictionary['CODIGO_MATRICULA']:
                        dictionary_by_delete = current_dictionary
                        break

        if dictionary_by_delete is None:
            print(f"> ERROR - Código incorreto ou {section} não encontrado(a)!")
        else:
            break

    print("\n----------------------------------------------------------------")
    while True:
        if section == "ESTUDANTE":
            resp = input(f"> Deseja excluir [{dictionary_by_delete["NOME_ESTUDANTE"]}] da lista de {section}S? [s/n] ").lower()
        elif section == "PROFESSOR":
            resp = input(f"> Deseja excluir [{dictionary_by_delete["NOME_PROFESSOR"]}] da lista de {section}ES? [s/n] ").lower()
        elif section == "DISCIPLINA":
            resp = input(f"> Deseja excluir [{dictionary_by_delete["NOME_DISCIPLINA"]}] da lista de {section}S? [s/n] ").lower()
        elif section == "TURMA":
            resp = input(f"> Deseja excluir a TURMA [{dictionary_by_delete['CODIGO_TURMA']}] da lista de {section}S? [s/n] ").lower()
        elif section == "MATRICULA":
            resp = input(f"> Deseja excluir a MATRÍCULA [{dictionary_by_delete['CODIGO_MATRICULA']}] da lista de {section}S? [s/n] ").lower()

        if resp == "s":
            if section == "PROFESSOR": # Verificar se um PROFESSOR esta cadastrado em uma TURMA, antes de confirmar sua exclusão!
                classes_list = read_file(file_classes)
                found = False
                for dictionary in classes_list:
                    if dictionary['CODIGO_PROFESSOR'] == cod_delete:
                        found = True # Booleano para confirmar que encontrou o PROFESSOR cadastrado em uma TURMA.
                        break
                if found: # SE encontrar, barrará a exclusão do PROFESSOR, para garantir a integridade do sistema. (Será necessário atualizar o PROFESSOR desta TURMA ou excluir a TURMA por completo)
                    print(f"> ERRO - Não é possível excluir o PROFESSOR:[{dictionary_by_delete['NOME_PROFESSOR']}], pois ele esta cadastrado na TURMA: [{dictionary['CODIGO_TURMA']}]!")
                else:
                    list_for_operation.remove(dictionary_by_delete)
                    save_file(list_for_operation, file_name)
                    print("\n---------------------------------------------------------------------")
                    input(f"> {section} excluído(a) com sucesso! Pressione Enter para voltar...")
                    break
            elif section == "DISCIPLINA": # Verificar se uma DISCIPLINA esta cadastrado em uma TURMA, antes de confirmar sua exclusão!
                classes_list = read_file(file_classes)
                found = False
                for dictionary in classes_list:
                    if dictionary['CODIGO_DISCIPLINA'] == cod_delete:
                        found = True
                        break
                if found: # SE encontrar, barrará a exclusão da DISCIPLINA, para garantir a integridade do sistema. (Será necessário atualizar outra DISCIPLINA desta TURMA ou excluir a TURMA por completo)
                    print(f"> ERROR - Não é possível excluir a DISCIPLINA:[{dictionary_by_delete['NOME_DISCIPLINA']}], pois ela esta cadastrado na TURMA: [{dictionary['CODIGO_TURMA']}]!")
                else:
                    list_for_operation.remove(dictionary_by_delete)
                    save_file(list_for_operation, file_name)
                    print("\n---------------------------------------------------------------------")
                    input(f"> {section} excluído(a) com sucesso! Pressione Enter para voltar...")
                    break
            elif section == "ESTUDANTE": # Verificar se um ESTUDANTES esta cadastrado em uma MATRICULA, antes de confirmar sua exclusão!
                students_list = read_file(file_id_numbers)
                found = False
                for dictionary in students_list:
                    if dictionary['CODIGO_ESTUDANTE'] == cod_delete:
                        found = True
                        break
                if found: # SE encontrar, barrará a exclusão do ESTUDANTE, para garantir a integridade do sistema. (Será necessário atualizar outro ESTUDANTE desta MATRICULA ou excluir a MATRICULA por completo)
                    print(f"> ERROR - Não é possível excluir a(o):[{dictionary_by_delete['NOME_ESTUDANTE']}], pois ele(a) esta cadastrado na MATRICULA: [{dictionary['CODIGO_MATRICULA']}]!")
                else:
                    list_for_operation.remove(dictionary_by_delete)
                    save_file(list_for_operation, file_name)
                    print("\n---------------------------------------------------------------------")
                    input(f"> {section} excluído(a) com sucesso! Pressione Enter para voltar...")
                    break
            elif section == "TURMA" : # Verificar se uma TURMA esta cadastrada em uma MATRICULA, antes de confirmar sua exclusão!
                classes_list = read_file(file_id_numbers)
                found = False
                for dictionary in classes_list:
                    if dictionary['CODIGO_TURMA'] == cod_delete:
                        found = True
                        break
                if found: # SE encontrar, barrará a exclusão da TURMA, para garantir a integridade do sistema. (Será necessário atualizar outra TURMA desta MATRICULA ou excluir a MATRICULA por completo)
                    print(f"> ERROR - Não é possível excluir a TURMA:[{dictionary_by_delete['CODIGO_TURMA']}], pois ela esta cadastrado na MATRICULA: [{dictionary['CODIGO_MATRICULA']}]!")
                else:
                    list_for_operation.remove(dictionary_by_delete)
                    save_file(list_for_operation, file_name) # ATUALIZA ARQUIVO
                    print("\n---------------------------------------------------------------------")
                    input(f"> {section} excluído(a) com sucesso! Pressione Enter para voltar...")
                    break
        elif resp == "n":
            print("\n----------------------------------------------------")
            input("> Exclusão cancelada. Pressione Enter para voltar...")
            break
        else:
            print("> ERROR - Opção inválida!")

def save_file(list_by_save, file_name): # Função para CRIAR/SALVAR arquivos .JSON com dados.
    with open(file_name, "w", encoding='utf-8') as file_open:
        json.dump(list_by_save, file_open, ensure_ascii=False) # Dump -> "jogar"/ salvar lista no arquivo aberto

def read_file(file): # Função para LER dados salvos nos arquivos .JSON
    try:
        with open(file, "r") as file_open:
            list_by_save = json.load(file_open)
        return list_by_save
    except FileNotFoundError:
        return []

while loop_menu == True: # Looping da Tela Inicial - MAIN()
    while True:
        try:
            option = display_main_menu()
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
    else:   # Este else existe, pois no momento não temos as opções 6,7,8 disponíveis. Futura implementação...
        print("\n> Opção indisponível! Tente novamente.")

    while loop_operations == True: # Looping da tela secundária de Operações

        if section == "ESTUDANTE":
            file_for_operation = file_students
        elif section == "PROFESSOR":
            file_for_operation = file_teachers
        elif section == "DISCIPLINA":
            file_for_operation = file_courses
        elif section == "TURMA":
            file_for_operation = file_classes
        elif section == "MATRÍCULA":
            file_for_operation = file_id_numbers

        while True:
            try:
                option = display_operations_menu(section)
                if option <= 0 or option > 5:
                    print("> Opção indisponível! Tente novamente.")    # Validação para garantir que o usuário escolha um número presente neste período.
                else:
                    break
            except ValueError:
                    print("> Valor inválido! Insira apenas números.") # Garante que aceite apenas números inteiros.
        if option == 1:  # OPERAÇÃO CADASTRAR
            operation = "CADASTRAR"
            create_operation(section, operation, file_for_operation)
        elif option == 2:  # OPERAÇÃO LISTAR
            operation = "LISTAR"
            read_operation(section, operation, file_for_operation)
        elif option == 3:  # OPERAÇÃO EDITAR
            operation = "ATUALIZAR"
            update_operation(section, operation, file_for_operation)
        elif option == 4:  # OPERAÇÃO EXCLUIR
            operation = "EXCLUIR"
            delete_operation(section, operation, file_for_operation)
        elif option == 5:  # VOLTAR
            loop_operations = False

print("\n>> ENCERRANDO SISTEMA PUC... Até a próxima! :)")