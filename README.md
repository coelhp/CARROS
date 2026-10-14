# 🚗 Carros - Sistema de Gestão de Veículos

Aplicação web desenvolvida com **Python e Django** durante o curso Django Master, da [PycodeBR](https://pycodebr.com.br/), com o objetivo de implementar um sistema para gerenciamento e divulgação de veículos.

O projeto utiliza os recursos do framework Django para desenvolver uma aplicação web completa, contemplando operações CRUD, autenticação de usuários, relacionamento entre modelos, consultas ao banco de dados e organização da aplicação seguindo a arquitetura MVT (*Model-View-Template*).

Além dos conceitos fundamentais do desenvolvimento web com Django, o projeto explora funcionalidades como gerenciamento de inventário, geração de descrições de veículos com inteligência artificial e integração com PostgreSQL.

## 📋 Sumário:

* [Sobre o projeto](#-sobre-o-projeto)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias utilizadas](#-tecnologias-utilizadas)
* [Conceitos aplicados](#-conceitos-aplicados)
* [Pré-requisitos](#-pré-requisitos)
* [Instalação e configuração](#-instalação-e-configuração)
* [Executando o projeto](#-executando-o-projeto)
* [Estrutura do projeto](#-estrutura-do-projeto)
* [Banco de dados](#-banco-de-dados)
* [Variáveis de ambiente](#-variáveis-de-ambiente)
* [Possíveis melhorias](#-possíveis-melhorias)
* [Referências](#-referências)
* [Licença](#-licença)

## 🎯 Sobre o projeto:

O **Carros** é um sistema web voltado ao gerenciamento de veículos, desenvolvido como projeto prático de aprendizado do framework Django.

A aplicação permite organizar informações sobre marcas e automóveis, disponibilizar uma vitrine de veículos e implementar funcionalidades administrativas e operacionais por meio de uma interface web.

O desenvolvimento reúne conceitos de programação em Python, orientação a objetos, desenvolvimento web, persistência de dados, autenticação e integração com serviços externos.

O projeto também serve como aplicação prática para compreender o ciclo de desenvolvimento de um sistema web, desde a modelagem dos dados até a configuração do ambiente e a preparação para publicação em produção.

## ✨ Funcionalidades:

### 🚘 Gerenciamento de veículos:

* Cadastro de veículos.
* Consulta e listagem dos veículos cadastrados.
* Visualização dos detalhes de cada veículo.
* Edição das informações dos veículos.
* Exclusão de registros.
* Armazenamento e exibição de imagens.
* Filtragem e ordenação de resultados.

### 🏷️ Gerenciamento de marcas:

* Cadastro e manutenção de marcas.
* Associação entre veículos e suas respectivas marcas.
* Organização dos dados por meio de relacionamentos entre modelos.

### 🔐 Autenticação e controle de acesso:

* Registro de usuários.
* Login e logout.
* Gerenciamento de sessões.
* Restrição de acesso a funcionalidades conforme as regras de autenticação e autorização implementadas.

### 📦 Controle de inventário:

* Gerenciamento das informações relacionadas ao inventário de veículos.
* Atualização automática de informações por meio de Django Signals, conforme os eventos definidos na aplicação.

### 🤖 Integração com inteligência artificial:

* Integração com a API da OpenAI.
* Possibilidade de geração automática de descrições para os veículos.
* Utilização de informações dos automóveis para enriquecer sua apresentação na aplicação.

### 🛠️ Interface administrativa:

* Utilização do Django Admin para gerenciamento dos registros.
* Configuração dos modelos para facilitar as operações administrativas.
* Centralização do gerenciamento dos dados da aplicação.

> **Observação:** a disponibilidade de cada funcionalidade depende da versão do projeto e das implementações presentes no repositório.

## 💻 Tecnologias utilizadas:

| Tecnologia       | Finalidade                                                           |
| ---------------- | -------------------------------------------------------------------- |
| Python           | Linguagem de programação principal                                   |
| Django           | Framework para desenvolvimento web                                   |
| Django ORM       | Mapeamento objeto-relacional e consultas ao banco de dados           |
| HTML             | Estrutura das páginas                                                |
| CSS              | Estilização das interfaces                                           |
| Templates Django | Renderização dinâmica das páginas                                    |
| PostgreSQL       | Banco de dados relacional para o ambiente configurado com PostgreSQL |
| OpenAI API       | Integração com serviços de inteligência artificial                   |
| Git              | Controle de versão                                                   |
| GitHub           | Hospedagem do código-fonte                                           |

A lista representa as tecnologias associadas ao projeto. A disponibilidade e a configuração de cada dependência devem ser confirmadas nos arquivos do repositório.

## 🧠 Conceitos aplicados:

Durante o desenvolvimento, são explorados conceitos importantes para a construção de aplicações web com Django.

**Programação em Python:**

* Funções, estruturas de controle e coleções.
* Programação orientada a objetos.
* Organização e reutilização de código.

**Desenvolvimento web com Django**

* Arquitetura MVT (*Model-View-Template*).
* Rotas e resolução de URLs.
* Views baseadas em funções e classes.
* Renderização de templates.
* Formulários e validação de dados.
* Autenticação e autorização.

**Modelagem e persistência de dados**

* Criação de modelos.
* Relacionamentos entre entidades.
* Migrações de banco de dados.
* Consultas com Django ORM.
* Operações CRUD (*Create, Read, Update, Delete*).

**Recursos avançados**

* Class-Based Views (CBVs).
* Django Signals.
* Manipulação de arquivos e imagens.
* Integração com APIs externas.
* Configuração de banco de dados relacional.
* Preparação para implantação em ambiente de produção.

## ⚙️ Pré-requisitos:

Antes de executar o projeto, verifique se o ambiente possui:

* Python em uma versão compatível com a versão do Django utilizada.
* Git.
* pip, gerenciador de pacotes do Python.
* Um ambiente virtual Python.
* PostgreSQL, caso o projeto esteja configurado para utilizá-lo.
* Uma chave de API da OpenAI, caso a funcionalidade de inteligência artificial esteja habilitada.

**Importante:** consulte o arquivo `requirements.txt` e as configurações do projeto para identificar as versões efetivamente utilizadas.

## 🚀 Instalação e configuração

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório do projeto:

```bash
cd carros
```

Substitua `<URL_DO_REPOSITORIO>` pelo endereço real do repositório.

### 2. Crie um ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

Se o repositório possuir um arquivo `requirements.txt`, execute:

```bash
python -m pip install -r requirements.txt
```

Caso esse arquivo não exista, instale as dependências documentadas pelo projeto.

### 4. Configure as variáveis de ambiente

Configure as credenciais e os parâmetros necessários para a execução da aplicação.

Dependendo da implementação, podem ser necessários:

* Chave secreta do Django.
* Configurações do banco de dados.
* Chave de API da OpenAI.
* Configurações de depuração e ambiente.

Não armazene senhas, chaves de API ou outras credenciais diretamente no código-fonte ou no repositório público.

### 5. Configure o banco de dados

Se o projeto utilizar PostgreSQL, crie o banco de dados e configure as credenciais de conexão conforme as configurações da aplicação.

Verifique os parâmetros de conexão definidos no projeto antes de executar as migrações.

### 6. Execute as migrações

Com o ambiente configurado, execute:

```bash
python manage.py makemigrations
python manage.py migrate
```

O comando `makemigrations` gera migrações para alterações nos modelos que ainda não tenham sido registradas. O comando `migrate` aplica as migrações pendentes ao banco de dados.

Se o repositório já possuir todas as migrações necessárias, normalmente será suficiente executar `migrate`.

### 7. Crie um superusuário

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Siga as instruções exibidas no terminal para cadastrar as credenciais.

## ▶️ Executando o projeto

Após concluir a configuração, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

A aplicação estará disponível, por padrão, em:

`http://127.0.0.1:8000/`

Para acessar o painel administrativo, utilize:

`http://127.0.0.1:8000/admin/`

O endereço da página inicial e as rotas administrativas podem variar conforme a configuração das URLs do projeto.

Para interromper o servidor, pressione `Ctrl + C` no terminal.

> O servidor iniciado pelo comando `runserver` é destinado ao desenvolvimento. Para disponibilizar a aplicação publicamente, utilize uma configuração apropriada para produção.

## 📁 Estrutura do projeto

A estrutura abaixo é ilustrativa e deve ser ajustada para refletir os diretórios e arquivos efetivamente existentes no repositório.

```text
carros/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── <projeto_django>/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── <aplicacao_carros>/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── templates/
├── static/
└── media/
```

### Principais componentes

| Componente    | Responsabilidade                                              |
| ------------- | ------------------------------------------------------------- |
| `manage.py`   | Executa comandos administrativos do Django                    |
| `settings.py` | Centraliza as configurações do projeto                        |
| `urls.py`     | Define o roteamento das requisições                           |
| `models.py`   | Define os modelos e a estrutura dos dados                     |
| `views.py`    | Implementa a lógica de processamento das requisições          |
| `forms.py`    | Define formulários e validações, quando utilizados            |
| `admin.py`    | Configura a interface administrativa                          |
| `migrations/` | Armazena as migrações dos modelos                             |
| `templates/`  | Armazena os templates HTML                                    |
| `static/`     | Armazena arquivos estáticos, como CSS e JavaScript            |
| `media/`      | Armazena arquivos enviados pelos usuários, quando configurado |

Os nomes entre sinais de `<` e `>` são marcadores ilustrativos, não diretórios que necessariamente existam no repositório.

## 🗄️ Banco de dados

O projeto contempla o uso de banco de dados relacional para persistir as informações de marcas e veículos.

O Django ORM permite representar os registros por meio de modelos Python, estabelecer relacionamentos entre entidades e executar consultas sem exigir a escrita manual de SQL para as operações mais comuns.

No ambiente configurado com PostgreSQL, o banco de dados é responsável por armazenar os registros da aplicação.

As configurações de conexão devem ser definidas de acordo com o ambiente de execução, evitando a exposição de credenciais no código-fonte.

## 🔑 Variáveis de ambiente

Para facilitar a configuração e aumentar a segurança, recomenda-se manter os parâmetros sensíveis fora do código-fonte.

Exemplo ilustrativo de um arquivo `.env`:

```dotenv
DJANGO_SECRET_KEY=sua-chave-secreta
DJANGO_DEBUG=True

DB_NAME=carros
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

OPENAI_API_KEY=sua-chave-da-openai
```

Os nomes apresentados são exemplos. Eles só terão efeito se forem utilizados pela configuração da aplicação.

Caso o projeto não implemente a leitura de variáveis de ambiente, será necessário adaptar suas configurações antes de utilizar esse modelo.

**Boas práticas de segurança:**

* Não publique arquivos `.env` contendo credenciais reais.
* Inclua os arquivos de configuração locais no `.gitignore`.
* Utilize `DJANGO_DEBUG=False` em produção.
* Configure uma chave secreta exclusiva para cada ambiente.
* Restrinja o acesso às credenciais do banco de dados.
* Armazene a chave da OpenAI em uma variável de ambiente e evite registrá-la em logs.

## 🔧 Possíveis melhorias

Como evolução do projeto, algumas melhorias que podem ser consideradas são:

* Implementação de testes automatizados para modelos, views e formulários.
* Ampliação da cobertura de testes de autenticação e autorização.
* Validação e tratamento de erros nas integrações externas.
* Paginação e otimização das consultas ao banco de dados.
* Melhorias de acessibilidade e responsividade da interface.
* Configuração de integração contínua (CI).
* Documentação das rotas e regras de negócio.
* Uso de variáveis de ambiente em todos os ambientes.
* Preparação de uma configuração de produção com servidor de aplicação e servidor web.
* Monitoramento de erros e registro estruturado de eventos.

## 📚 Referências

* [PycodeBR - Django Master](https://pycodebr.com.br/djangomaster-org/)
* [Documentação oficial do Django](https://docs.djangoproject.com/)
* [Documentação oficial do Python](https://docs.python.org/3/)
* [Documentação oficial do PostgreSQL](https://www.postgresql.org/docs/)
* [Documentação da API da OpenAI](https://platform.openai.com/docs/)

## 📄 Licença

Este repositório foi desenvolvido no contexto de aprendizado do curso Django Master, da PycodeBR.

A licença de distribuição do código deve ser definida pelo responsável pelo repositório, respeitando os direitos autorais e os termos aplicáveis aos materiais utilizados no projeto.

---

Desenvolvido com Python e Django como parte da jornada de aprendizado em desenvolvimento web.
