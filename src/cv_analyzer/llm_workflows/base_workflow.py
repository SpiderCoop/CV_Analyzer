"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""


def create_llm_chain(llm_model, structured_output_model, chat_prompt_creator):

    modelo_base = llm_model

    modelo_estructurado = modelo_base.with_structured_output(structured_output_model)
    chat_prompt = chat_prompt_creator
    cadena = (chat_prompt | modelo_estructurado).with_retry(
        stop_after_attempt=4,  # Intentará hasta 4 veces antes de rendirse
        wait_exponential_jitter=True,  # Esperará cada vez un poco más (ej. 2s, 4s, 8s)
    )

    return cadena
