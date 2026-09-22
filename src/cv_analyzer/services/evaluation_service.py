"""
Descripción:   Script para la evaluacion del candidato al puesto de trabajo
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

import pandas as pd
from langchain_core.documents import Document
from tqdm import tqdm

from cv_analyzer.services.pdf_processor import extraer_texto_pdf
from cv_analyzer.services.pt_extractor import extraer_pt
from cv_analyzer.services.cv_extractor import extraer_cv
from cv_analyzer.services.evaluator import evaluar_candidato
from cv_analyzer.services.web_scrapper import extraer_texto_url


def evaluar(url: str, cv_path: str):

    with tqdm(total=4, desc="Evaluando candidato", unit="paso") as pbar:

        # Iniciamos extrayendo el texto de url
        pbar.set_description("Extrayendo texto del puesto")
        texto_pt_raw = extraer_texto_url(url)
        pbar.update(1)

        # Procesamos el puesto de trabajo
        pbar.set_description("Procesando descripción del puesto")
        texto_pt = extraer_pt(texto_pt_raw)
        texto_pt_json = texto_pt.model_dump_json()
        pbar.update(1)

        objeto_doc = Document(
            page_content=texto_pt_json,
            metadata={
                "source": url,
                "plataforma": url.lower()
                .split("//")[-1]
                .split("/")[0]
                .replace("www.", ""),
                "procesado": pd.Timestamp.now(),
            },
        )

        # Obtenemos el texto del cv
        pbar.set_description("Procesando CV")
        texto_cv = extraer_cv(extraer_texto_pdf(cv_path))
        texto_cv_json = texto_cv.model_dump_json()
        pbar.update(1)

        # Realizamos la evaluacion
        pbar.set_description("Evaluando candidato")
        evaluacion = evaluar_candidato(texto_cv_json, texto_pt_json)
        pbar.update(1)

    return texto_cv, texto_pt, evaluacion
