#!/bin/bash

gcloud functions deploy ejecutar_app --runtime python39 --trigger-topic solicitudes_catastro --entry-point=ejecutar_app