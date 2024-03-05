from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_ENDPOINT= os.getenv("DB_ENDPOINT")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT")
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}:{DB_PORT}/{DB_DATABASE}"

class Database:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Configura la URL de la base de datos
            DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_ENDPOINT}:{DB_PORT}/{DB_DATABASE}"
            # Crea el motor SQLAlchemy
            cls._instance.engine = create_engine(DB_URL)
            # Crea un creador de sesión
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            # Crea la sesión
            cls._instance.session = cls._instance.Session()

        return cls._instance
    
    def get_engine(self):
        return create_engine(DB_URL)

    def get_session(self):
        return self.Session()