# Inputs

## Utilizando um Form

Com um form no template é possível fazer inputs

```
...
<form action="/criar" method="post">
        <fieldset>
          <div class="form-group">
            <label for="nome">Nome</label>
            <input type="text" id="nome" name="nome" class="form-control">
          </div>
...
```

**Importante:**
- action: direciona para a rota designada
- method: é preciso adicionar "post" como método

## Recuperando o valor na rota

Importar o método request

```
from flask import Flask, render_template, request
```

Usando o método request para recuperar o valor

```
nome = request.form['nome']
```

**Importante:** adicionar POST como um método da rota

```
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
...
```

## Redirecionando Rotas

A rota de criação deve ser intermediária, logo após seu uso, outra rota deve ser mostrada em seguida.
Para isso, usamos **redirect()**.

```
@app.route('/criar', methods=['POST',])
def criar():
  ...
  return redirect('/')
```