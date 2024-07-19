# FLASK
- `Framework molto leggero` per webapp in python (micro-framework). 
- È `flessibile e modulare` quindi si possono installare diversi moduli e renderlo personalizzato.
- `Non segue dei pattern` stringenti o scaffolding quindi rende lo sviluppatore abbastanza libero di gestirsi il progetto.
- `Facile` da imparare.

## Storia
- Nato nel 2010 ma maturo da poco, la v1.0 nel 2019.
- la v2.0 nel 2021 con python >= v3.6
- Flask v3.0 nel settembre 2023. -> quella che useremo noi.

## Alternative a Flask
- `WSGI`: Web Server Gateway Interface, è uno standard python per le interfacce tra server Web. Flask è un un app WSGI.
- `Django`: Framework Python molto completo, basato su WSGI e pensato per app complesse, è `opinionated` quindi è piu restrittivo e rigido, è anche più difficile da imparare.

### Crea un Environment
```bash
mkdir myproject
cd myproject
py -3 -m nome_ambiente nome_cartella
```
### Attiva virtual environment
Nel terminale:
```bash
nome_cartella\Scripts\acivate
```
Per disattivarlo  
```bash
 deactivate
 ```
- Attivalo anche in vscode cliccando sulla versione python in basso a destra


## Routes
- I percorsi ai quali flask risponde (endpoint, url con relativi metodi)
  
Solo `Route`
```python
@app.route('/')
def home():
  return 'Hello world'
```
  
Con `parametri`:
```py
@app.route('/user/<username>')
def user(username):
  return f'ciao {username}'
```
  
Parametri con `tipo`:
```py
@app.route('/post/<int:post_id>')
def show_post(post_id:int):
  return f'<h1>Post number: {post_id}</h1>'
```

### Metodi HTTP sulle rotte
Per aggiungere il metodo oltre a GET, come secondo parametro alla decoration si mette una lista di str con i metodi.

```py
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return '<em>Autenticazione in corso...</em>'
  else:
    return '<h1>Pagina di Login</h1>'
```
  
Nell'oggetto Request ci sono i dati delle GET e POST:
- `request.args` -> sono gli argomenti della query string
- `request.data` -> il body ricevuto dal client
- `request.headers` -> gli headers
- `request.form` -> si usa coi form

### Routes Statiche
In flask puoi fornire direttamente dei file (immagini di solo) creando routes direttamente collegate al filesystem, puoi designare delle cartelle come asset statici.
Si utilizza `send_from_directory`
```py
from flask import send_from_directory
@app.route('/images/<path:percorso>')
def send_images(percorso):
  return send_from_directory('assets/img', percorso)
```
### L'oggetto globale g
Oggetto globale per scambiare valori e variabili fra le routes durante una request
```py
from flask import g

def add_to_cart(price):
  g.totale_carrello += price

@app.route('/add-to-cart', methods=['POST'])
def pass_to_cart():
  if request.method == 'POST':
    add_to_cart(request.args.get('price') if 'price' in request.args.keys() else 0)
```

### Routes multiple
Per avere più routes diverse per lo stesso risultato
```py
@app.route('/')
@app.route('/home')
def home():
  return 'Sono la homepage.'
```

### Redirect ed errori
Usi `redirect` per i 300 e `abort` per i 400
```py
from flask import redirect, abort
@app.route('/index') # lo reinvio a '/' perche li non ce piu
def index():
  return redirect('/')

@app.route('/privato') #qui non puoi andare
def privato():
  abort(401)#blocchi e mandi lo status

@app.errorhandler(401)
def unauthorized_error(error): #argomento error implicito
  return '<h1>Non autorizzato</h1>'
```
### url_for
Ti ritorna l'url che viene ritornato da una delle rotte, 
```py
from flask import url_for
@app.route('/info')
def info():
  return url_for(nome_funzione,eventuale_param=valore)
```
### Scaffolding

-`run.py`: Il punto di ingresso dell app, crea il server, fa partire il DB con le config o per prod o dev o staging ad esempio prendendole dal config.py
- `config.py`: il file dove sono differenziate le configurazioni (prod, staging, dev)
- `app/`: cartella dove ci sono:
    - `__init__.py`: creazione della app
    - `routes.py`: contiene tutte le routes
    - `models.py`: contiene i modelli
    - `templates/`: cartella dove sono contenuti i templates html.