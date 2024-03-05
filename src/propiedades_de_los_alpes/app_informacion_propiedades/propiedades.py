import json

from flask import request
from flask import Response
from modulos.aplicacion.comandos import ejecutar_comando
from modulos.aplicacion.queries import ejecutar_query

from flask import Flask
app = Flask(__name__)

@app.route('/propiedad-comando', methods=('POST',))
def crear_propiedad_asincrona():
    try:
        propiedad_dict = request.json
        ejecutar_comando(propiedad_dict)
        
        return Response('{}', status=202, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@app.route('/propiedad-query/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    query_resultado = ejecutar_query(id)
    return str(query_resultado)
    
if __name__ == '__main__':
    app.run(debug=True)