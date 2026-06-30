from pydantic import BaseModel, Field

class PuestoTrabajo(BaseModel):
    """Modelo de datos para extraccion de elementos del puesto de trabajo."""

    empresa: str = Field(description="Nombre de la empresa que publica el puesto de trabajo")
    puesto: str = Field(description="Nombre o titulo del puesto de trabajo")
    nivel: str = Field(description="Nivel del puesto de trabajo (entrada, medio, gerencial o dirección)")
    salario: int = Field(description="Salario (si se menciona)",)
    beneficios: list[str] = Field(description="Lista de beneficios y/o prestaciones")
    descripcion: str = Field(description="Descripcion general del puesto de trabajo")
    funciones: list[str] = Field(description="Lista de funciones y responsabilidades del puesto de trabajo")
    requisitos_obligatorios: list[str] = Field(description="Lista de requisitos obligatorios solicitados")
    requisitos_deseables: list[str] = Field(description="Lista de requisitos deseables")
    modalidad: str = Field(description="modalidad del puesto de trabajo (Remoto, Híbrido o Presencial)")