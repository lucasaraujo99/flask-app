# SqlAlchemy

**OBS:** nesse método, usamos um banco em mysql com as tabelas já configuradas

## Iniciando

Importar o sqlalchemy

```
from flask_sqlalchemy import SQLAlchemy
```

Criar uma URI que indicará as informações de conexão com o banco de dados. Devemos guardá-la em uma variável dentro das configurações da aplicação

```
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )
```

Instanciar o sqlalchemy

```
db = SQLAlchemy(app)
```

## Classes

Criar classes equivalentes às tabelas do sql

```
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
```

Tabela original:

```
CREATE TABLE `jogos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
```

## Querys

**order_by():**

```
lista = Jogos.query.order_by(Jogos.id)
```

**filter_by():**

```
jogo = Jogos.query.filter_by(nome=nome_do_jogo).first()
```

**OBS:** querys retornam valores de True ou False além da consulta e podem ser usadas em condicionais

```
jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash("Jogo já existente")
        ...
```