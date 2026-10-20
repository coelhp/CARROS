# Pense assim:

O projeto é o sistema inteiro e contém as configurações gerais.
A app é uma parte funcional do sistema, responsável por um determinado domínio.
No Projeto Carros, por exemplo, o projeto possui as configurações gerais, enquanto a app cars concentra funcionalidades relacionadas aos carros.

## Criando uma nova app
Dentro da pasta onde está o manage.py, você executa:

```bash
python manage.py startapp cars
```

O Django cria automaticamente uma estrutura inicial:

```bash
cars/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

Essa é uma app vazia, ou seja, ela ainda não possui as regras específicas do seu sistema. O Django apenas cria os arquivos básicos para você começar.

O passo mais importante: registrar a app
Depois de criar a app, ela ainda não está sendo utilizada pelo projeto. É necessário adicioná-la no INSTALLED_APPS, dentro do settings.py do projeto:

python

Copiar
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "cars",
]
Essa é exatamente a ideia apresentada nas aulas: criar a app não significa automaticamente que o projeto já está usando essa app.

Uma analogia: criar a app é como comprar uma peça nova para o Fiat Marea 1999. A peça existe, mas ainda precisa ser instalada no carro para funcionar. Aqui é vida real.

Estrutura da app
__init__.py
Indica que a pasta cars é um pacote Python.

Normalmente, permanece vazio e você não precisa alterá-lo inicialmente.

admin.py
É usado para registrar os models no painel administrativo do Django.

Por exemplo, depois de criar um model Car em models.py, você poderá registrá-lo:

python

Copiar
from django.contrib import admin
from .models import Car

admin.site.register(Car)
A partir daí, o model poderá aparecer no /admin/, desde que você também tenha um superusuário.

apps.py
Contém a configuração da app.

Normalmente, o Django cria algo parecido com:

python

Copiar
from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cars"
O atributo name informa o caminho da app.

Em alguns casos, a app pode ser adicionada no settings.py usando a classe de configuração:

python

Copiar
"cars.apps.CarsConfig",
migrations/
Essa pasta armazena o histórico das alterações feitas nos models.

Inicialmente, ela contém apenas:

text

Copiar
migrations/
└── __init__.py
Depois que você cria ou altera um model e executa:

bash

Copiar
python manage.py makemigrations
o Django cria arquivos de migration dentro dessa pasta.

Depois, você aplica as alterações ao banco com:

bash

Copiar
python manage.py migrate
O fluxo normalmente é:

text

Copiar
Alterar models.py
        ↓
python manage.py makemigrations
        ↓
python manage.py migrate
        ↓
Alteração aplicada no banco
models.py
É onde você define a estrutura dos dados da app.

Por exemplo:

python

Copiar
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
Esse model representa uma tabela de carros no banco de dados.

Depois de criá-lo, você precisa gerar e aplicar as migrations:

bash

Copiar
python manage.py makemigrations
python manage.py migrate
tests.py
É o arquivo destinado aos testes automatizados da app.

Você pode testar, por exemplo:

criação de registros;
regras de negócio;
respostas das views;
comportamento de formulários;
permissões de usuários.
No começo, ele geralmente vem vazio ou com uma estrutura básica.

views.py
É onde ficam as views, que recebem requisições e retornam respostas.

Um exemplo simples:

python

Copiar
from django.http import HttpResponse


def home(request):
    return HttpResponse("Página inicial de carros")
Mas criar a view não basta. Você também precisa criar uma rota para ela ser acessada.

Geralmente, criamos um urls.py dentro da app:

text

Copiar
cars/
├── urls.py
├── views.py
└── ...
E depois conectamos essas URLs no urls.py principal do projeto.

Projeto x app
A diferença principal pode ser resumida assim:

Projeto	App
Representa o sistema completo	Representa uma funcionalidade ou domínio
Possui settings.py	Possui models.py, views.py etc.
Possui as configurações gerais	Implementa regras específicas
Possui o urls.py principal	Pode possuir seu próprio urls.py
Coordena as apps	Trabalha em uma parte do sistema
Por exemplo, em um sistema de carros:

text

Copiar
projeto/
├── manage.py
├── app/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── cars/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
└── db.sqlite3
Nesse exemplo:

app é o coração e a configuração geral do projeto;
cars é uma app funcional;
settings.py precisa conhecer cars por meio do INSTALLED_APPS;
cars/models.py define os dados relacionados aos carros;
cars/views.py define o comportamento das páginas ou endpoints;
cars/admin.py configura a administração desses dados.
Um detalhe importante
Uma app não precisa representar necessariamente uma única tabela. Ela deve representar uma área de responsabilidade do sistema.

Por exemplo:

text

Copiar
cars/
brands/
dealers/
users/
Cada app pode cuidar de um domínio diferente. Essa organização ajuda a evitar que todo o código fique misturado em uma única pasta.

Portanto, o fluxo inicial é:

Criar a app:

bash

Copiar
python manage.py startapp cars
Adicioná-la ao INSTALLED_APPS.

Criar os models, views e demais funcionalidades.

Criar migrations quando houver alterações nos models.

Conectar as URLs da app ao projeto.

A ideia apresentada nas aulas é justamente essa: o Django cria a estrutura padrão da app, mas é você quem vai transformar essa app vazia em uma parte funcional do sistema.
