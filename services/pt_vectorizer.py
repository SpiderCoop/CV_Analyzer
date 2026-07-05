"""
Descripción:   Script para la vectorizacion de puesto de trabajo y almacenamiento
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-07-04
"""
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

# Configurar credenciales
os.environ["GOOGLE_API_KEY"] = "TU_API_KEY_AQUI"

# 1. Instanciar el modelo de embeddings de Gemini
embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")

# 2. Tu base extensa de puestos de trabajo (Simulación de registros existentes)
base_puestos = [
    "Data Scientist: Modelos predictivos, Machine Learning, Python, SQL y desarrollo de pipelines RAG.",
    "Quantitative Analyst: Econometría, optimización de portafolios, valoración de derivados, Python y VBA.",
    "Cloud Data Engineer: Administración de bases de datos AWS RDS, ETL con Lambda, PostgreSQL y S3.",
    "Frontend Developer: Creación de interfaces de usuario, React, TypeScript, Tailwind CSS y Next.js."
]

# --- CONFIGURACIÓN DE POSTGRESQL + PGVECTOR ---
# Modifica estos datos con las credenciales de tu base de datos real
USUARIO = "postgres"
PASSWORD = "tu_password_aqui"
HOST = "localhost"
PORT = "5432"
DB_NAME = "tu_base_datos"

# Cadena de conexión usando el driver psycopg (v3)
CONNECTION_STRING = f"postgresql+psycopg://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
COLLECTION_NAME = "puestos_trabajo"  # Nombre de la tabla/colección dentro de pgvector


# 3. Crear el índice vectorial e insertar los datos en PostgreSQL
# Nota: `.from_texts` creará automáticamente las tablas necesarias si no existen.
vector_store = PGVector.from_texts(
    texts=base_puestos,
    embedding=embeddings,
    connection=CONNECTION_STRING,
    collection_name=COLLECTION_NAME,
    use_jsonb=True # Guarda metadatos en formato JSONB de forma eficiente
)

# A PARTIR DE AQUÍ EL FLUJO DE PRODUCCIÓN ES IGUAL:
# Si en ejecuciones futuras YA tienes los datos cargados en la base de datos y solo quieres consultar,
# en lugar de usar `.from_texts()`, simplemente inicializas el objeto así:
# vector_store = PGVector(
#     connection=CONNECTION_STRING,
#     collection_name=COLLECTION_NAME,
#     embeddings=embeddings
# )

# 4. El perfil consolidado ("Puesto Ideal") generado para el aplicante
puesto_ideal_aplicante = "Rol enfocado en finanzas cuantitativas, análisis econométrico de series de tiempo y automatización con Python."

# 5. Ejecutar la búsqueda de similitud (Traer los 2 más cercanos)
# Por defecto, LangChain con pgvector calcula la distancia del coseno (o L2 dependiendo de la configuración interna).
resultados = vector_store.similarity_search_with_score(puesto_ideal_aplicante, k=2)

# 6. Mostrar resultados
print("--- PUESTOS MÁS RELEVANTES ENCONTRADOS EN PGVECTOR ---")
for doc, score in resultados:
    # El score representa la distancia; dependiendo de la métrica, valores más bajos o cercanos a cero indican mayor similitud.
    print(f"\n[Match] Puesto: {doc.page_content}\n[Distancia/Score]: {score:.4f}")