from flask import Flask

# variavel que armezena a aplicacao
app = Flask(__name__)

@app.route('/inicio')
def ola():
    return '<h1>Olá Mundo!</h1>'

# rodar a aplicacao
app.run()

