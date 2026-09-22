"""
Descripción:   Script para la ejecucion del pipeline
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.reports.job_hunting_report import crear_reporte_oportunidad_laboral
from cv_analyzer.services.email_manager import email
from cv_analyzer.services.evaluation_service import evaluate

from config import CV_PATH, RECIPIENTS, URL

# Realizamos la evaluacion
puesto_trabajo, evaluacion = evaluate(URL, CV_PATH)

# Enviamos la evaluacion
cuerpo_correo = crear_reporte_oportunidad_laboral(evaluacion, puesto_trabajo)
email.send(
    f"Evaluacion de puesto de trabajo: {puesto_trabajo.puesto}",
    cuerpo_correo,
    [RECIPIENTS],
)
