#!/bin/bash

# Configura tus variables
PROJECT_ID="apps-no-monoliticas-415223"
APP_NAME="mock_servicios_terceros_web"
REGION="us-central1"
SERVICE_NAME="servicio-tercero-catastro"

# Construye la imagen de Docker
docker build -t gcr.io/$PROJECT_ID/$APP_NAME .

# Sube la imagen a Google Container Registry
docker push gcr.io/$PROJECT_ID/$APP_NAME

# Despliega la imagen en Cloud Run
gcloud run deploy $SERVICE_NAME --image gcr.io/$PROJECT_ID/$APP_NAME --platform managed --region $REGION --allow-unauthenticated