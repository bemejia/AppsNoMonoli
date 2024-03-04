# Usa una imagen base oficial de Python
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al directorio de trabajo actual (/app) en el contenedor
COPY . /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
