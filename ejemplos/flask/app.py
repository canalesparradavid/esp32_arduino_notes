import re
from flask import Flask, render_template, request, Response, jsonify
from back import Database

app = Flask(__name__)
#CORS(app)

"""if __name__ == "__main__":
    # Cambia la dirección IP a 0.0.0.0 para escuchar en todas las interfaces de red
    app.run(host='192.168.168.43', port=5000)"""

config = {
    'host': 'localhost',
    'db': 'flaskApplication'
}

def removePunctuationSymbols(text):
    """Elimina simbolos de puntuación de un texto dado."""
    accepted_chars = re.compile(r'[^0-9a-z]')
    text = accepted_chars.sub(' ', text).strip()
    return re.sub(' +', '', text)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/api/v1/vote', methods=['POST'])
def vote():
    """Votar en una categoría."""
    try:
        if request.is_json:
           
            data = request.get_json()
            print(data)
            votation = data['votation']
            category = data['valor1']

            db = Database(config)
            db.create(votation, category)
            db.close()
            return Response(status=200)
        return Response(status=403)
       
    except Exception as e:
        message = {
            'message': e
        }
        resp = jsonify(message)
        resp.status_code = 500
        return resp
