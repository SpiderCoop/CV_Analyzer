"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from cv_analyzer.models.pt_model import PuestoTrabajo
from cv_analyzer.prompts.pt_prompts import crear_pt_extraccion_prompts
from cv_analyzer.services.llm import llm_model
from cv_analyzer.states.alignment_state import AlignmentState


def crear_extractor_pt():

    modelo_base = llm_model

    modelo_estructurado = modelo_base.with_structured_output(PuestoTrabajo)
    chat_prompt = crear_pt_extraccion_prompts()
    cadena = chat_prompt | modelo_estructurado

    return cadena


def extraer_pt(state: AlignmentState) -> PuestoTrabajo:

    texto_pt = state["texto_puesto"]

    try:
        cadena_evaluacion = crear_extractor_pt()

        resultado = cadena_evaluacion.invoke({"texto": texto_pt})

        return resultado.model_dump()

    except Exception as e:
        raise ValueError(f"Error al procesar la descripción del puesto: {e}") from e
