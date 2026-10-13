from pydantic import BaseModel, Field


class Curriculo(BaseModel):
    """Modelo de datos para el análisis completo y general de un CV."""

    nombre_candidato: str = Field(
        default="No especificado",
        description="Nombre completo del candidato extraído del CV.",
    )
    email_candidato: str = Field(
        default="No especificado",
        description="Correo electrónico del candidato extraído del CV.",
    )
    telefono_candidato: str = Field(
        default="No especificado",
        description="Número de teléfono del candidato extraído del CV.",
    )
    # Para enteros, es mejor usar Optional para que devuelva None o 0 si no lo encuentra
    experiencia_años: int | None = Field(
        default=0, description="Años totales de experiencia laboral."
    )
    educacion_candidato: str = Field(
        default="No especificada",
        description="Nivel educativo más alto y especialización principal.",
    )
    locacion_candidato: str = Field(
        default="No especificada", description="Lugar de residencia del candidato."
    )
    experiencia_candidato: str = Field(
        default="Sin experiencia detallada",
        description="Resumen conciso de la experiencia laboral del candidato, enfocado en los últimos dos puestos o 10 años de experiencia.",
    )
    habilidades_tecnicas: list[str] = Field(
        default_factory=list,
        description="Lista de 5-10 habilidades tecnicas del candidato.",
    )
    habilidades_adicionales: list[str] = Field(
        default_factory=list,
        description="Lista de 3-5 habilidades adicionales del candidato basadas en su perfil.",
    )
