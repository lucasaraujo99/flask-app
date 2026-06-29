# Flask Wtforms

## Instalando

```
pip install flask-wtf
```

## Classes de Forms

Importando funções necessárias:

```
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
```

Criando classe relativa ao forms:

```
class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
```

**OBS:** validators permitem validar características específicas do campo, como o preenchimento e número de caracteres

## Aplicando nas Rotas e Templates

Dentro da rota, é preciso instanciar a classe criada e passá-la para render_template

```
@app.route('/novo')
def novo():
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form)
```

No template, os campos do wtforms tem um formato específico.

Formato original em hmtl:
```
<!-- Campos do formulário usando html puro -->
<label for="nome">Nome</label>
<input type="text" id="nome" name="nome" class="form-control">
```

Formato em wtforms:
```
{# Campos do formulário usando flask-wtf #}
{{ form.nome.label(class="form-label") }}
{{ form.nome(class="form-control") }}
```

A rota que recebe os dados dos campos também precisa intanciar a classe criada

```
@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioJogo(request.form) # instanciando o formulário

    if not form.validate_on_submit(): # Validando campos
        return redirect(url_for('novo'))

    # Recuperando dados dos campos do forms
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
```

**OBS:** validate_on_submit() permite validar as informações conforme o que foi definido na classes

## CSRF

Medida de segurança necessária para o wtforms funcionar

Importando o csrf:
```
from flask_wtf.csrf import CSRFProtect
```

Instanciando o csrf:
```
csrf = CSRFProtect(app)
```

Passando o csrf para o forms:
```
<fieldset>
    {{ form.csrf_token() }}
    <div class="form-group">
    {{ form.nome.label(class="form-label") }}
    {{ form.nome(class="form-control") }}
    </div>
...
```


