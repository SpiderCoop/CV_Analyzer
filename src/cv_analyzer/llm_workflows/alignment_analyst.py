"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.llm_workflows.base_workflow import create_llm_chain
from cv_analyzer.models.alignment_model import AlignmentAnalysis
from cv_analyzer.prompts.alignment_prompts import ALIGNMENT_ANALYSIS_CHAT_PROMPT
from cv_analyzer.services.llm import llm_model
from cv_analyzer.states.alignment_state import AlignmentState


def alignment_analysis(state: AlignmentState) -> dict:

    try:
        cadena = create_llm_chain(
            llm_model, AlignmentAnalysis, ALIGNMENT_ANALYSIS_CHAT_PROMPT
        )

        resultado = cadena.invoke(state)

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al evaluar el candidato: {e}") from e
