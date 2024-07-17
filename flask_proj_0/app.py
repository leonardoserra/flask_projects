from flask import Flask #import della classe Flask.

app = Flask(__name__) #costruiamo un istanza della nostra WebApp, con __name__ usiamo il nome del file.

@app.route("/")# con questo decorator crei un endpoint che una volta chiamato eseguirà la funzione che ce sotto
def hello_world():
    return "<h1>Ciao caro!</h1>"
