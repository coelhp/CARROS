# Views

## Pense nesta pergunta:

A URL `/carros/` apenas identifica o endereço. Mas quem decide o que será buscado no banco e o que será devolvido ao usuário?

A responsável por isso é a view.

## O que é uma view?
No Django, a view é a camada que contém a lógica da aplicação. Ela faz o meio de campo entre:

- a requisição do usuário;
- as URLs;
- os models e o banco de dados;
- os templates ou respostas JSON;
- as regras da aplicação.

Apesar do nome, view não significa simplesmente a parte visual da aplicação. No contexto do Django, ela se aproxima do papel de um controller no padrão MVC.

O fluxo é:

```text
Usuário acessa uma URL
        ↓
A URL encontra uma view
        ↓
A view executa a lógica
        ↓
Consulta ou altera dados
        ↓
Retorna uma resposta
```

## Exemplo prático
Imagine que o usuário acesse:

```text
/carros/
```
A URL encaminha a requisição para uma view:

```python
from django.http import HttpResponse


def cars(request):
    return HttpResponse("Lista de carros")
```
Essa é uma function-based view, ou seja, uma view criada como função.

A URL poderia estar ligada a ela assim:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("carros/", views.cars, name="cars"),
]
```
Quando o usuário acessa `/carros/`, o Django executa a função cars.

## View consultando o banco de dados
Na prática, a view geralmente consulta um model:

```python
from django.shortcuts import render
from .models import Car


def cars(request):
    cars_list = Car.objects.all()

    return render(
        request,
        "cars.html",
        {"cars": cars_list}
    )
```

Nesse exemplo, a view:

- Recebe a requisição por meio do parâmetro request;
- Busca todos os carros usando o model Car;
- Envia os dados para o template cars.html;
- Retorna uma página HTML para o usuário.

O template fica responsável pela apresentação, enquanto a view fica responsável pela lógica de buscar os dados.

## A view não é o template
Essa separação é importante:

```text
View:
- busca os carros;
- aplica regras;
- decide o que fazer;
- envia os dados.

Template:
- exibe os carros;
- organiza HTML;
- apresenta o resultado ao usuário.
```

Por exemplo, o template poderia exibir os dados assim:

```html
{% for car in cars %}
    <p>{{ car.brand }} {{ car.model }}</p>
{% endfor %}
```
A view não precisa construir manualmente todo o HTML. Ela prepara os dados e os envia para o template.

View também pode alterar dados
Uma view não serve apenas para listar registros. Ela também pode:

cadastrar um objeto;
editar um objeto;
excluir um objeto;
validar informações;
processar formulários;
consultar registros;
retornar mensagens;
controlar permissões de acesso.


Por exemplo, uma view pode criar um carro depois de receber dados de um formulário:

python

Copiar
def create_car(request):
    if request.method == "POST":
        # obter dados enviados
        # validar informações
        # salvar o carro
        pass
A lógica completa dependerá do formulário e do model, mas o princípio é esse: a view recebe a requisição e decide o que deve acontecer.

Views baseadas em função
As function-based views, ou FBVs, são funções comuns do Python:

python

Copiar
def home(request):
    return HttpResponse("Página inicial")
Elas são boas para começar porque deixam o fluxo bastante explícito:

recebe a requisição;
executa comandos;
retorna uma resposta.
Views baseadas em classe
O Django também oferece as class-based views, ou CBVs.

Nesse caso, utilizamos classes já preparadas pelo Django para tarefas comuns. Existem views para:

listar vários objetos;
detalhar um objeto;
criar um objeto;
atualizar um objeto;
excluir um objeto.
Um exemplo conceitual de uma view para listar objetos:

python

Copiar
from django.views.generic import ListView
from .models import Car


class CarListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"
Essa classe aproveita recursos que o Django já fornece. Em vez de escrever toda a lógica de listagem manualmente, você configura a classe de acordo com sua necessidade.

A ideia apresentada no curso é que o Django já possui uma hierarquia de views prontas, cada uma voltada para um tipo de operação. Por exemplo:

uma view para listar vários objetos;
uma view para detalhar um objeto;
uma view para criar um novo objeto.
Views em APIs
Em uma aplicação tradicional, a view geralmente retorna um template HTML:

text

Copiar
View → Template HTML → Navegador
Em uma API, a view normalmente retorna dados em JSON:

text

Copiar
View → JSON → Cliente da API
Por exemplo:

json

Copiar
{
  "id": 1,
  "brand": "Fiat",
  "model": "Marea"
}
A lógica central continua parecida: a view recebe a requisição, acessa os dados e retorna uma resposta. O que muda principalmente é o formato do retorno.

Resumo
As views são responsáveis por:

receber requisições;
executar a lógica da aplicação;
consultar ou alterar dados;
conversar com os models;
enviar dados para templates;
retornar HTML ou JSON;
controlar o fluxo de cada funcionalidade.
A relação entre os principais componentes fica assim:

text

Copiar
URL
  ↓
View
  ↓
Model / Banco de dados
  ↓
Template HTML ou resposta JSON
Uma analogia: a URL é o endereço da oficina, a view é o mecânico que entende o problema, consulta as peças e decide o serviço, o model representa as peças e o banco é o estoque. O template é a forma organizada de apresentar o resultado ao cliente. Se misturar tudo no mesmo lugar, vira manutenção de Fiat Marea 1999 sem manual — aqui é vida real. 😄

O próximo passo recomendado é estudar uma view simples que lista objetos do banco e depois observar como a mesma funcionalidade pode ser escrita com uma class-based view.
