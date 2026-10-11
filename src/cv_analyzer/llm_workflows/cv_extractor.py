"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.models.cv_model import Curriculo
from cv_analyzer.prompts.cv_prompts import crear_cv_extraccion_prompts
from cv_analyzer.services.llm import llm_model
from cv_analyzer.states.alignment_state import AlignmentState


def crear_extractor_cv():

    modelo_base = llm_model

    modelo_estructurado = modelo_base.with_structured_output(Curriculo)
    chat_prompt = crear_cv_extraccion_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion


def extraer_cv(state: AlignmentState) -> Curriculo:

    texto_cv = state["texto_cv"]

    try:
        cadena_evaluacion = crear_extractor_cv()

        resultado = cadena_evaluacion.invoke(
            {"texto": texto_cv}
        )

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al procesar el CV: {e}") from e