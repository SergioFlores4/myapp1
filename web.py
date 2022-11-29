from flask import Flask

app = Flask(__name__)

# arranquem l'aplicacio
# si no especifiquem res al decorator, és el mètode GET
@app.route("/")
def formulari_get():
	# mostrem el formulari
	return """
<form method='post'>
Introdueix el teu nom:
<input name='nom' type='text' />
<br>
<input type='submit'>
</form>
"""

# important importar la request per accedir a les dades adjuntes
from flask import request

@app.route("/", methods=['POST'])
def formulari_post():
	# processem les dades del formulari
	nom = request.form["nom"]
	return "Salut, {}".format(nom)


