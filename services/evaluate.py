"""
Descripción:   Script para la evaluacion del candidato al puesto de trabajo
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""


from tqdm import tqdm

from services.web_scrapper import extraer_texto_url
from services.pdf_processor import extraer_texto_pdf

from services.pt_extractor import extraer_pt
from services.cv_evaluator import evaluar_candidato


def evaluate(url: str, cv_path: str):

    with tqdm(total=4, desc="Evaluando candidato", unit="paso") as pbar:
        # Iniciamos extrayendo el texto de url
        pbar.set_description("Extrayendo texto del puesto")
        texto_pt_raw = extraer_texto_url(url)
        pbar.update(1)

        pbar.set_description("Procesando descripción del puesto")
        texto_pt = extraer_pt(texto_pt_raw)
        texto_pt_str = texto_pt.model_dump_json()
        pbar.update(1)

        # Obtenemos el texto del cv
        pbar.set_description("Extrayendo texto del CV")
        texto_cv = extraer_texto_pdf(cv_path)
        pbar.update(1)

        # Realizamos la evaluacion
        pbar.set_description("Evaluando candidato")
        evaluacion = evaluar_candidato(texto_cv, texto_pt_str)
        pbar.update(1)

    return texto_pt, evaluacion