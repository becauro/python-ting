# Boas vindas ao repositório do projeto TING(Trybe is not Google)!


# Habilidades (Hard skills) desse projeto:

- Manipular Pilhas

- Manipular Deque

- Manipular Nó & Listas ligadas

- Manipular Listas duplamentes ligadas

--- 


## Sobre o projeto

Por se tratar de um projeto (bootcamp) feito através da @Tryber, o nome do sistema é **ting** (`Trybe Is Not Google`).

Trata -se de um programa que simula o algoritmo de indexação de documentos similar ao do Google. Ou seja, um programa que permita anexar arquivos de texto e posteriormente opere funções de busca sobre tais arquivos

> Com a quantidade de informações disponíveis na Web, encontrar o que você precisa seria quase impossível sem nenhuma ajuda para classificá-las. Os sistemas de classificação do Google organizam centenas de bilhões de páginas da Web, no índice da pesquisa, para fornecer os resultados mais úteis e relevantes em uma fração de segundo. Além disso tudo, a Google também precisa se preocupar em apresentar os resultados de uma maneira que ajude você a encontrar o que está procurando com mais facilidade ainda.

#### Analisar palavras

> Compreender o significado da sua pesquisa é crucial para retornarmos boas respostas. Por isso, para encontrar páginas com informações relevantes, nosso primeiro passo é analisar o significado das palavras na consulta de pesquisa. Desenvolvemos modelos linguísticos para decifrar as sequências de palavras que precisamos procurar no índice.

Não iremos nos apegar a análise de significados ou busca por sinônimos. Nosso objetivo será identificar ocorrências de termos em arquivos _TXT_. Neste contexto, a idéia do programa é permitir anexar arquivos de texto e posteriormente operar funções de busca sobre tais arquivos.

Sendo assim o programa deverá possui dois módulos:

- Modo gerenciamento de arquivos (`ting_file_management`);

- Modo de buscas (`ting_word_searches`).

---

## Estrutura

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste (`tests`) criados. Há também o diretório `statics` que contém os arquivos necessários para realização de testes, caso julgue necessário, sinta-se à vontade para criar novos arquivos ou editar o conteúdo dos arquivos existentes. Veja abaixo:

```md
.
├── statics
│   ├── arquivo_teste.txt
│   ├── novo_paradigma_globalizado.txt
│   └── novo_paradigma_globalizado-min.txt
├── tests
├── ting_file_management
│   ├── file_management.py
│   └── file_process.py
├── ting_word_searches
│   └── word_search.py
├── README.md
├── requirements.txt
└── setup.cfg
```



### Dependências

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. 



## Instruções de compilação

1. Clone de repositório

- `git clone git@github.com:tryber/sd-012-project-ting.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-012-project-ting`

2. Criação do ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instalação das dependências

- `python3 -m pip install -r dev-requirements.txt`

---



## Testes

Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

---



## LINT

Para verificar o guia de estilo do Python, o flake8 foi usado. Verificação manual é feita com o comando:

```bash
$ python3 -m flake8
```
---



## Requisitos Funcionais:


### Pacote `ting_file_management`

#### 1 - Implementação de uma fila para armazenar os arquivos que serão lidos.

A classe `Queue`, presente no arquivo `queue.py` foi utilizado para essa implementação.

Nessa fila (Queue) foi usado uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair.

Implementado os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

O tamanho da fila é exposto através do método `__len__` que, após implementeado, permite o uso de `len(instancia_da_fila)`.

Na busca, caso um índice inválido seja passado, uma exceção do tipo `IndexError` é lançada. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.


#### 2 - Implementação da função `txt_importer` dentro do módulo `file_management` a qual é capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Todas as mensagens de erro vão para a `stderr`.

**Exemplo simples de um arquivo txt a ser importado:**

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```

- Caso o arquivo TXT não exista, é exibido a mensagem: "Arquivo {path_file} não encontrado";

- Caso a extensão do arquivo seja diferente de .txt, é exibido uma mensagem: "Formato inválido" na `stderr`;

- A função retorna uma lista contendo as linhas do arquivo.


#### 3 - Implementação da função `process` dentro do módulo `file_process` é capaz de ler o arquivo carregado na função anterior e efetuar o preprocessamento do conteúdo.

**Exemplo de retorno**:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Nome do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```

- O exemplo de retorno acima é emitido após cada nova inserção válida, via `stdout`;

- A função recebe como parâmetro a fila implementada no requisito 1 e o caminho do arquivo.

- A instância da fila recebida por parâmetro é utilizada para registrar o processamento dos arquivos.

- São ignorados os arquivos que já tenham sido processados anteriormente (ou seja, que tenham o mesmo nome).


#### 4 - Implementação da função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função recebe como parâmetro a fila que implementada no requisito 1.

- Caso não hajam arquivos na fila, a função deve apenas emite a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, é emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`.


#### 5 - Implementação da função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.

- Baseado na posição informada, é apresentado as informações relacionadas ao arquivo, parecido com o apresentado abaixo. Ou seja, essa é um exemplo de mensagem com sucesso:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```

- Em caso da posição não existir, é exibida a mensagem de erro `Posição inválida` via `stderr`.

- A função recebe como parâmetro a fila que implementamos no requisito 1 e o índice a ser buscado.



### Pacote `ting_word_searches`

#### 6 - Implementação da função `exists_word` dentro do módulo `word_search`, que valide a existência da palavra em todos os arquivos processados. Para cada palavra encontrada, é listado sua linha conforme segue abaixo.

- A busca deve ser _case insensitive_ e deve retornar uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1
    },
    {
      "linha": 2
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, retorna-se uma lista vazia.

- A fila é modificada durante a busca. Ela permanece com os mesmos arquivos processados antes e depois da busca!


#### 7 - Implementação da função `search_by_word` dentro do módulo `word_search`, que busque a palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha, o conteúdo e o arquivo da ocorrência.

- A busca é ser _case insensitive_ e retorna uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 2,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, retorna-se uma lista vazia.

- A fila é modificada durante a busca. Ela permanecer com os mesmos arquivos processados antes e depois da busca!

