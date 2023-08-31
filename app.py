from flask import Flask

app = Flask('meu app')

@app.route("/")
def hello ():
    return 'Hello Word'

@app.route("/novo")
def novo():
    return "<hi> Nova pagina</h1>"