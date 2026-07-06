"""
Descripción:   Script para la ejecucion del pipeline
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.services.evaluate import evaluate
from cv_analyzer.services.email_manager import email
from cv_analyzer.reports.job_hunting_report import crear_reporte_oportunidad_laboral

from cv_analyzer.services.config import *


# Realizamos la evaluacion
puesto_trabajo, evaluacion = evaluate(url, cv_path)

# Enviamos la evaluacion
cuerpo_correo =  crear_reporte_oportunidad_laboral(evaluacion, puesto_trabajo)
email.send(f'Evaluacion de puesto de trabajo: {puesto_trabajo.puesto}', cuerpo_correo, [RECIPIENTS])