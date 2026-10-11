"""
Description:   Write a brief description of the script's purpose here.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-10-10
"""

from typing import TypedDict
from pydantic import Field
from langgraph.graph import StateGraph, START, END

from cv_analyzer.services.web_scrapper import extraer_texto_url
from cv_analyzer.llm_workflows.pt_extractor import extraer_pt
from cv_analyzer.llm_workflows.cv_extractor import extraer_cv
from cv_analyzer.llm_workflows.evaluator import evaluar_candidato


# Definimos el esquema del estado

class AlignmentState(TypedDict):

    # Información básica del puesto de trabajo
    puesto_url: str
    texto_puesto:str
    puesto: str
    empresa: str
    nivel_puesto: str
    locacion_puesto: str
    modalidad_puesto: str
    salario_puesto: int
    beneficios: list[str]
    descripcion_puesto: str
    funciones_puesto: list[str]
    requisitos_obligatorios: list[str]
    requisitos_deseables: list[str]

    # Información del candidato y ajuste al puesto
    texto_cv: str
    nombre_candidato: str
    email_candidato: str
    telefono_candidato: str
    locacion_candidato: str
    experiencia_candidato: str
    educacion_candidato: str
    experiencia_años: int
    habilidades_tecnicas: list[str]
    habilidades_adicionales: list[str]

    # Información adicional del análisis del candidato respecto al puesto
    experiencia_relevante: str
    habilidades_clave: list[str]
    fortalezas: list[str]
    areas_mejora: list[str]
    porcentaje_ajuste: int
    justificacion: str


# Creamos el grafo de estados para el análisis del candidato
alignment_graph = StateGraph(AlignmentState)

# Definimos los nodos del grafo de análisis del candidato
alignment_graph.add_node("Extraer texto del puesto desde url",extraer_texto_url)
alignment_graph.add_node("Extraer información del puesto",extraer_pt)
alignment_graph.add_node("Extraer información del CV",extraer_cv)
alignment_graph.add_node("Evaluar ajuste del candidato",evaluar_candidato)

# Definimos las transiciones entre los nodos del grafo de análisis del candidato
alignment_graph.add_edge(START, "Extraer texto del puesto desde url")
alignment_graph.add_edge("Extraer texto del puesto desde url", "Extraer información del puesto")
alignment_graph.add_edge("Extraer información del puesto", "Extraer información del CV")
alignment_graph.add_edge("Extraer información del CV", "Evaluar ajuste del candidato")
alignment_graph.add_edge("Evaluar ajuste del candidato", END)
compiled_alignment_graph = alignment_graph.compile()