"""
Descripción:   Script para la recuperacion de los puestos de trabajo mas relevantes en PGVector
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-07-04
"""
import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from langchain_core.retrievers import MultiQueryRetriever

# 1. Configurar credenciales y modelo de embeddings
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Falta la clave de API de Google. Define GOOGLE_API_KEY en el entorno.")


llm_model = ChatGoogleGenerativeAI(model="gemma-4-31b-it",
                                     temperature=0.2,
                                     api_key=api_key,
    )


embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")



# 2. Parámetros de conexión a tu base de datos existente
USUARIO = "postgres"
PASSWORD = "tu_password_aqui"
HOST = "localhost"
PORT = "5432"
DB_NAME = "tu_base_datos"
COLLECTION_NAME = "puestos_trabajo"

CONNECTION_STRING = f"postgresql+psycopg://{USUARIO}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# 3. Inicializar el Vector Store en modo "Solo Lectura / Consulta"
# Al no usar .from_texts(), pgvector no inserta nada, solo se conecta a la tabla existente.
vector_store = PGVector(
    connection=CONNECTION_STRING,
    collection_name=COLLECTION_NAME,
    embeddings=embeddings
)

# Perfil o query de búsqueda (Puesto ideal del aplicante)
query_aplicante = "Necesito un rol para construir bases de datos orientadas a la nube, pipelines ETL y uso de AWS."


# =====================================================================
# Convertir a un "Retriever" oficial de LangChain (Para pipelines RAG)
# =====================================================================
print("\n--- RECOVERY: USANDO EL RETRIEVER INTERFACE (LCEL) ---")
# Este es el enfoque estándar si vas a conectar este proceso a un LLM o Agente.
# Permite usar estrategias avanzadas como MMR (Maximal Marginal Relevance) para evitar resultados redundantes.
base_retriever = vector_store.as_retriever(
    search_type="similarity", # También puedes usar "mmr"
    search_kwargs={"k": 2}
)

retriever = MultiQueryRetriever.from_llm(base_retriever, llm_model)

# En LangChain, los retrievers se ejecutan usando el método .invoke()
docs_desde_retriever = retriever.invoke(query_aplicante)

for i, doc in enumerate(docs_desde_retriever, 1):
    print(f"Resultado {i} del Retriever: {doc.page_content}")