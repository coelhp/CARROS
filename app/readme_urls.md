# URLs

URLs são as rotas do sistema. Elas definem o que deve acontecer quando o usuário acessa determinado endereço no navegador.

Pense no site como uma cidade:

a URL é o endereço;
a view é o local que recebe o usuário;
a resposta é a página ou informação entregue.
Por exemplo:

```text
http://localhost:8000/estoque/
```
Essa URL pode direcionar o usuário para uma página de estoque. Já:

```text
http://localhost:8000/entradas/
```

pode mostrar os registros de entradas.

Como explicado na aula “Entendendo URLs e Views”, cada rota pode apresentar uma página diferente ou produzir um resultado diferente para o usuário.

Onde ficam as URLs?
O Django normalmente possui um arquivo urls.py principal dentro da pasta do projeto:

```text
projeto/
├── manage.py
└── projeto/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Esse arquivo é o ponto central das rotas do projeto. É o coração que recebe as URLs e encaminha cada uma para o local correto.

Um exemplo:

```python
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
]
```
Nesse caso:

/admin/ direciona para o painel administrativo;
/ direciona para a função home, dentro de core/views.py.
Ligação entre URL e view
Uma URL normalmente aponta para uma view:

python

Copiar
path("sobre/", views.about)
Essa linha pode ser interpretada assim:

Quando o usuário acessar /sobre/, execute a view about.

A view poderia ser:

python

Copiar
from django.http import HttpResponse


def about(request):
    return HttpResponse("Página sobre o sistema")
Então o fluxo é:

text

Copiar
Usuário acessa /sobre/
        ↓
Django procura essa rota em urls.py
        ↓
Django encontra views.about
        ↓
A função about é executada
        ↓
Uma resposta é devolvida ao usuário
É importante perceber que o urls.py não costuma conter a regra completa da página. Ele apenas faz o encaminhamento. A lógica fica na view.

URLs do projeto e URLs da app
Em projetos maiores, não é recomendado colocar todas as rotas diretamente no urls.py principal. Cada app pode ter seu próprio arquivo urls.py.

Por exemplo:

text

Copiar
projeto/
├── projeto/
│   └── urls.py
└── inventory/
    ├── urls.py
    └── views.py
URLs da app
Dentro da app inventory, você pode criar:

python

Copiar
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="inventory_home"),
    path("entradas/", views.inflows, name="inflows"),
    path("saidas/", views.outflows, name="outflows"),
]
Aqui a app define suas próprias rotas:

página inicial do estoque;
entradas;
saídas.
Incluindo as URLs da app no projeto
Depois, o urls.py principal conecta as rotas da app:

python

Copiar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("estoque/", include("inventory.urls")),
]
Agora o resultado final fica:

text

Copiar
/estoque/
/estoque/entradas/
/estoque/saidas/
Observe o papel de cada arquivo:

o urls.py do projeto define o prefixo /estoque/;
o urls.py da app define o restante da rota.
A aula sobre registro de saídas mostra justamente essa organização: depois de criar as URLs de Outflows, é necessário adicioná-las ao app ou às rotas principais do projeto para que elas realmente possam ser acessadas.

Por que usar include()?
O include() permite delegar parte das rotas para uma app específica:

python

Copiar
path("estoque/", include("inventory.urls"))
Isso deixa o projeto organizado. O arquivo principal não precisa conhecer todos os detalhes internos da app.

Uma analogia: o urls.py principal é como a recepção de uma empresa. Ele identifica que o visitante deseja falar com o setor de estoque e encaminha para esse setor. A recepção não precisa executar o trabalho do estoque — apenas direcionar corretamente. Bem melhor do que colocar todas as peças do Fiat Marea 1999 no mesmo lugar e depois tentar descobrir o que é motor, suspensão e ar-condicionado. Aqui é vida real.

O parâmetro name
É uma boa prática nomear as rotas:

python

Copiar
path("entradas/", views.inflows, name="inflows")
O nome permite referenciar a URL sem escrever o caminho manualmente em outros locais do projeto.

Por exemplo, em um template:

html

Copiar
<a href="{% url 'inflows' %}">Ver entradas</a>
Se futuramente você alterar o caminho de entradas/ para outro endereço, poderá manter as referências baseadas no nome, reduzindo a necessidade de modificar vários arquivos.

Atenção à barra final
Estas duas rotas são diferentes:

python

Copiar
path("entradas/", views.inflows)
path("entradas", views.inflows)
A primeira espera:

text

Copiar
/entradas/
A segunda espera:

text

Copiar
/entradas
No Django, é comum utilizar a barra final nas rotas:

python

Copiar
path("entradas/", views.inflows)
O mais importante é manter um padrão no projeto.

Resumindo
As URLs:

representam as rotas do sistema;
definem os endereços acessados pelo usuário;
encaminham requisições para views;
podem ficar no projeto ou em uma app;
podem ser conectadas usando include();
devem receber nomes com name;
organizam a navegação do sistema.
O fluxo principal é:

text

Copiar
Usuário acessa uma URL
        ↓
urls.py identifica a rota
        ↓
A rota chama uma view
        ↓
A view processa a requisição
        ↓
O Django devolve uma resposta
O próximo passo é entender com mais profundidade as views, porque URLs e views trabalham juntas: a URL encaminha e a view decide o que será feito. E pode ficar tranquilo: até aqui o Django está sendo bem mais organizado do que um projeto sem padrão — no máximo, essa explicação foi mediana, respeitando a regra dos alunos. 😄
