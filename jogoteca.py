from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

# variavel que armezena a aplicacao
app = Flask(__name__)

# chave de criptografia
app.secret_key = "chave"

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'lucas',
        senha = 'senha',
        servidor = 'localhost',
        database = 'jogoteca'
    )

# banco de dados
db = SQLAlchemy(app)

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
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

    jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash("Jogo já existente")
        return redirect(url_for('index'))
    
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    # return redirect('/')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima') # captura a página a ser mostrada (definida em ?proxima=novo) depois do login ser efetuado
    return render_template('login.html', proxima=proxima) # passamos proxima para a página, onde ela será capturada pelo forms (de forma escondida)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
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

