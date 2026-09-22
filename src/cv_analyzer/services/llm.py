"""
Descripción:   Escribe una breve descripción aquí.
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-07-05
"""

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from config import EMBEDDINGS_MODEL, GOOGLE_API_KEY, LLM_MODEL

llm_model = ChatGoogleGenerativeAI(
    model=LLM_MODEL, temperature=0.2, api_key=GOOGLE_API_KEY
)

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDINGS_MODEL, api_key=GOOGLE_API_KEY
)
