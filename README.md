# Sistema de Gerenciamento Acadêmico (Sistema PUC) 🎓

Este projeto foi desenvolvido como requisito para a disciplina de Raciocínio Computacional do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da PUCPR. [cite_start]A temática de nosso projeto da disciplina será um Sistema de Gerenciamento Acadêmico[cite: 3]. [cite_start]O projeto foi construído inteiramente em Python [cite: 126] utilizando a IDE PyCharm.

[cite_start]O sistema foi desenvolvido incrementalmente durante a disciplina[cite: 4], partindo da lógica de menus na primeira etapa e evoluindo para um sistema completo com persistência em arquivos.


## 🚀 Funcionalidades Obrigatórias

[cite_start]O sistema deverá oferecer a possibilidade de cadastro dos seguintes dados[cite: 7]:
* [cite_start]**Estudante** [cite: 8]
* [cite_start]**Disciplina** [cite: 9]
* [cite_start]**Professor** [cite: 10]
* [cite_start]**Turma** [cite: 11]
* [cite_start]**Matrícula** [cite: 12]

[cite_start]Para cada uma das funcionalidades descritas, deve ser possível realizar as seguintes funcionalidades[cite: 13]:
* [cite_start]Incluir novos registros[cite: 14].
* [cite_start]Listar os dados cadastrados[cite: 15].
* [cite_start]Atualizar informações existentes[cite: 17].
* [cite_start]Excluir registros do sistema[cite: 16].

## 🛠️ Tecnologias e Conceitos Aplicados

[cite_start]Durante o desenvolvimento, diversos conceitos fundamentais de lógica de programação foram aplicados seguindo boas práticas de programação[cite: 102]:

* [cite_start]**Persistência de Dados (JSON):** Para não perder dados ao reiniciar o programa, os dados devem ser armazenados em uma lista, e posteriormente em um arquivo JSON[cite: 18]. [cite_start]Foram utilizados arquivos para a persistência dos dados cadastrados[cite: 100].
* [cite_start]**Estruturas de Dados:** Utilização de estruturas de dados compostas (listas, dicionários, e/ou tuplas) para organização dos dados[cite: 99].
* [cite_start]**Controle de Fluxo:** Utilização de estruturas condicionais (if/elif/else) no código [cite: 97][cite_start], além da utilização de estruturas de repetição (for ou while) para navegação dos menus[cite: 98].
* [cite_start]**Modularização:** Utilização de funções para modularizar as principais funcionalidades da aplicação[cite: 101]. Funções genéricas foram criadas para evitar duplicação de código.
* [cite_start]**Validação e Integridade:** O sistema conta com validação de dados na manipulação de turmas e matrículas (verificar se um código já existe antes de incluir uma nova turma/matrícula com o mesmo código)[cite: 94]. [cite_start]Também conta com validações de dados e controle de possíveis exceções/erros de execução (try/except)[cite: 104].

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
