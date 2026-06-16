from flask import Flask, render_template

# variavel que armezena a aplicacao
app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

@app.route('/inicio')
def ola():
    jogo1 = Jogo("Dark Souls", "RPG", "PS3")
    jogo2 = Jogo("Super Mario", "Plataforma", "Super Nintendo")
    lista =[jogo1, jogo2]
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)

# rodar a aplicacao
app.run()
# app.run(host='0.0.0.0', port=8080) # é possível alterar o endereço e a porta

