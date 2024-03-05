from faker import Faker
import random
import json

fake = Faker()

def run(event, context):
    num_propiedades = 5  # Número de propiedades a generar

    departamentos = ["Antioquia", "Bogotá D.C.", "Valle del Cauca", "Atlántico", "Santander", "Boyaca", "Cundinamarca"]
    ciudades = ["Medellín", "Bogotá", "Cali", "Barranquilla", "Bucaramanga", "Tunja", "Chía"]
    tipos_propiedad = ["Vivienda", "Comercial", "Industrial", "Terreno"]
    estados_legales = ["Libre de gravámenes", "Hipotecada", "Arrendada", "En litigio", "Embargada"]
    tipo_contrato = ["Compra", "Arrendamiento"]
    documentos = ["Escritura pública", "Contrato de arrendamiento", "Certificado de libertad y tradición"]

    propiedades = []

    for _ in range(num_propiedades):
        departamento_ciudad = random.randint(0, 6)
        propiedad = {
            "id_propiedad": fake.unique.random_int(min=1, max=1000),
            "tipo_propiedad": random.choice(tipos_propiedad),  
            "pais": "Colombia",
            "departamento": departamentos[departamento_ciudad],
            "ciudad": ciudades[departamento_ciudad],
            "direccion": fake.street_address(),
            "estado_legal": random.choice(estados_legales),
            "tipo_contrato": random.choice(tipo_contrato),
            "documento_legal": random.choice(documentos),
            "valor_catastral": random.randint(10000, 1000000),
            "anio_construccion": random.randint(1900, 2023),
            "superficie_terreno": random.randint(50, 1000),
            "superficie_construida": random.randint(30, 900),
            "nombre_propietario": fake.name(),
            "domicilio_propietario": fake.address()
        }
        propiedades.append(propiedad)

    response = {
        "statusCode": 200,
        "body": json.dumps(propiedades)
    }

    return response

if __name__ == '__main__':
    print(run(None, None))
