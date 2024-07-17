from flask import Flask
from definitions import generate_page
import csv
app = Flask(__name__)

@app.route('/')
def home():
  return generate_page('Home', 'Ciao a tutti sono la Homepage')

@app.route('/catalogo')
def catalogo():
  with open('./lista_prodotti.csv', 'r') as prodotti:
    prodotti_estratti =[p for p in csv.reader(prodotti, delimiter=',')]
    return generate_page('Catalogo', *prodotti_estratti)


  
