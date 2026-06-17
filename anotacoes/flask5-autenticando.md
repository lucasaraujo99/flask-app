# Session e Autenticação

## Session

Ferramenta do Flask que permite armazena informações em Cookies do navegador

```
from flask import session
```

## Guardando informação

É possível pegar o valor de um forms e guardá-lo na session

```
session['usuario_logado'] = request.form['usuario']
```

**Importante:** é preciso adicionar um **secret_key** para criptografar as informações armazenadas

```
app = Flask(__name__)

app.secret_key = "chave"
```

**OBS:** também é possível excluir uma informação

```
session['usuario_logado'] = None
```

## Flash: exibindo informações

Com **flash()** é possível exibir mensagens para o usuário

```
flash('Login efetuado com sucesso')
```

**Importante:** para isso, é preciso adicionar onde o flash aparece no template

```
{% with messages = get_flashed_messages() %}
    {% if messages %} 
        <ul id="messages" class="list-unstyled">
        {% for message in messages %}
            <li class="alert alert-success">{{ message }}</li>
        {% endfor %}
        </ul>
    {% endif %}
{% endwith %}
```
