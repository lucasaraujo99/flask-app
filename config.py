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