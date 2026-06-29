from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# variavel que armezena a aplicacao
app = Flask(__name__)

app.config.from_pyfile('config.py')

# banco de dados
db = SQLAlchemy(app)

csrf = CSRFProtect(app)

from views import *

if __name__ == '__main__':
    # rodar a aplicacao
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080) # é possível alterar o endereço e a porta

