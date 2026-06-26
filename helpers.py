import os
from jogoteca import app

def retorna_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']): # percorre lista de nomes de arquivos no diretório de uploads
        # if f'capa{id}.jpg' == nome_arquivo:
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
        
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = retorna_imagem(id)

    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo)) # remove o "arquivo" no diretório "upload"