"""
Descripción:   Script para la ejecucion del pipeline
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

import os
from dotenv import load_dotenv

from services.evaluate import evaluate
from services.email_manager import email
from reports.job_hunting_report import crear_reporte_oportunidad_laboral


# variables iniciales y de configuracion
cv_path = "data/CV David Jimenez Cooper 2026 En.pdf"

load_dotenv()
url = os.environ.get('url')
recipients = os.environ.get('RECIPIENTS')

# Realizamos la evaluacion
puesto_trabajo, evaluacion = evaluate(url, cv_path)

# Enviamos la evaluacion
cuerpo_correo =  crear_reporte_oportunidad_laboral(evaluacion, puesto_trabajo)
email.send(f'Evaluacion de puesto de trabajo: {puesto_trabajo.puesto}', cuerpo_correo, [recipients])