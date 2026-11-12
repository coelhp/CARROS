# Templates

Agora entramos nos **templates**, que são a parte responsável por apresentar os dados ao usuário em páginas HTML.

Até aqui, o fluxo estava assim:

```text
URL → View → Resposta
```
Com templates, a view deixa de montar uma resposta simples e passa a renderizar uma página HTML:

```text
URL → View → Template HTML → Navegador
```

## O que são templates?
Templates são arquivos HTML que usam a **linguagem de templates do Django** para receber dados e apresentar informações dinamicamente.

Por exemplo, uma página pode exibir:

- lista de carros;
- dados de um produto;
- formulário;
- mensagens;
- informações do usuário;
- registros de entradas e saídas.

O template cuida principalmente da **apresentação**. A regra de negócio e a busca dos dados continuam na view.

## Exemplo simples
Uma view pode retornar um template usando `render`:

```python
from django.shortcuts import render


def home(request):
    return render(request, "home.html")
```

Nesse caso, o Django procura o arquivo `home.html` e devolve seu conteúdo ao navegador.

O arquivo poderia conter:

```html
<h1>Página inicial</h1>
<p>Bem-vindo ao sistema.</p>
```
A função `render` facilita três tarefas:

- Localiza o template;
- Processa a linguagem de templates do Django;
- Retorna uma resposta HTTP com o HTML.
- Enviando dados da view para o template

A view também pode enviar um dicionário de dados, chamado de contexto:

```python
from django.shortcuts import render


def home(request):
    context = {
        "name": "Patrick",
        "course": "Django Master",
    }

    return render(request, "home.html", context)
```

No template:

```html
<h1>Olá, {{ name }}!</h1>
<p>Você está estudando {{ course }}.</p>
```

A sintaxe:

```django
{{ name }}
```
serve para exibir o valor de uma variável enviada pela view.

O fluxo fica:

```text
View cria os dados
        ↓
View envia os dados no contexto
        ↓
Template acessa as variáveis
        ↓
HTML final é exibido no navegador
```

## Por que não colocar tudo na view?
Imagine uma view com dezenas de linhas de HTML:

```python
def home(request):
    html = """
    <html>
        <body>
            <h1>Página inicial</h1>
        </body>
    </html>
    """

    return HttpResponse(html)
```

Isso até pode funcionar, mas rapidamente se torna difícil de:

- ler;
- alterar;
- estilizar;
- reutilizar;
- manter em equipe.
  
Por isso, o Django separa as responsabilidades:

```text
View:
- processa a requisição;
- busca os dados;
- aplica a lógica.

Template:
- organiza o HTML;
- exibe os dados;
- define a apresentação.
```
Essa separação torna o projeto mais limpo e facilita resolver o problema do cliente sem misturar regra de negócio com estrutura visual.

## Onde organizar os templates?
Uma organização comum é criar uma pasta templates dentro da app:

```text
minha_app/
├── migrations/
├── templates/
│   └── minha_app/
│       ├── home.html
│       ├── list.html
│       └── detail.html
├── admin.py
├── apps.py
├── models.py
├── urls.py
└── views.py
```
O uso de uma subpasta com o nome da app ajuda a evitar conflitos.

Por exemplo, duas apps poderiam ter um arquivo chamado:

```text
templates/home.html
```
Se o projeto tiver várias apps, isso pode gerar confusão. Com a separação:

```text
templates/cars/home.html
templates/inventory/home.html
```
fica claro qual template pertence a cada app.

Na view, o caminho pode ser informado assim:

```python
return render(request, "minha_app/home.html")
```
Essa organização é especialmente importante em projetos maiores e evita depender de templates genéricos sem contexto.

## Exibindo listas
O Django permite percorrer listas usando `{% for %}`.

Na view:

```python
def cars(request):
    cars_list = [
        {"brand": "Fiat", "model": "Marea"},
        {"brand": "Volkswagen", "model": "Golf"},
    ]

    return render(
        request,
        "cars/list.html",
        {"cars": cars_list}
    )
```
No template:

```html
<h1>Carros</h1>

<ul>
    {% for car in cars %}
        <li>{{ car.brand }} {{ car.model }}</li>
    {% endfor %}
</ul>
```
A estrutura:

```django
{% for car in cars %}
{% endfor %}
```

é usada para executar uma repetição no template.

## Condições no template
Também podemos usar condições:

```html
{% if cars %}
    <p>Existem carros cadastrados.</p>
{% else %}
    <p>Nenhum carro foi cadastrado.</p>
{% endif %}
```

A sintaxe:

```django
{% if condição %}
{% else %}
{% endif %}
```
é utilizada para controlar o que será exibido.

Uma recomendação importante: o template deve cuidar de decisões simples de apresentação. Regras complexas devem ficar na view, no model ou em outra camada apropriada.

## Templates base e herança
Quando várias páginas possuem a mesma estrutura, não é necessário repetir o HTML inteiro.

Podemos criar um template base:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Sistema{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Sistema</h1>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

Depois, outra página pode reutilizar essa estrutura:

```html
{% extends "base.html" %}

{% block title %}
    Lista de carros
{% endblock %}

{% block content %}
    <h2>Carros cadastrados</h2>
{% endblock %}
```
Com isso:

- `{% extends %}` reutiliza o template base;
- `{% block %}` define partes que podem ser substituídas;
- o layout comum fica centralizado.

Essa abordagem evita duplicação e facilita alterações futuras. Se o cabeçalho mudar, por exemplo, você altera um local em vez de várias páginas.

## Templates e URLs
As páginas também podem criar links usando o nome das rotas:

```html
<a href="{% url 'cars' %}">
    Ver carros
</a>
```
Essa é uma boa prática porque o template não precisa depender diretamente do caminho escrito manualmente.

Se a URL mudar de:

```text
/carros/
```
para:

```text
/veiculos/
```
o link continuará funcionando, desde que o nome da rota permaneça o mesmo.

## Cuidados importantes
Ao trabalhar com templates:

- mantenha a lógica de negócio fora do HTML;
- organize os arquivos por app;
- evite nomes genéricos que possam gerar conflitos;
- use templates base para estruturas repetidas;
- envie dados pela view usando contexto;
- utilize nomes nas URLs;
- mantenha o HTML responsável pela apresentação.
  
A aula sobre organização e retorno de templates marca justamente o momento em que o resultado do projeto começa a ficar visível no navegador. A view deixa de retornar apenas um texto e passa a entregar uma página estruturada para resolver uma necessidade real do usuário.

## Resumo
Templates são arquivos HTML processados pelo Django. Eles:

- apresentam dados;
- recebem informações das views;
- utilizam variáveis, loops e condições;
- podem herdar estruturas de outros templates;
- ajudam a separar lógica e apresentação;
- tornam o projeto mais organizado e fácil de manter.

O fluxo completo fica:

```text
Usuário acessa uma URL
        ↓
A URL chama a view
        ↓
A view busca ou prepara os dados
        ↓
A view envia um contexto para o template
        ↓
O template gera o HTML
        ↓
O navegador exibe a página
```

O próximo passo recomendado é praticar uma página que liste registros vindos de um model, porque aí você conecta URL, view, model, banco de dados e template em um único fluxo. Aqui começa a aparecer o sistema de verdade, sem colocar motor, suspensão e painel do Fiat Marea 1999 no mesmo arquivo. 😄
