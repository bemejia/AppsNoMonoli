from flask import Flask, jsonify
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

@app.route('/propiedad/<int:id>', methods=['GET'])
def obtener_propiedad(id):
    fake = Faker()
    Faker.seed(id)  # Setting a seed for reproducibility

    departamentos = ["Antioquia", "Bogotá D.C.", "Valle del Cauca", "Atlántico", "Santander", "Boyaca", "Cundinamarca"]
    ciudades = ["Medellín", "Bogotá", "Cali", "Barranquilla", "Bucaramanga", "Tunja", "Chia"]
    tipos_suelo_co = ["Urbano", "Rural", "Comercial", "Mixto"]
    usos_principales_co = ["Residencial", "Comercial", "Industrial", "Recreacional"]
    tipos_propiedad = ["Vivienda", "Comercial", "Industrial", "Terreno"]
    instalaciones = [["Ascensor", "Calefacción central"], ["Piscina", "Jardín"], ["Garaje", "Solarium"]]
    estados_conservacion = ["Nuevo", "Bueno", "Regular", "Malo"]

    # Generate property data using faker and random choices for Colombian standards
    departamento_ciudad = fake.random_int(min=0, max=6)
    propiedad = {
        "id_propiedad": id,
        "tipo_propiedad":  fake.random_element(elements=tipos_propiedad),  # Assume same property types
        "pais": "Colombia",
        "departamento": departamentos[departamento_ciudad],
        "ciudad": ciudades[departamento_ciudad],
        "direccion": fake.street_address(),
        "codigo_postal": fake.postcode(),  # Assuming use of postal codes
        "referencia_catastral": fake.bothify(text='##########??????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        "valor_catastral": fake.random_int(min=10000, max=1000000),
        "año_construccion": fake.random_int(min=1900, max=2023),
        "superficie_terreno": fake.random_int(min=50, max=1000),
        "superficie_construida": fake.random_int(min=30, max=900),
        "nombre": fake.name(),
        "domicilio_fiscal": fake.address(),
        "tipo_suelo": fake.random_element(elements=tipos_suelo_co), 
        "uso_principal": fake.random_element(elements=usos_principales_co), 
        "estado_conservacion": random.choice(estados_conservacion),  # Assume same conservation states
        "instalaciones": fake.random_element(elements=instalaciones)   # Assume same installations options
        }

    return jsonify(propiedad)

if __name__ == '__main__':
    app.run()
