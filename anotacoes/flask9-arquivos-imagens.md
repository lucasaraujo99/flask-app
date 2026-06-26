# Arquivos e Imagens

É possível salvar arquivos em um diretório local

## Salvar Imagem

No template, é preciso adicionar um input com **type="file"** e **accept** correspondente ao tipo de arquivo
```
<input type="file" name="arquivo" accept=".jpg">
```

Na rota, fazemos e o request do arquivo e o salvamos com um nome correspondente a string em **file.save("nome_arquivo)**

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

### Exibição responsiva

Ao fazer upload de um arquivo, podemos querer visualizá-lo automaticamente, mesmo se te-lo salvado ainda. Isso ajuda o usuário a saber que o arquivo correto será enviado.

Para isso, usamos um pouco de javascript, presente na pasta **static/**


```
static/
├── app.js
├── jquery.js
└── ...
```

No template (html), é preciso fazer a importação dos scripts

```
<!-- importação dos scripts js -->
<script type="text/javascript" src="{{ url_for('static', filename='jquery.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='app.js') }}"></script>
```

## Encontrar nome da imagem

Pode ser necessário encontrar o nome da imagem através do seu id, supondo que existe uma convenção para isso.

```
def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'
```

**OBS:** os.listdir(caminho) lista os arquivos dentro do diretório indicado pelo caminho

## Deletar imagem

Também é possível deletar uma imagem através do seu path e seu nome

```
def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
```

**OBS:** os.path.join(path, arquivo) tem o mesmo efeito de f'{path}/{arquivo}, porém o primeiro é mais efetivo já que diferentes sistemas operacionais tem diferentes formatações de path