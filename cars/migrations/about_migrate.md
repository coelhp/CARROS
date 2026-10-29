# Migrate
Se o makemigrations cria um “plano” com as alterações dos models, o migrate é o comando que executa esse plano no banco de dados.

Antes de continuar, pense:

Depois que o Django cria um arquivo dentro de migrations/, a tabela já foi criada no banco?

Ainda não. O arquivo de migration apenas contém instruções. Para que essas instruções sejam aplicadas, usamos o migrate.

O comando migrate
```bash
python manage.py migrate
```

Esse comando faz o Django:

* Verificar as migrations existentes;
* Identificar quais ainda não foram aplicadas;
* Interpretar as instruções desses arquivos;
* Traduzir essas instruções para o banco de dados;
* Criar ou alterar tabelas, colunas e relacionamentos;
* Registrar quais migrations já foram executadas.

Em outras palavras, o migrate transforma as definições do Django em alterações reais no banco.

Fluxo completo
O processo normalmente é:

```text
models.py
   ↓
python manage.py makemigrations
   ↓
Arquivo criado em migrations/
   ↓
python manage.py migrate
   ↓
Alteração aplicada no banco
```
Por exemplo, depois de criar um model:

```python
from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
```

Você executa:

```bash
python manage.py makemigrations
```
Esse comando cria uma migration, como:

```text
cars/migrations/0001_initial.py
```
Mas a tabela ainda não foi criada fisicamente no banco. Então executamos:

```bash
python manage.py migrate
```
Agora o Django lê o arquivo 0001_initial.py e cria a tabela correspondente ao model Car.

Migrations internas do Django
Uma parte importante mostrada na aula é que o Django já possui várias aplicações internas, como:

-   django.contrib.auth;
-   django.contrib.admin;
-   django.contrib.contenttypes;
-   django.contrib.sessions.

Essas aplicações também possuem migrations.

Por isso, quando você executa o primeiro:

```bash
python manage.py migrate
```
Mesmo sem ter criado nenhum model próprio, o Django já cria tabelas básicas para seu funcionamento, incluindo tabelas relacionadas a:

* usuários;
* grupos;
* permissões;
* sessões;
* administração;
* controle das próprias migrations.

É por isso que o Django consegue oferecer funcionalidades como login, permissões e painel administrativo desde o início.

Como saber o que foi aplicado?
Durante a execução, o Django mostra algo parecido com:

```text
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying sessions.0001_initial... OK
```
O OK indica que aquela migration foi aplicada com sucesso.

Depois disso, você pode criar um superusuário:

```bash
python manage.py createsuperuser
```
Isso só é possível corretamente depois que as tabelas necessárias do sistema de autenticação já foram criadas pelo migrate.

O migrate pode ser executado várias vezes?
Sim. É comum executar:

```bash
python manage.py migrate
```
várias vezes durante o desenvolvimento.

Se não houver migrations pendentes, o Django não repetirá alterações já aplicadas. Ele verifica o histórico e executa apenas o que ainda falta.

Por exemplo, se você executar novamente sem nenhuma alteração pendente, poderá receber uma mensagem semelhante a:

```text
No migrations to apply.
```
Isso significa que o banco já está atualizado em relação às migrations conhecidas pelo projeto.

Como o Django controla as migrations aplicadas?
O Django mantém uma tabela interna no banco chamada:

```text
django_migrations
```
Ela registra quais migrations já foram aplicadas.

Esse controle evita que o Django tente criar novamente uma tabela ou adicionar novamente uma coluna que já existe.

Uma analogia: o makemigrations prepara a ordem de serviço do Fiat Marea 1999; o migrate executa o serviço e ainda registra no histórico o que já foi feito. Assim, o mecânico não troca a mesma peça toda vez que o carro entra na oficina. Aqui é vida real.

Diferença entre os dois comandos
Comando	Responsabilidade
makemigrations	Cria arquivos com instruções baseadas nos models
migrate	Aplica essas instruções no banco de dados
A sequência recomendada é:

```bash
python manage.py makemigrations
python manage.py migrate
```
Resumo
O comando:

```bash
python manage.py migrate
```
é responsável por aplicar as migrations pendentes no banco de dados.

Ele:

* cria tabelas;
* altera estruturas;
* aplica migrations das suas apps;
* aplica migrations internas do Django;
* mantém o banco sincronizado com os models;
* registra o histórico das migrations executadas.

Portanto, o makemigrations descreve a mudança, enquanto o migrate realiza a mudança.

O próximo passo natural da trilha é acessar o admin, criar o superusuário e verificar que as tabelas de autenticação já foram preparadas pelo migrate.