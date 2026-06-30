"""
Descripción:   Funciones de integracion del modelo evaluador
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from models.pt_model import PuestoTrabajo
from prompts.pt_prompts import crear_extraccion_prompts

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Falta la clave de API de Google. Define GOOGLE_API_KEY en el entorno.")

def crear_extractor_pt():

    modelo_base = ChatGoogleGenerativeAI(
        model="gemma-4-31b-it",
        temperature=0.2,
        api_key=api_key,
    )

    modelo_estructurado = modelo_base.with_structured_output(PuestoTrabajo)
    chat_prompt = crear_extraccion_prompts()
    cadena = chat_prompt | modelo_estructurado

    return cadena

def extraer_pt(texto_pt: str) -> PuestoTrabajo:
    try:
        cadena_evaluacion = crear_extractor_pt()

        resultado = cadena_evaluacion.invoke({
            "texto": texto_pt
        })

        return resultado
    
    except Exception as e:
        return PuestoTrabajo(
            empresa = "Error",
            puesto = "Error",
            nivel = "Error",
            salario = 0,
            beneficios = ["Error"],
            descripcion = "Error",
            funciones = ["Error"],
            requisitos_obligatorios = ["Error"],
            requisitos_deseables = ["Error"],
            modalidad = "Error",
        )
