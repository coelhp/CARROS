# Makemigrations

## O comando makemigrations é responsável por transformar as alterações feitas nos seus models em arquivos de migração.

Pense nesta pergunta:

Se eu crio uma classe no models.py, a tabela aparece automaticamente no banco de dados?

Não. O Django precisa primeiro registrar o que mudou e depois aplicar essa mudança. É exatamente aí que entra o makemigrations.

O comando
No terminal, dentro da pasta que contém o manage.py, executamos:

```bash
python manage.py makemigrations
```

O que ele faz?
De acordo com a aula, o Django:

* Varre o projeto;
* Analisa as apps instaladas;
* Verifica os models;
* Compara o estado atual dos models com as migrações existentes;
* Cria novos arquivos dentro da pasta migrations quando identifica alterações.

As migrations são arquivos Python que descrevem operações para o banco de dados, como:

* criar uma tabela;
* adicionar uma coluna;
* alterar um campo;
* remover uma tabela;
* criar ou remover relacionamentos.

Por exemplo, suponha este model:

```python
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
```

Depois de executar:

```bash
python manage.py makemigrations
```

O Django poderá criar um arquivo semelhante a:


```text
cars/
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

Esse arquivo contém instruções que representam a criação da tabela correspondente ao model Car.

O que o makemigrations não faz?
O makemigrations não altera diretamente o banco de dados.

Ele apenas cria o arquivo que descreve a alteração.

O fluxo completo possui duas etapas:

```text
models.py
   ↓
python manage.py makemigrations
   ↓
arquivo de migration criado
   ↓
python manage.py migrate
   ↓
alteração aplicada no banco de dados
```

Portanto:

- makemigrations: cria o plano da alteração;
- migrate: executa esse plano no banco.

Uma analogia: o makemigrations é como o mecânico preparar uma ordem de serviço para modificar o Fiat Marea 1999. A ordem descreve o que precisa ser feito, mas o carro só muda quando o serviço é executado. Aqui é vida real.

Quando usar?
Você deve executar o makemigrations depois de criar ou alterar um model.

Exemplo:

python
```
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
```

Depois:

```bash
python manage.py makemigrations
```

E, para aplicar no banco:

```bash
python manage.py migrate
```

Onde o arquivo é criado?
O arquivo de migration é criado dentro da pasta migrations da app correspondente:

```text
cars/
├── models.py
└── migrations/
    ├── __init__.py
    └── 0001_initial.py
```

Se você fizer uma nova alteração posteriormente, o Django criará outro arquivo:

```text
migrations/
├── __init__.py
├── 0001_initial.py
└── 0002_car_year.py
```

Esses arquivos formam um histórico das mudanças realizadas na estrutura do banco.

Resumo
|Comando	|Função|
|----|----|
|python manage.py makemigrations|	Cria arquivos de migração com base nas alterações dos models|
|python manage.py migrate	|Aplica as migrações no banco de dados|

A sequência mais importante para memorizar é:

```bash
python manage.py makemigrations
python manage.py migrate
```

O primeiro comando prepara a alteração. O segundo comando executa a alteração.

No próximo passo, vale estudar o comando migrate, porque os dois trabalham juntos e serão usados constantemente durante o desenvolvimento de projetos Django.
