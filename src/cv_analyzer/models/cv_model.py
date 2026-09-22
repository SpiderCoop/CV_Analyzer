from pydantic import BaseModel, Field


class Curriculo(BaseModel):
    """Modelo de datos para el análisis completo y general de un CV."""

    nombre_candidato: str = Field(
        description="Nombre completo del candidato extraído del CV."
    )
    experiencia_años: int = Field(description="Años totales de experiencia laboral.")
    educacion: str = Field(
        description="Nivel educativo más alto y especialización principal."
    )
    locacion: str = Field(description="Lugar de residencia del candidato.")
    experiencia: str = Field(
        description="Resumen conciso de la experiencia laboral del candidato, enfocado en los últimos dos puestos o 10 años de experiencia."
    )
    habilidades_tecnicas: list[str] = Field(
        description="Lista de 5-10 habilidades tecnicas del candidato."
    )
    habilidades_adicionales: list[str] = Field(
        description="Lista de 3-5 habilidades adicionales del candidato basadas en su perfil."
    )
    areas_mejora: list[str] = Field(
        description="Lista de 2-4 áreas donde el candidato podría desarrollarse o mejorar."
    )
