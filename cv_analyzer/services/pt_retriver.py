"""
Descripción:   Script para la recuperacion de los puestos de trabajo mas relevantes en PGVector
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-07-04
"""


from langchain_postgres import PGVector
from langchain_core.retrievers import MultiQueryRetriever

from cv_analyzer.services.llm import embeddings, llm_model
from cv_analyzer.services.config import *


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