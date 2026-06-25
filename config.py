import os

# chave de criptografia
SECRET_KEY = "chave"

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'lucas',
        senha = 'senha',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = \
    os.path.dirname(        # Retorna apenas o diretório pai. ex: ex: C:\Users\Lucas\Documents\GitHub\flask-app
        os.path.abspath(    # Transforma um caminho em caminho absoluto. ex: C:\Users\Lucas\Documents\GitHub\flask-app\config.py
            __file__        # variável especial do Python que contém o caminho do arquivo atual. ex: C:\Users\Lucas\Documents\GitHub\flask-app\config.py
    )) + '/uploads'         # diretório onde devem ser feitos os uploads