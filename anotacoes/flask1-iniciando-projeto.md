# Iniciando o projeto em Flask

## Importar o flask 

No arquivo Python que criamos, importe o flask no topo do arquivo

```
from flask import Flask
```

## Variável do objeto instanciado

Crie uma variável que receberá um novo objeto sendo instanciado

```
app = Flask(__name__)
```

## Rodar sua aplicação

Adicione a linha de código ao final do arquivo, para rodar sua aplicação

```
app.run()
```

**OBS:** para facilitar o desenvolvimento, é possível usar a função de debbug

```
app.run(debbug = True)
```

## Definindo uma rota

Defina um caminho (rota) e logo abaixo a função

```
@app.route('/inicio')
def ola():
    return '<h1>Olá Mundo!</h1>'
```

**OBS:** a rota inicial costuma se chamar "index" e ser chamada apenas de '/'

```
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)
```

## ***render_template***

Para usar o helper do flask chamado render_template, primeiro importe o render_template

```
from flask import Flask, render_template
```

Crie uma pasta chamada **templates** e em seguida crie um arquivo HTML dentro dela, que irá conter a interface da aplicação

Agora utilize o render_template para mostrar a página criada.

```
@app.route('/inicio')
def ola():
    return render_template('lista.html');
```

## Executar aplicação

Execute seu arquivo Python e cheque o link fornecido no seu navegador

**OBS:** para acessar um rota específica, é preciso adicionar seu nome ao final do link