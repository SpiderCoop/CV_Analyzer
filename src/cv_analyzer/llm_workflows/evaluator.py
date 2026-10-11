"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.models.analysis_model import AnalisisCV
from cv_analyzer.states.alignment_state import AlignmentState
from cv_analyzer.prompts.analysis_prompts import crear_alignment_analysis_prompts
from cv_analyzer.services.llm import llm_model


def crear_evaluador_cv():

    modelo_base = llm_model

    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_alignment_analysis_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion


def evaluar_candidato(state: AlignmentState) -> AnalisisCV:

    estado = state.model_dump()

    try:
        cadena_evaluacion = crear_evaluador_cv()

        resultado = cadena_evaluacion.invoke(
            {"estado": estado}
        )

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al evaluar el candidato: {e}") from e
