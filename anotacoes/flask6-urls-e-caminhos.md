# URLs e Caminhos

## Definir caminho

É possível definir rotas posteriores, que serão acessadas após um direcionamento

```
@app.route('/novo')
def novo():
    if session['usuario_logado'] == None: # Verifica se usuário esta logado
        return redirect('/login?proxima=novo') # Se não estiver logador, redireciona para rota de login e coloca "novo" no caminho
    return render_template('novo.html', titulo='Novo Jogo')
```

Para recuperar o caminho da url é preciso usar **request.args.get()** e para passar a informação, usamos uma variável no parâmetro de **render_template()**

```
@app.route('/login')
def login():
    proxima = request.args.get('proxima') # pegando o caminho
    return render_template('login.html', proxima=proxima) # passando o caminho adiante
```

No template, é preciso de um **input** que guarda o valor da variável, mas que fica escondido

```
<input type="hidden" name="proxima" value="{{ proxima }}">
```

Na rota que irá direcionar ao destino final, basta recuperar a informação do forms com **request.form[]**

```
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    ...
    proxima_pagina = request.form['proxima']
    return redirect('/{}'.format(proxima_pagina))
    ...
```

## URLs Dinâmicas

Com **url_for()** é possível passar o nome da função que instancia a rota, permitindo mudar o nome das rotas, sem quebrar a lógica da aplicação

```
return redirect(url_for('index'))
```

O mesmo é possível nos templates

```
<form method="POST" action="{{ url_for('autenticar') }}">
```

**Importante:** é preciso importar url_for()

```
from flask import url_for
```