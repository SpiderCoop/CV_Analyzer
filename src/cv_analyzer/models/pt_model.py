from pydantic import BaseModel, Field


class PuestoTrabajo(BaseModel):
    """Modelo de datos para extraccion de elementos del puesto de trabajo."""

    empresa: str = Field(
        default="No especificada",
        description="Nombre de la empresa que publica el puesto de trabajo",
    )
    puesto: str = Field(
        default="No especificado", description="Nombre o titulo del puesto de trabajo"
    )
    nivel_puesto: str = Field(
        default="No especificado",
        description="Nivel del puesto de trabajo (entrada, medio, gerencial o dirección)",
    )
    locacion_puesto: str = Field(
        default="No especificada",
        description="País, estado donde se encuentra el puesto de trabajo",
    )
    modalidad_puesto: str = Field(
        default="No especificada",
        description="modalidad del puesto de trabajo (Remoto, Híbrido o Presencial)",
    )
    salario_puesto: int | None = Field(
        default=0,
        description="Salario (si se menciona). Devuelve 0 si no se menciona.",
    )
    beneficios: list[str] = Field(
        default_factory=list, description="Lista de beneficios y/o prestaciones"
    )
    descripcion_puesto: str = Field(
        default="No especificada",
        description="Descripcion general del puesto de trabajo",
    )
    funciones_puesto: list[str] = Field(
        default_factory=list,
        description="Lista de funciones y responsabilidades del puesto de trabajo",
    )
    requisitos_obligatorios: list[str] = Field(
        default_factory=list, description="Lista de requisitos obligatorios solicitados"
    )
    requisitos_deseables: list[str] = Field(
        default_factory=list, description="Lista de requisitos deseables"
    )
