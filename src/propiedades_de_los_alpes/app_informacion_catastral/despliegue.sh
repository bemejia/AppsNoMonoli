#!/bin/bash

# Despliegue de la función de Google Cloud Functions
#gcloud functions deploy ejecutar_app --runtime python39 --trigger-topic solicitudes_catastro --entry-point=ejecutar_app

# Despliegue en Kubernetes
docker build -t servicio_catastro_enr .
docker tag servicio_catastro_enr gcr.io/apps-no-monoliticas-415223/servicio_catastro_enr
docker push gcr.io/apps-no-monoliticas-415223/servicio_catastro_enr
#kubectl create secret generic mi-secreto --from-literal=PULSAR_TOKEN="" # Usar esta linea para configurar el token de pulsar
#gcloud container clusters get-credentials clus-no-monoliticas --zone us-central1 --project apps-no-monoliticas-415223
kubectl apply -f deployment.yaml