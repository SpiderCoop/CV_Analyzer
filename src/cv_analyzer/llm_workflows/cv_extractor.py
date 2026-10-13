"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.llm_workflows.base_workflow import create_llm_chain
from cv_analyzer.models.cv_model import Curriculo
from cv_analyzer.prompts.cv_prompts import EXTRACCION_CV_CHAT_PROMPT
from cv_analyzer.services.llm import llm_model
from cv_analyzer.states.alignment_state import AlignmentState


def extraer_cv(state: AlignmentState) -> Curriculo:

    texto_cv = state["texto_cv"]

    try:
        cadena = create_llm_chain(llm_model, Curriculo, EXTRACCION_CV_CHAT_PROMPT)

        resultado = cadena.invoke(
            {"texto": texto_cv},
        )

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al procesar el CV: {e}") from e
