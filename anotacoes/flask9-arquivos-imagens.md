# Arquivos e Imagens

É possível salvar arquivos em um diretório local

## Salvar Imagem

No template, é preciso adicionar um input com **type="file"** e **accept** correspondente ao tipo de arquivo
```
<input type="file" name="arquivo" accept=".jpg">
```

Na rota:

```
arquivo = request.files['arquivo']
arquivo.save(f'{upload_path}/capa{novo_jogo.id}.jpg')
```

**OBS:** no forms, é preciso adicionar **enctype="multipart/form-data"**, para conseguir enviar textos e imagens

```
<form action="{{ url_for('criar') }}" method="post" enctype="multipart/form-data">
```

## Exibir imagem

No template, solicitamos a fonte (scr) através de uma rota e o nome do arquivo

```
<img class="img-fluid" src="{{ url_for('imagem', nome_arquivo='capa_padrao.jpg') }}">
```

Na rota:

```
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
```

**Importante:** é preciso importar **send_from_directory**

```
from flask import send_from_directory
```