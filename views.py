from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
import time

from jogoteca import app, db
from models import Jogos, Usuarios
from helpers import retorna_imagem, deleta_arquivo, FormularioJogo, FormularioUsuario

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
    form = FormularioJogo()
    return render_template('novo.html', titulo= 'Novo Jogo', form = form)

@app.route('/criar', methods=['POST',])
def criar():

    # Recuperando a partir dos campos de formulário com Flask puro
    # nome = request.form['nome'] # "nome" é o valor no "name" no input do form
    # categoria = request.form['categoria']
    # console = request.form['console']

    # Recuperando e validando a partir dos campos de formulário com flask-wtf
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

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

    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console

    capa_jogo = retorna_imagem(id)
    # return render_template('editar.html', titulo= 'Editar Jogo', jogo=jogo, capa_jogo=capa_jogo) # render_template usado com flask puro
    return render_template('editar.html', titulo= 'Editar Jogo', id=id, capa_jogo=capa_jogo, form=form)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioJogo(request.form)
    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()

        # Requisição de campos do forms em flask puro
        # jogo.nome = request.form['nome']
        # jogo.categoria = request.form['categoria']
        # jogo.console = request.form['console']

        # Requisição de campos do forms em flask-wtf
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

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
    form = FormularioUsuario() #flask-wtform
    return render_template('login.html', proxima=proxima, form=form) # passamos proxima para a página, onde ela será capturada pelo forms (de forma escondida)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    # usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
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