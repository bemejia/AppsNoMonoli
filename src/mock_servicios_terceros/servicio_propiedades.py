from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

@app.route('/propiedad/<int:id>', methods=['GET'])
def obtener_propiedad(id):
    fake = Faker()
    Faker.seed(id)  # Setting a seed for reproducibility

    tipos_propiedad = ["oficina", "minorista", "industrial", "uso especializado"]
    ciudades = ["Medellín", "Bogotá", "Cali", "Barranquilla", "Bucaramanga", "Tunja", "Chia"]
    caracteristicas = ["Ascensor", "Calefacción central", "Piscina", "Jardín", "Garaje", "Solarium"]

    # Generate property data using faker and random choices for Colombian standards
    propiedad = {"id_propiedad": id,         
                 "tipo":  fake.random_element(elements=tipos_propiedad),        
                 "ciudad": fake.random_element(elements=ciudades),         
                 "precio_min": fake.random_int(min=50000000, max=100000000),  
                 "precio_max": fake.random_int(min=100000001, max=500000000), 
                 "tamano_min": fake.random_int(min=50, max=500),  
                 "tamano_max": fake.random_int(min=501, max=1000), 
                 "caracteristica": fake.random_element(elements=caracteristicas),         
                 }    

    return jsonify(propiedad)

if __name__ == '__main__':
    app.run()
