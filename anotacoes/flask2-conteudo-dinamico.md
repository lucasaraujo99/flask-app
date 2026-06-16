# Conteúdo Dinâmico

## Variáveis no Template

É possível passar variáveis para render_template e usá-las no template

### Passar a Variável

```
valor_da_variavel = 10
render_template('lista.html', variavel=valor_da_variavel)
```

### Usar a variável no template

Delimitadores {{ }}: para chamar a variável no template

```
<h1>{{ titulo }}</h1>
```

Também é possível aplicar operações sobre as variáveis

```
<h1>{{  titulo.upper()  }}</h1>
```

## Código no Template

Delimitadores {% %}: para chamar código no template

```
<tbody>
{% for item in lista %}    
    <tr>
        <td>{{ item }}</td>
    </tr>
{% endfor %}
</tbody>
```

```
{% if lista %}
  <p>Temos {{ len(lista) }} apostilas no nosso site. </p>
{% else %}
  <p>Nenhuma apostila aqui... </p>
{% endif %}
```

## Comentários no Template

Delimitadores {# #}: para colocar comentário no template que não serão exibidos