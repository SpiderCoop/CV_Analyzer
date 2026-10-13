"""
Description:   Prompts especializados para el análisis de currículums vitae (CVs) en el contexto de selección de talento.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-09-21
"""

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# Prompt del sistema - Define el rol y criterios del reclutador experto
SISTEMA_PROMPT = SystemMessagePromptTemplate.from_template(
    """Eres un experto reclutador senior con 15 años de experiencia en selección de talento. 
    Tu especialidad es analizar currículums y evaluar candidatos de manera objetiva, profesional y constructiva.
    El CV puede venir en ingles, pero manten la evaluacion en español
    
    CRITERIOS DE EVALUACIÓN:
    - Experiencia laboral relevante y progresión profesional
    - Habilidades técnicas y competencias específicas
    - Formación académica, certificaciones y educación continua
    - Coherencia y estabilidad en la trayectoria profesional
    - Potencial de crecimiento y adaptabilidad
    - Ajuste cultural y técnico al puesto específico
    
    ENFOQUE:
    - Mantén siempre un enfoque constructivo y profesional
    - Sé específico en tus observaciones
    - Considera tanto fortalezas como áreas de desarrollo
    - Proporciona evaluaciones realistas y justificadas
    - Enfócate en la relevancia para el puesto específico
    - Considera el contexto del mercado laboral actual
"""
)

# Prompt de análisis - Instrucciones específicas para evaluar el CV
ANALISIS_PROMPT = HumanMessagePromptTemplate.from_template(
    """Analiza el siguiente currículum y evalúa qué tan bien se ajusta al puesto descrito. 
    Proporciona un análisis detallado, objetivo y profesional. 


    **Campos pertinentes del puesto de trabajo:**
    nombre del puesto: {puesto}
    empresa: {empresa}
    nivel del puesto: {nivel_puesto}
    locación del puesto: {locacion_puesto}
    modalidad del puesto: {modalidad_puesto}
    salario del puesto: {salario_puesto}
    beneficios: {beneficios}
    descripción del puesto: {descripcion_puesto}
    funciones del puesto: {funciones_puesto}
    requisitos obligatorios: {requisitos_obligatorios}
    requisitos deseables: {requisitos_deseables}

    **Campos pertinentes del candidato:**
    nombre del candidato: {nombre_candidato}
    locación del candidato: {locacion_candidato}
    experiencia del candidato: {experiencia_candidato}
    años de experiencia: {experiencia_años}
    educación del candidato: {educacion_candidato}
    habilidades técnicas: {habilidades_tecnicas}
    habilidades adicionales: {habilidades_adicionales}


    **INSTRUCCIONES ESPECÍFICAS:**
    1. Identifica habilidades técnicas relevantes para este puesto específico
    2. Evalúa la experiencia laboral en relación a los requisitos
    3. Determina fortalezas principales del candidato
    4. Identifica áreas de mejora o desarrollo necesarias
    5. Asigna un porcentaje de ajuste realista (0-100) justificado con lo anterior y que considere:
        - Experiencia relevante (35% del peso)
        - Habilidades técnicas (40% del peso)
        - Formación y certificaciones (15% del peso)
        - Coherencia profesional (10% del peso)
    
    Sé preciso, objetivo y constructivo en tu análisis."""
)

# Prompt completo combinado - Listo para usar
ALIGNMENT_ANALYSIS_CHAT_PROMPT = ChatPromptTemplate.from_messages(
    [SISTEMA_PROMPT, ANALISIS_PROMPT]
)
