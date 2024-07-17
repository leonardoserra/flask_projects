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
