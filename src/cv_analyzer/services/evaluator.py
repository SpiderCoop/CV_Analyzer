"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.models.analysis_model import AnalisisCV
from cv_analyzer.prompts.cv_prompts import crear_cv_analysis_prompts
from cv_analyzer.services.llm import llm_model


def crear_evaluador_cv():

    modelo_base = llm_model

    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_cv_analysis_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion


def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()

        resultado = cadena_evaluacion.invoke(
            {"texto_cv": texto_cv, "descripcion_puesto": descripcion_puesto}
        )

        return resultado

    except Exception as e:
        raise ValueError(f"Error al evaluar el candidato: {e}") from e
