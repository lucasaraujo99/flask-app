# CRUD

- Create
- Read
- Update
- Delete

## Create

```
novo_objeto = Objeto(nome=nome, categoria=categoria)
db.session.add(novo_objeto)
db.session.commit()
```

**Importante:** após fazer um mudança, é necessário fazer o **commit**

## Read

Operações de leitura são feitas através de **query**

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

## Update

O update é semelhante ao create

```
objeto = Objetos.query.filter_by(id=id).first()
objeto.nome = novo_nome
objeto.categoria = nova_categoria

db.session.add(objeto)
db.session.commit()
```

## Delete

A operação de delete é feita através de uma query

```
Objetos.query.filter_by(id=id).delete()
db.session.commit()
```