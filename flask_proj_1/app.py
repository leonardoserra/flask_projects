from flask import Flask, request, send_from_directory, redirect, abort
from definitions import generate_page, render_component 
from components.card_component import card_component
import csv
app = Flask(__name__)

disponibilita = {
  "A123":123,
  "B345":77,
  "C773":6,
  "D888":98
}

#home
@app.route('/')
def home():
  return generate_page('Home', subtitle='Ciao a tutti sono la Homepage')

@app.route('/catalogo')
def catalogo():
  global disponibilita
  with open('./lista_prodotti.csv', 'r') as prodotti:
    prodotti_estratti = [p for p in csv.reader(prodotti, delimiter=',')]
    return generate_page('Catalogo', subtitle="PRODOTTI", *prodotti_estratti, components=[render_component('card.html')], disponibilita = disponibilita )

@app.route('/catalogo/<int:product_id>')
def show_product_description(product_id):
  with open('./lista_prodotti.csv', 'r') as prodotti:
    prodotti_estratti =[p for p in csv.reader(prodotti, delimiter=',')]
    prodotto = prodotti_estratti[product_id]
    return generate_page('Prodotto', ''.join(prodotto[3]) + '\n\nPrezzo: ' + ''.join(prodotto[2]) + '€' + ' Immagine: '+ f"<img src=\"{'/images/'+''.join(prodotto[0])}.jpg\">" , subtitle=''.join(prodotto[1]))

#metodi http
@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    return '<h1>LOGIN EFFETTUATO!</h1>'
  else:
    return generate_page('Pagina di Login', components=[render_component('login.html')], subtitle="Inserisci i tuoi dati")

#args con GET
@app.route('/somma')
def somma_get_query():
  print(request.args)
  if 'a' in request.args.keys() and 'b' in request.args.keys():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return F'SOMMA di {a} + {b} = {a + b}'
  else:
    return '<p>No args</p>'

#params con GET
@app.route('/somma/<int:a>/<int:b>')
def somma_get_url(a, b):
  print(request.args)
  return F'SOMMA di {a} + {b} = {a + b}'

#compra prodotto e togli da disponibilita
@app.route('/compra/<string:codice>')
def compra(codice):
  global disponibilita
  if codice in disponibilita:
    if disponibilita[codice] > 0:
      disponibilita[codice] -= 1
      return redirect('/catalogo')
    
@app.route('/card')
def card():
  return card_component('ciao', 'sono il content')

#rotta statica per immagini
@app.route('/images/<path:percorso_img>')
def send_images(percorso_img):
  return send_from_directory('./assets/img', percorso_img)

@app.route('/index') # lo reinvio a '/' perche li non ce piu
def index():
  return redirect('/')

@app.route('/privato') #qui non puoi andare
def privato():
  abort(401)#blocchi e mandi l'errore

@app.errorhandler(401) #gestisce quando ce l'errore 401
def unauthorized_error(error): #argomento error implicito
  return F'<h1>Non autorizzato: </h1><p>{error}</p>'
