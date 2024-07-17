from flask import Flask
from definitions import generate_page, render_component
import csv
app = Flask(__name__)

@app.route('/')
def home():
  return generate_page('Home', subtitle='Ciao a tutti sono la Homepage')

@app.route('/catalogo')
def catalogo():
  with open('./lista_prodotti.csv', 'r') as prodotti:
    prodotti_estratti = [p for p in csv.reader(prodotti, delimiter=',')]
    prodotti_estratti.append([render_component('card.html')])
    return generate_page('Catalogo',subtitle="PRODOTTI", *prodotti_estratti,)

@app.route('/catalogo/<int:product_id>')
def show_product(product_id):
  with open('./lista_prodotti.csv', 'r') as prodotti:
    prodotti_estratti =[p for p in csv.reader(prodotti, delimiter=',')]
    return generate_page('Catalogo', ' '.join(prodotti_estratti[product_id]) ,subtitle="PRODOTTI")

  
