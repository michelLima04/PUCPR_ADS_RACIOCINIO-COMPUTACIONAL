# Instituição: Pontifícia Universidade Católica do Paraná PUCPR
# Curso: Tecnologia em Análise e Desenvolvimento de Sistemas
# Aluno/Autor: Michel Urban Rosendo de Lima
# Disciplina: Raciocínio Computacional (1ºPeríodo/2025)
# Tema: Sistema de Gerenciamento PUC

import json # Importação da biblioteca JSON

loop_menu = True
file_students   = "students_puc.json"  # Arquivo que armazenará Alunos
file_teachers   = "teachers_puc.json"  # Arquivo que armazenará Professores
file_courses    = "courses_puc.json"   # Arquivo que armazenará Disciplinas
file_classes    = "classes_puc.json"   # Arquivo que armazenará Turmas
file_id_numbers = "idnumbers_puc.json" # Arquivo que armazenará Matrículas

def get_valid_integer(message): # Valida se os Imputs de números são inteiros e positivos.
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            print("> Valor inválido!")
        except ValueError:
            print("> Valor inválido! Insira apenas números.")

def get_valid_string(message): # Verificar se os Imputs de String contém apenas Caracteres
    while True:
        text = input(message).strip() # .strip() -> Remove todos os possíveis espaços extras. Por exemplo no início ou final da string.
        if text.replace(" ", "").isalpha(): # .replace() -> Remove todos possíveis espaços entre strings. .isalpha() -> Verifica se o conteúdo restante são apenas caracteres.
            return text
        print("> Valor inválido! Insira apenas caracteres.")

def get_valid_cpf(message): # Verificar se o input de CPF são 11 Digitos.
    while True:
        cpf = input(message).strip() # Remove possíveis espaços extras.
        if cpf.isdigit() and len(cpf) == 11: # .isdigit -> Função que verifica se os caracteres são números. len() -> Delimita a qtd. necessária de digitos.
            return cpf
        print("> Valor inválido! O CPF precisa conter 11 digitos.")

def get_id_key(section): # Retorna a Chave Primária correspondente à Seção Atual
    keys = {
        "ESTUDANTE": "CODIGO_ESTUDANTE",
        "PROFESSOR": "CODIGO_PROFESSOR",
        "DISCIPLINA": "CODIGO_DISCIPLINA",
        "TURMA": "CODIGO_TURMA",
        "MATRÍCULA": "CODIGO_MATRICULA",
        "MATRICULA": "CODIGO_MATRICULA"
    }
    return keys.get(section)

def get_existing_foreign_key(message, file_name_to_check, key_to_check, entity_name):
    # Garantir que os demais COD's das Entidades existam, para o Cadastro ou Atualização de Dados

    list_to_check = read_file(file_name_to_check)
    while True:
        cod = get_valid_integer(message)
        for dictionary in list_to_check:
            if dictionary[key_to_check] == cod:
                return cod
        print(f"> Erro - Código incorreto ou {entity_name} não encontrado(a)!")

def display_main_menu(): # Função para exibir a tela do Menu Inicial
    print("\n-------[SISTEMA PUC]-------")
    print("\n       (1) Estudante")
    print("       (2) Professor")
    print("       (3) Disciplina")
    print("       (4) Turma")
    print("       (5) Matrícula")
    print("       (6) Sair")
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

def create_operation(section, operation, file_name):  # Função para criar/adicionar dados.
    list_for_operation = read_file(file_name)  # LÊ/ABRE O RESPECTIVO ARQUIVO
    id_key = get_id_key(section)

    print(f"\n-----[{section} -> {operation}]-----")

    # Garantir que o COD da seção atual seja um número inteiro, ÚNICO e maior ou igual a zero.
    while True:
        # Instrução visual para o usuário saber como cancelar um cadastro
        current_cod = get_valid_integer(f"\n> Digite o Código do(a) {section} (ou 0 para cancelar/voltar): ")

        if current_cod == 0:
            print(f"\n> Cadastro de {section} cancelado. Retornando ao menu...")
            return list_for_operation

        codigo_existe = any(linha[id_key] == current_cod for linha in list_for_operation)
        if codigo_existe:
            print("> Erro - Código já cadastrado!")
        else:
            break

    dictionary = {}

    if section in ["ESTUDANTE", "PROFESSOR"]:
        current_name = get_valid_string(f"> Digite o Nome do(a) {section}: ")
        cpf = get_valid_cpf(f"> Digite o CPF do(a) {section}: ")

        dictionary[id_key] = current_cod
        dictionary[f"NOME_{section}"] = current_name
        dictionary[f"CPF_{section}"] = cpf

    elif section == "DISCIPLINA":
        name_course = get_valid_string(f"> Digite o Nome da DISCIPLINA: ")
        dictionary = {id_key: current_cod, "NOME_DISCIPLINA": name_course}

    elif section == "TURMA":
        cod_teacher = get_existing_foreign_key("> Digite o Código do PROFESSOR: ", file_teachers, 'CODIGO_PROFESSOR',
                                               'PROFESSOR')
        cod_course = get_existing_foreign_key("> Digite o Código da DISCIPLINA: ", file_courses, 'CODIGO_DISCIPLINA',
                                              'DISCIPLINA')
        # SE ambos os CÓDIGOS (professor,disciplina) existem, a TURMA será criada
        dictionary = {id_key: current_cod, 'CODIGO_PROFESSOR': cod_teacher, 'CODIGO_DISCIPLINA': cod_course}

    else:  # section == "MATRICULA" ou "MATRÍCULA"
        cod_class = get_existing_foreign_key("> Digite o Código da TURMA: ", file_classes, 'CODIGO_TURMA', 'TURMA')
        cod_student = get_existing_foreign_key("> Digite o Código do ESTUDANTE: ", file_students, 'CODIGO_ESTUDANTE',
                                               'ESTUDANTE')
        # SE ambos os CÓDIGOS (turma,estudante) existem, a MATRICULA será criada
        dictionary = {id_key: current_cod, 'CODIGO_TURMA': cod_class, 'CODIGO_ESTUDANTE': cod_student}

    list_for_operation.append(dictionary)
    save_file(list_for_operation, file_name)  # ATUALIZA ARQUIVO
    print("\n----------------------------------------------------------------")
    input(f"> {section} cadastrado(a) com sucesso! Pressione Enter para voltar...")
    return list_for_operation

def read_operation(section, operation, file_name):  # Função para LER/LISTAR dados.
    list_for_operation = read_file(file_name)  # LÊ/ABRE O RESPECTIVO ARQUIVO

    print(f"\n-----[{section} -> {operation}]-----")
    if len(list_for_operation) == 0:  # Se a lista referente a seção escolhida estiver vazia, não terá como LISTAR dados...
        print("\n-----------------------------------")
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
    else:
        print(f"\n> QTD[{len(list_for_operation)}]: \n")
        for dictionary in list_for_operation:
            print(f"- {dictionary}")
        print("\n-----------------------------------")
        input("> Pressione Enter para continuar...")
    return

def update_operation(section, operation, file_name):  # Função para atualizar dados.

    list_for_operation = read_file(file_name)  # LÊ/ABRE O RESPECTIVO ARQUIVO
    id_key = get_id_key(section)

    print(f"\n-----[{section} -> {operation}]-----")
    if len(list_for_operation) == 0:
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
        return list_for_operation

    while True:
        cod_edit = get_valid_integer(f"\n> Digite o código do(a) {section} para EDITAR dados: ")

        if cod_edit == 0:
            print(f"\n> Atualização de {section} cancelada. Retornando ao menu...")
            return list_for_operation

        dictionary_by_edit = None
        for current_dictionary in list_for_operation:
            if current_dictionary[id_key] == cod_edit:
                dictionary_by_edit = current_dictionary
                break

        if dictionary_by_edit is None:
            print(f"> ERROR - Código incorreto ou {section} não encontrado(a)!")
        else:
            break

    print(f"\n> {section} encontrado(a)! Responda [s/n] para os dados que deseja alterar:")

    if section in ["ESTUDANTE", "PROFESSOR"]:
        if input(f"> Deseja alterar o NOME atual [{dictionary_by_edit[f'NOME_{section}']}]? [s/n]: ").strip().lower() == 's':
            new_name = get_valid_string(f"> Digite o novo NOME para o(a) {section}: ")
            dictionary_by_edit[f'NOME_{section}'] = new_name

        if input(f"> Deseja alterar o CPF atual [{dictionary_by_edit[f'CPF_{section}']}]? [s/n]: ").strip().lower() == 's':
            new_cpf = get_valid_cpf(f"> Digite o novo CPF para o(a) {section}: ")
            dictionary_by_edit[f'CPF_{section}'] = new_cpf

    elif section == "DISCIPLINA":
        if input(f"> Deseja alterar o NOME atual [{dictionary_by_edit['NOME_DISCIPLINA']}]? [s/n]: ").strip().lower() == 's':
            new_name = get_valid_string(f"> Digite o novo NOME para a {section}: ")
            dictionary_by_edit["NOME_DISCIPLINA"] = new_name

    elif section == "TURMA":
        # Pergunta sobre o Professor com input simples
        if input(f"> Deseja alterar o CÓD. PROFESSOR atual [{dictionary_by_edit['CODIGO_PROFESSOR']}]? [s/n]: ").strip().lower() == 's':
            cod_teacher = get_existing_foreign_key("> Digite o novo Código do PROFESSOR: ", file_teachers,
                                                   'CODIGO_PROFESSOR', 'PROFESSOR')
            dictionary_by_edit['CODIGO_PROFESSOR'] = cod_teacher

        # Pergunta sobre a Disciplina com input simples
        if input(f"> Deseja alterar o CÓD. DISCIPLINA atual [{dictionary_by_edit['CODIGO_DISCIPLINA']}]? [s/n]: ").strip().lower() == 's':
            cod_course = get_existing_foreign_key("> Digite o novo Código da DISCIPLINA: ", file_courses,
                                                  'CODIGO_DISCIPLINA', 'DISCIPLINA')
            dictionary_by_edit['CODIGO_DISCIPLINA'] = cod_course

    elif section in ["MATRICULA", "MATRÍCULA"]:
        if input(f"> Deseja alterar o CÓD. TURMA atual [{dictionary_by_edit['CODIGO_TURMA']}]? [s/n]: ").strip().lower() == 's':
            cod_class = get_existing_foreign_key("> Digite o novo Código da TURMA: ", file_classes, 'CODIGO_TURMA',
                                                 'TURMA')
            dictionary_by_edit['CODIGO_TURMA'] = cod_class

        if input(f"> Deseja alterar o CÓD. ESTUDANTE atual [{dictionary_by_edit['CODIGO_ESTUDANTE']}]? [s/n]: ").strip().lower() == 's':
            cod_student = get_existing_foreign_key("> Digite o novo Código do ESTUDANTE: ", file_students,
                                                   'CODIGO_ESTUDANTE', 'ESTUDANTE')
            dictionary_by_edit['CODIGO_ESTUDANTE'] = cod_student

    save_file(list_for_operation, file_name)  # ATUALIZA ARQUIVO
    print("\n----------------------------------------------------------------")
    input(f"> Dados do(a) {section} verificados e atualizados com sucesso! Pressione Enter para voltar... ")

def delete_operation(section, operation, file_name):  # Função para remover/apagar dados.
    list_for_operation = read_file(file_name)  # LÊ ARQUIVO EXISTENTE
    id_key = get_id_key(section)

    print(f"\n-----[{section} -> {operation}]-----")
    if len(list_for_operation) == 0:  # Se a lista referente a seção escolhida estiver vazia, não terá como DELETAR dados...
        print("\n------------------------------------------------------------------------------------------------")
        input(f"> Nenhum(a) {section} cadastrado(a) no sistema para {operation}! Pressione Enter para voltar...")
        return list_for_operation

    while True:
        cod_delete = get_valid_integer(f"\n> Digite o código do(a) {section} para Excluir do sistema: ")

        if cod_delete == 0:
            print(f"\n> Exclusão de {section} cancelada. Retornando ao menu...")
            return list_for_operation

        dictionary_by_delete = None
        for current_dictionary in list_for_operation:
            if current_dictionary[id_key] == cod_delete:
                dictionary_by_delete = current_dictionary
                break

        if dictionary_by_delete is None:
            print(f"> ERROR - Código incorreto ou {section} não encontrado(a)!")
        else:
            break

    print("\n----------------------------------------------------------------")
    while True:
        # Busca o nome para exibição (se não tiver nome, exibe o código)
        nome_exibicao = dictionary_by_delete.get(f"NOME_{section}", dictionary_by_delete.get(id_key))
        resp = input(f"> Deseja excluir [{nome_exibicao}] da lista de {section}S? [s/n] ").lower()

        if resp == "s":
            # Verificar integridade (se o dado está sendo usado em outra tabela)
            is_bound = False
            bound_file = None
            bound_key = None

            if section == "PROFESSOR":
                bound_file, bound_key = file_classes, 'CODIGO_PROFESSOR'
            elif section == "DISCIPLINA":
                bound_file, bound_key = file_classes, 'CODIGO_DISCIPLINA'
            elif section == "ESTUDANTE":
                bound_file, bound_key = file_id_numbers, 'CODIGO_ESTUDANTE'
            elif section == "TURMA":
                bound_file, bound_key = file_id_numbers, 'CODIGO_TURMA'

            if bound_file and bound_key:
                dependency_list = read_file(bound_file)
                for dep_dict in dependency_list:
                    if dep_dict[bound_key] == cod_delete:
                        is_bound = True
                        if section in ["PROFESSOR", "DISCIPLINA"]:
                            print(
                                f"> ERRO - Não é possível excluir, pois está cadastrado na TURMA: [{dep_dict['CODIGO_TURMA']}]!")
                        else:
                            print(
                                f"> ERROR - Não é possível excluir, pois está cadastrado na MATRICULA: [{dep_dict['CODIGO_MATRICULA']}]!")
                        break

            if is_bound:
                break  # Cancela a exclusão pois viola a integridade do sistema
            else:
                list_for_operation.remove(dictionary_by_delete)
                save_file(list_for_operation, file_name)
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

def main():
    loop_menu = True

    while loop_menu:  # Looping da Tela Inicial

        # Menu Principal
        while True:
            try:
                option = display_main_menu()
                if option <= 0 or option > 6:
                    print("> Opção indisponível! Tente novamente.")
                else:
                    break
            except ValueError:
                print("> Valor inválido! Insira apenas números.")

        loop_operations = False
        section = ""

        # Definição da Seção
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
        elif option == 6:
            loop_menu = False
            continue

        # Looping da tela Secundária de Operações
        while loop_operations:

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
                    op_sec = display_operations_menu(section)
                    if op_sec <= 0 or op_sec > 5:
                        print("> Opção indisponível! Tente novamente.")
                    else:
                        break
                except ValueError:
                    print("> Valor inválido! Insira apenas números.")

            if op_sec == 1:
                create_operation(section, "CADASTRAR", file_for_operation)
            elif op_sec == 2:
                read_operation(section, "LISTAR", file_for_operation)
            elif op_sec == 3:
                update_operation(section, "ATUALIZAR", file_for_operation)
            elif op_sec == 4:
                delete_operation(section, "EXCLUIR", file_for_operation)
            elif op_sec == 5:
                loop_operations = False

    print("\n>> ENCERRANDO SISTEMA PUC... Até a próxima! :)")

if __name__ == "__main__":
    main()