"""
Descripción:   Script para la ejecucion del pipeline
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from config import CV_PATH, RECIPIENTS, URL
from cv_analyzer.reports.alignment_report import crear_reporte_oportunidad_laboral
from cv_analyzer.services.email_manager import email
from cv_analyzer.services.pdf_processor import extraer_texto_pdf
from cv_analyzer.services.web_scrapper import extraer_texto_url
from cv_analyzer.states.alignment_graph import alignment_graph
from cv_analyzer.states.graph_executioner import execute_graph

# Creamos el estado inicial
estado_inicial = {
    "puesto_url": URL,
    "texto_puesto": extraer_texto_url(URL),
    "texto_cv": extraer_texto_pdf(CV_PATH),
}

# Realizamos la evaluacion
resultado = execute_graph(alignment_graph, estado_inicial)

# Enviamos la evaluacion
cuerpo_correo = crear_reporte_oportunidad_laboral(resultado)
email.send(
    f"Evaluacion de puesto de trabajo: {resultado.get('empresa')} | {resultado.get('puesto')}",
    cuerpo_correo,
    [RECIPIENTS],
)
