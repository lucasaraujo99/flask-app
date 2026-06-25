# Flask App

Projeto de aplicativo web em Flask, simulando uma biblioteca de jogos eletrônicos.

## Objetivos

- Aplicação web com Flask com conteúdos dinâmicos
- Captura de inputs do usuário
- Interface usando HTML e Bootstrap
- Sistema de login e autorização
- Definição de rotas, redirecionamentos e templates
- URL dinâmicas

## Inicialização e Execução do Projeto

### Criar pasta venv
- linux: python3 -m venv venv 
- windows: py -3 -m venv .venv

### Ativa ambiente virtual
- linux: source /venv/bin/activate /
- windows: .venv\Scripts\activate

### Instalar requerimentos
- pip install -r requirements.txt

### Rodar
- python jogoteca.py

## Estrutura do Projeto

```
flask-app/
├── anotacoes/
├── static/
├── templates/
├── uploads/
├── config.py
├── jogoteca.py
├── models.py
├── prepara_banco.py
├── views.py
└── ...
```

anotacoes/ → material de consulta

static/ → arquivos de estilo (css e bootstrap)

templates/ → arquivos de interface (html)

uploads/ → contém as imagens guardadas localmente

config.py → arquivo de configuração do projeto (chave de criptografia, uri)

jogoteca.py → arquivo principal da aplicação (instancia e roda)

models.py → arquivo de classes equivalentes às tabelas do mysql (Jogos, Usuarios)

prepara_banco.py → arquivo de inicialização do banco MySql usando para armazenar os dados da aplicação

views.py → arquivo de rotas (routes) (index, login, autenticar, etc)