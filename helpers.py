import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.data_required(), validators.length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.data_required(), validators.length(min=1, max=40)])
    console = StringField('Console', [validators.data_required(), validators.length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

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