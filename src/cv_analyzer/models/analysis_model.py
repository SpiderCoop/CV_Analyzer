from pydantic import BaseModel, Field


class AnalisisCV(BaseModel):
    """Modelo de datos para el análisis completo de un Cv."""

    experiencia_años: int = Field(
        description="Años totales de experiencia laboral relevante para el puesto."
    )
    experiencia_relevante: str = Field(
        description="Resumen conciso de la experiencia más relevante para el puesto específico."
    )
    habilidades_clave: list[str] = Field(
        description="Lista de las 3-5 habilidades del candidato más relevantes para el puesto."
    )
    fortalezas: list[str] = Field(
        description="Lista de 3-5 principales fortalezas del candidato basadas en su perfil para el puesto."
    )
    areas_mejora: list[str] = Field(
        description="Lista de 2-4 áreas donde el candidato podría desarrollarse o mejorar para el puesto específico."
    )
    porcentaje_ajuste: int = Field(
        description="Porcetaje de ajuste al puesto (0-100) basado en experiencia, habilidades y formación.",
        ge=0,
        le=100,
    )
