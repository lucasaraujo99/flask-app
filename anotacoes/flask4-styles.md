# Styles

## Pasta Static

Por padrão, o arquivos css em Flask ficam dentro da pasta Static

## Referência para o estilo

No head do template é possível passar a referência para o estilo

```
<head>
    ...
    <link rel="stylesheet" href="../static/bootstrap.css">  
</head>
```

**OBS**: **url_for()** permite encontrar um arquivo pelo nome dentro de uma pasta
```
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.css') }}">
```

## Reutilizando partes de Templates

É possível reutilizar partes de um arquivo base como o head e modificar apenas o corpo do código

### Arquivo Base (reutilizado)

```
<!DOCTYPE html>
<html>
<head>
...
{% block conteudo %} {% endblock %}
...
</body>
</html>
```

### Corpo modificado

```
{% extends "template.html" %}
{% block conteudo %}
<div>
...
</div>
{% endblock %}
```