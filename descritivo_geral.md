# Descritivo Geral: 
## Estrutura Inicial do Projeto Django

Quando você executa o comando startproject, o Django cria uma estrutura inicial pronta para começar o desenvolvimento. A ideia é que você não precise configurar tudo do zero — o framework já traz várias facilidades, como usuários, sessões, grupos e permissões.

Antes de olhar arquivo por arquivo, pense assim:

O projeto Django precisa de um arquivo para executar comandos, outro para configurações, outro para URLs e pontos de entrada para servidores web.

Uma estrutura inicial costuma ficar assim:

```
meu_projeto/
├── manage.py
└── meu_projeto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

### 1. manage.py
É o arquivo usado para executar comandos administrativos do Django.

Por exemplo:


```python
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py startapp filme
```

Ele funciona como uma “central de controle” do projeto.


runserver: inicia o servidor de desenvolvimento;
migrate: aplica as alterações no banco;
makemigrations: cria arquivos de migração a partir das alterações nos models;
startapp: cria uma nova aplicação dentro do projeto.
Na prática, você passará bastante tempo utilizando esse arquivo pelo terminal.

### 2. Pasta interna do projeto
A pasta interna, que normalmente possui o mesmo nome do projeto, contém as configurações principais do Django.

Por exemplo:


```
meu_projeto/
├── manage.py
└── meu_projeto/
```

A pasta externa é o diretório geral do projeto. A pasta interna é o pacote Python que contém a configuração do Django.

Essa separação pode parecer estranha no início, mas é normal em praticamente todo projeto Django.

### 3. __init__.py
Esse arquivo informa ao Python que aquela pasta pode ser tratada como um pacote Python.

Inicialmente, ele normalmente fica vazio.

Você não precisa fazer alterações nele no começo.

### 4. settings.py
Esse é um dos arquivos mais importantes do projeto. Ele concentra as configurações gerais do Django.

Entre outras coisas, ele define:

aplicações instaladas;
banco de dados;
arquivos estáticos;
templates;
idioma;
fuso horário;
middleware;
chave secreta;
configurações de segurança.
Um trecho importante é o INSTALLED_APPS:

python

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",]
```
Essas aplicações já vêm habilitadas por padrão e oferecem funcionalidades importantes, como:

administração;
usuários;
grupos;
permissões;
sessões;
mensagens;
arquivos estáticos.
Aqui entra um ponto importante do material do curso: o Django já traz muita coisa pronta. Porém, essas funcionalidades precisam armazenar dados no banco de dados.

Por isso, o Django já possui models e tabelas internas para recursos como:

usuários;
grupos;
permissões;
sessões;
controle de migrações.
### 5. urls.py
Esse arquivo define as URLs principais do projeto.

Inicialmente, ele costuma conter uma rota para o painel administrativo:

python

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
```


Quando o usuário acessa:


```python
http://127.0.0.1:8000/admin/
```
o Django consulta o urls.py para descobrir qual funcionalidade deve ser executada.

Conforme o projeto cresce, normalmente você conecta as URLs das aplicações nesse arquivo principal.

### 6. asgi.py
É um ponto de entrada para servidores compatíveis com ASGI.

Ele é utilizado principalmente em cenários que precisam lidar com recursos assíncronos, como:

WebSockets;
aplicações assíncronas;
servidores modernos compatíveis com ASGI.
No início do curso, você provavelmente não precisará alterar esse arquivo.

### 7. wsgi.py
É outro ponto de entrada do projeto, utilizado por servidores compatíveis com WSGI.

Ele é bastante comum em deploy de aplicações Django tradicionais.

Assim como o asgi.py, normalmente você não precisa modificá-lo durante a criação inicial do projeto. Ele fica preparado para que um servidor externo consiga executar sua aplicação.

E o banco de dados?
Depois da criação inicial, quando você executa:

bash

```bash
python manage.py migrate
```
o Django aplica as migrações que já vêm prontas.

Em um projeto inicial, utilizando SQLite, pode surgir o arquivo:


db.sqlite3
A estrutura pode ficar assim:

text

```
meu_projeto/
├── db.sqlite3
├── manage.py
└── meu_projeto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```
Esse banco já recebe tabelas necessárias para os recursos internos do Django, como usuários, grupos, permissões e sessões.

makemigrations e migrate
É importante separar os dois conceitos:

makemigrations
Cria os arquivos que descrevem alterações nos seus models:

bash

Copiar
python manage.py makemigrations
migrate
Aplica essas alterações no banco:

```
python manage.py migrate
```
Uma analogia: o makemigrations prepara o projeto de reforma da casa; o migrate realmente executa a reforma. Aqui é vida real: criar o plano não altera o banco sozinho.

Projeto e aplicação são coisas diferentes
Após criar o projeto, você normalmente cria uma aplicação:

```
python manage.py startapp filmes
```
A estrutura poderá ficar parecida com:

```
meu_projeto/
├── manage.py
├── db.sqlite3
├── meu_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── filmes/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```
A diferença principal é:

Projeto: configuração geral do sistema;
Aplicação: módulo responsável por uma funcionalidade específica.
Por exemplo, em um sistema de filmes, você poderia ter aplicações como:

filmes;
usuarios;
vendas;
relatorios.
Resumindo
Arquivo ou pasta	Responsabilidade
manage.py	Executar comandos do Django
settings.py	Configurações do projeto
urls.py	Rotas principais
asgi.py	Entrada para servidores ASGI
wsgi.py	Entrada para servidores WSGI
__init__.py	Identifica um pacote Python
db.sqlite3	Banco SQLite criado após as migrações
migrations/	Histórico das alterações do banco
models.py	Estrutura dos dados
views.py	Regras e respostas das requisições
admin.py	Configuração do painel administrativo
Essa é a estrutura base criada nas aulas iniciais do curso. Depois, as aplicações começam a organizar as funcionalidades reais do sistema.