"""
Descripción:   Script para la evaluacion del candidato al puesto de trabajo
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""


import os
from dotenv import load_dotenv

from services.web_scrapper import extraer_texto_url
from services.pdf_processor import extraer_texto_pdf
from services.email_manager import email
from reports.job_hunting_report import crear_reporte_oportunidad_laboral

from services.pt_extractor import extraer_pt
from services.cv_evaluator import evaluar_candidato


# variables iniciales y de configuracion
cv_path = "data/CV David Jimenez Cooper 2026 En.pdf"

load_dotenv()
url = os.environ.get('url')
recipients = os.environ.get('RECIPIENTS')

# Iniciamos extrayendo el texto de url
texto_pt_raw = extraer_texto_url(url)
texto_pt = extraer_pt(texto_pt_raw)
texto_pt_str = texto_pt.model_dump_json()


# Obtenemos el texto del cv
texto_cv = extraer_texto_pdf(cv_path)

# Realizamos la evaluacion
evaluacion = evaluar_candidato(texto_cv, texto_pt_str)

# Enviamos la evaluacion
cuerpo_correo =  crear_reporte_oportunidad_laboral(evaluacion, texto_pt)
email.send('Evaluacion de puesto de trabajo', cuerpo_correo, [recipients])