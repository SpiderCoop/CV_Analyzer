"""
Descripción:   Script para la ejecucion del pipeline
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.services.pdf_processor import extraer_texto_pdf
from cv_analyzer.states.alignment_graph import compiled_alignment_graph
from cv_analyzer.reports.alignment_report import crear_reporte_oportunidad_laboral
from cv_analyzer.services.email_manager import email

from config import CV_PATH, RECIPIENTS, URL


# Creamos el estado inicial
estado_inicial = {
    "puesto_url": URL,
    "texto_cv": extraer_texto_pdf(CV_PATH),
}

# Realizamos la evaluacion
resultado = compiled_alignment_graph.invoke(estado_inicial)

# Enviamos la evaluacion
cuerpo_correo = crear_reporte_oportunidad_laboral(resultado)
email.send(
    f"Evaluacion de puesto de trabajo: {resultado.get('empresa')} | {resultado.get('puesto')}",
    cuerpo_correo,
    RECIPIENTS,
)
