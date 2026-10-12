# 🚗 Projeto Carros

Sistema web para gerenciamento e exposição de veículos, desenvolvido com **Python e Django** durante o curso Django Master, da PyCodeBR.

O projeto tem como objetivo aplicar conceitos de desenvolvimento web, programação orientada a objetos, banco de dados relacionais e autenticação de usuários, construindo uma aplicação para gerenciamento de uma revenda de automóveis.

## 📋 Funcionalidades

O projeto contempla funcionalidades voltadas à administração e à visualização de veículos.

* **Cadastro de veículos:** registro e gerenciamento das informações dos carros.
* **Gestão de marcas:** cadastro de marcas e relacionamento com os veículos.
* **Vitrine de veículos:** exibição dos carros cadastrados.
* **Pesquisa e filtros:** consulta de veículos com base em parâmetros informados pelo usuário.
* **Autenticação de usuários:** registro, login e gerenciamento de sessões.
* **Operações CRUD:** criação, consulta, atualização e exclusão de registros.
* **Upload de imagens:** armazenamento e exibição de fotos dos veículos.
* **Inventário:** acompanhamento das informações e da quantidade de veículos cadastrados.
* **Integração com inteligência artificial:** geração de descrições para os veículos por meio da API da OpenAI, conforme a configuração do projeto.

## 🛠️ Tecnologias utilizadas

* **Python** - linguagem de programação.
* **Django** - framework para desenvolvimento web.
* **HTML e CSS** - estruturação e estilização das páginas.
* **Django Templates** - renderização dinâmica de páginas HTML.
* **Django ORM** - interação com o banco de dados.
* **SQLite ou PostgreSQL** - persistência de dados, conforme o ambiente configurado.
* **Git e GitHub** - versionamento e hospedagem do código-fonte.
* **OpenAI API** - integração com inteligência artificial para geração de descrições, quando habilitada.

## 📁 Estrutura do projeto

A estrutura pode variar conforme a evolução da aplicação. Uma organização típica de um projeto Django desse tipo é:

```text
carros/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
├── templates/
├── static/
├── media/
└── carros/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

> **Observação:** a estrutura acima é ilustrativa. Os diretórios e arquivos devem corresponder à organização real do repositório.

## ⚙️ Pré-requisitos

Antes de executar o projeto, instale:

* Python 3;
* Git;
* pip;
* Um editor de código, como o Visual Studio Code.

Caso utilize PostgreSQL, também será necessário configurar o banco de dados e instalar o driver correspondente.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre no diretório do projeto:

```bash
cd carros
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço HTTPS ou SSH do seu repositório no GitHub.

### 2. Cri
