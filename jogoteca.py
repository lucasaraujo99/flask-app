from flask import Flask, render_template, request, redirect, session, flash, url_for

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

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Lucas Araujo", "Lara", "12345")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

usuarios = { usuario1.nickname :usuario1, 
                usuario2.nickname :usuario2,
                usuario3.nickname :usuario3 }

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        # return redirect('/login?proxima=novo') # ?proxima=novo é usado para guardar e redirecionar o usuário para a pg que ele queria inicialmente
        return redirect(url_for('login', proxima=url_for('novo'))) 
    return render_template('novo.html', titulo= 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome'] # "nome" é o valor no "name" no input do form
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    # return redirect('/')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima') # captura a página a ser mostrada (definida em ?proxima=novo) depois do login ser efetuado
    return render_template('login.html', proxima=proxima) # passamos proxima para a página, onde ela será capturada pelo forms (de forma escondida)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios [request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso ')
            proxima_pagina = request.form['proxima']
            # return redirect('/{}'.format(proxima_pagina)) # redireciona para a página que o user queria inicialmente
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        # return redirect('/login')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    # return redirect('/')
    return redirect(url_for('index'))

# rodar a aplicacao
app.run(debug=True)
# app.run(host='0.0.0.0', port=8080) # é possível alterar o endereço e a porta

