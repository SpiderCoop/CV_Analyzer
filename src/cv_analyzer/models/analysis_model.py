from pydantic import BaseModel, Field


class AlignmentAnalysis(BaseModel):
    """Modelo de datos para el análisis de alineacion entre un candidato y un puesto de trabajo."""

    experiencia_años: int | None = Field(
        default=0,
        description="Años totales de experiencia laboral relevante para el puesto.",
    )
    experiencia_relevante: str = Field(
        default="No especificada",
        description="Resumen conciso de la experiencia más relevante para el puesto específico.",
    )
    habilidades_clave: list[str] = Field(
        default_factory=list,
        description="Lista de las 3-5 habilidades del candidato más relevantes para el puesto.",
    )
    fortalezas: list[str] = Field(
        default_factory=list,
        description="Lista de 3-5 principales fortalezas del candidato basadas en su perfil para el puesto.",
    )
    areas_mejora: list[str] = Field(
        default_factory=list,
        description="Lista de 2-4 áreas donde el candidato podría desarrollarse o mejorar para el puesto específico.",
    )
    porcentaje_ajuste: int = Field(
        default=0,
        description="Porcentaje de ajuste al puesto entre 0 y 100 basado en experiencia, habilidades y formación.",
    )
    justificacion: str = Field(
        default="Sin justificación",
        description="Justificación detallada del porcentaje de ajuste al puesto basado en la experiencia, habilidades y formación del candidato.",
    )
