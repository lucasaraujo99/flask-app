from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
import time

from jogoteca import app, db
from models import Jogos, Usuarios
from helpers import retorna_imagem, deleta_arquivo

# Arquivo de rotas

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

    arquivo = request.files['arquivo']
    #arquivo.save(f'uploads/{arquivo.filename}')

    timestamp=time.time()

    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestamp}.jpg')

    # return redirect('/')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    
    jogo = Jogos.query.filter_by(id=id).first()
    capa_jogo = retorna_imagem(id)
    return render_template('editar.html', titulo= 'Editar Jogo', jogo=jogo, capa_jogo=capa_jogo)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()

    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']

    deleta_arquivo(jogo.id)

    timestamp=time.time()
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    Jogos.query.filter_by(id=id).delete()

    db.session.commit()

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
            if(proxima_pagina=="None"):
                return redirect(url_for('index'))
            else:
                return redirect(proxima_pagina)
        else:
            flash('Senha incorreta.')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    # return redirect('/')
    return redirect(url_for('index'))

@app.route('/imagem/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)