"""
Description:   Write a brief description of the script's purpose here.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-10-10
"""

from typing import TypedDict


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
