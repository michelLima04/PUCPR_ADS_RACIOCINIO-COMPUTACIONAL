# Sistema de Gerenciamento Acadêmico (Sistema PUC) 🎓

Este projeto foi desenvolvido como requisito para a disciplina de Raciocínio Computacional do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da PUCPR. A temática deste projeto da disciplina é um Sistema de Gerenciamento Acadêmico. O projeto foi construído inteiramente em Python, utilizando a IDE PyCharm.

O sistema foi desenvolvido incrementalmente durante toda a disciplina de Raciocínio Computacional, partindo da lógica de menus na primeira etapa e evoluindo para um sistema completo com persistência em arquivos.

## 🚀 Funcionalidades Obrigatórias

[cite_start]O sistema deverá oferecer a possibilidade de cadastro dos seguintes dados[cite: 7]:
* **Estudante**
* **Disciplina**
* **Professor**
* **Turma**
* **Matrícula** 

Para cada uma das funcionalidades descritas, é possível realizar as seguintes funcionalidades no modelo CRUD:
* Incluir novos registros.
* Listar os dados cadastrados.
* Atualizar informações existentes.
* Excluir registros do sistema.

## 🛠️ Tecnologias e Conceitos Aplicados

Durante o desenvolvimento, diversos conceitos fundamentais de lógica de programação foram aplicados seguindo boas práticas de programação:

* **Persistência de Dados (JSON):** Para não perder dados ao reiniciar o programa, os dados devem ser armazenados em uma lista, e posteriormente em um arquivo JSON. Foram utilizados arquivos para a persistência dos dados cadastrados.
* **Estruturas de Dados:** Utilização de estruturas de dados compostas (listas, dicionários, e/ou tuplas) para organização dos dados.
* **Controle de Fluxo:** Utilização de estruturas condicionais (if/elif/else) no código, além da utilização de estruturas de repetição (for ou while) para navegação dos menus.
* **Modularização:** Utilização de funções para modularizar as principais funcionalidades da aplicação[cite: 101]. Funções genéricas foram criadas para evitar duplicação de código.
* **Validação e Integridade:** O sistema conta com validação de dados na manipulação de turmas e matrículas (verificar se um código já existe antes de incluir uma nova turma/matrícula com o mesmo código). Também conta com validações de dados e controle de possíveis exceções/erros de execução (try/except).

## 💻 Como Executar o Projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.
2. Clone este repositório:
   `git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git`
3. Navegue até o diretório do projeto:
   `cd NOME_DO_REPOSITORIO`
4. Execute o arquivo principal:
   `python main_SistemaPUC_Michel.py`
5. Os arquivos `.json` (como `students_puc.json`, `teachers_puc.json`, etc.) serão gerados automaticamente no mesmo diretório assim que os primeiros cadastros forem realizados.

## 👨‍💻 Autor

**Michel Urban Rosendo de Lima**
Estudante de Análise e Desenvolvimento de Sistemas (1º Período/2025)
