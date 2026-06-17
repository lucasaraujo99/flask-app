from flask import Flask, render_template, request, redirect, session, flash

# variavel que armezena a aplicacao
app = Flask(__name__)

# chave de criptografia
app.secret_key = "chave"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo("Dark Souls", "RPG", "PS3")
jogo2 = Jogo("Super Mario", "Plataforma", "Super Nintendo")
lista =[jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo= 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome'] # "nome" é o valor no "name" no input do form
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado']+' logado com sucesso.') # mostrar mensagem na tela
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')

app.run(debug=True)

# rodar a aplicacao
app.run(debug=True)
# app.run(host='0.0.0.0', port=8080) # é possível alterar o endereço e a porta

