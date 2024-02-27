from sqlalchemy import create_engine

# Conectar a una base de datos SQLite en memoria
engine = create_engine('postgresql://postgres:prueba@35.184.202.9:5432/postgres')
