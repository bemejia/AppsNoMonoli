#!/bin/bash

# Despliegue de la función de Google Cloud Functions
#gcloud functions deploy ejecutar_app --runtime python39 --trigger-topic solicitudes_catastro --entry-point=ejecutar_app

# Despliegue en Kubernetes
docker build -t servicio_auditoria .
docker tag servicio_auditoria gcr.io/apps-no-monoliticas-415223/servicio_auditoria
docker push gcr.io/apps-no-monoliticas-415223/servicio_auditoria
#kubectl create secret generic mi-secreto --from-literal=PULSAR_TOKEN="" # Usar esta linea para configurar el token de pulsar
#gcloud container clusters get-credentials clus-no-monoliticas --zone us-central1 --project apps-no-monoliticas-415223 # Usar esta linea para obtener las credenciales del cluster
kubectl apply -f deployment.yaml