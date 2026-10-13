"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.llm_workflows.base_workflow import create_llm_chain
from cv_analyzer.models.pt_model import PuestoTrabajo
from cv_analyzer.prompts.pt_prompts import EXTRACCION_PT_CHAT_PROMPT
from cv_analyzer.services.llm import llm_model
from cv_analyzer.states.alignment_state import AlignmentState


def extraer_pt(state: AlignmentState) -> PuestoTrabajo:

    texto_pt = state["texto_puesto"]

    try:
        cadena = create_llm_chain(llm_model, PuestoTrabajo, EXTRACCION_PT_CHAT_PROMPT)

        resultado = cadena.invoke({"texto": texto_pt})

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al procesar la descripción del puesto: {e}") from e
