import os
from dotenv import load_dotenv
load_dotenv()  # Carga las variables de entorno desde el archivo .env


# --- CONFIGURACIÓN DE MODELOS ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemma-4-31b-it")  # Modelo de LLM por defecto
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "text-embedding-004")  # Modelo de embeddings por defecto


# --- CONFIGURACIÓN DE CORREO ---
CUENTA = os.environ.get("CUENTA")
PASSWORD = os.environ.get("PASSWORD")
RECIPIENTS = os.environ.get("RECIPIENTS")


# --- CONFIGURACIÓN RUTAS ---
url = os.environ.get('url')
cv_path = "data/CV David Jimenez Cooper 2026 En.pdf"


# --- CONFIGURACIÓN DE POSTGRESQL + PGVECTOR ---
USUARIO = "postgres"
POSTGRESQL_PASSWORD = "tu_password_aqui"
HOST = "localhost"
PORT = "5432"
DB_NAME = "tu_base_datos"
COLLECTION_NAME = "puestos_trabajo"  # Nombre de la tabla/colección dentro de pgvector

# Cadena de conexión usando el driver psycopg (v3)
CONNECTION_STRING = f"postgresql+psycopg://{USUARIO}:{POSTGRESQL_PASSWORD}@{HOST}:{PORT}/{DB_NAME}"