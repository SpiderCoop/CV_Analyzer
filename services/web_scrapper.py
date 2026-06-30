"""
Descripción:   Script para leer datos de urls y extraer texto de forma robusta
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

import json
import re
from typing import Any

import requests
from bs4 import BeautifulSoup, Comment

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
}


def _normalize_text(text: str) -> str:
    text = text.replace('\r', ' ')
    text = re.sub(r'\s+', ' ', text)
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]
    return '\n'.join(lines)


def _collect_text_from_json(value: Any, partes: list[str]) -> None:
    if isinstance(value, str):
        texto = value.strip()
        if texto:
            partes.append(texto)
    elif isinstance(value, dict):
        for val in value.values():
            _collect_text_from_json(val, partes)
    elif isinstance(value, list):
        for item in value:
            _collect_text_from_json(item, partes)


def _extract_text_from_json_ld(soup: BeautifulSoup) -> str:
    partes: list[str] = []
    for script in soup.find_all('script', type='application/ld+json'):
        if not script.string:
            continue

        payload_text = script.string.strip()
        try:
            payload = json.loads(payload_text)
        except json.JSONDecodeError:
            match = re.search(r'({.*})', payload_text, re.S)
            if not match:
                continue
            try:
                payload = json.loads(match.group(1))
            except json.JSONDecodeError:
                continue

        documentos = payload if isinstance(payload, list) else [payload]
        for documento in documentos:
            _collect_text_from_json(documento, partes)

    única = []
    for parte in partes:
        texto = _normalize_text(parte)
        if texto and texto not in única:
            única.append(texto)
    return '\n\n'.join(única)


def _extract_text_from_meta(soup: BeautifulSoup) -> str:
    partes: list[str] = []
    if soup.title and soup.title.string:
        partes.append(soup.title.string.strip())

    propiedades = [
        'og:title',
        'og:description',
        'twitter:title',
        'twitter:description',
        'description',
    ]
    for prop in propiedades:
        meta = soup.find('meta', property=prop) or soup.find('meta', attrs={'name': prop})
        if meta and meta.get('content'):
            partes.append(meta['content'].strip())

    única = []
    for parte in partes:
        if parte and parte not in única:
            única.append(parte)
    return '\n\n'.join(única)


def _extract_text_from_itemprops(soup: BeautifulSoup) -> str:
    partes: list[str] = []
    for tag in soup.find_all(attrs={'itemprop': True}):
        texto = tag.get_text(separator=' ', strip=True)
        if texto:
            partes.append(texto)
        for attr in ('content', 'alt', 'title', 'aria-label', 'placeholder'):
            if tag.has_attr(attr):
                contenido = str(tag[attr]).strip()
                if contenido:
                    partes.append(contenido)

    única = []
    for parte in partes:
        if parte and parte not in única:
            única.append(parte)
    return '\n\n'.join(única)


def _extract_text_from_attributes(soup: BeautifulSoup) -> str:
    partes: list[str] = []
    for tag in soup.find_all(attrs=True):
        for attr in ('alt', 'title', 'aria-label', 'placeholder'):
            if tag.has_attr(attr):
                contenido = str(tag[attr]).strip()
                if contenido:
                    partes.append(contenido)

    única = []
    for parte in partes:
        if parte and parte not in única:
            única.append(parte)
    return '\n\n'.join(única)


def _extract_visible_text(soup: BeautifulSoup) -> str:
    for tag in soup(['script', 'style', 'iframe', 'svg', 'noscript']):
        tag.extract()
    for comment in soup.find_all(string=lambda texto: isinstance(texto, Comment)):
        comment.extract()
    texto = soup.get_text(separator=' ')
    return _normalize_text(texto)


def extraer_texto_url(url: str) -> str:
    try:
        session = requests.Session()
        session.headers.update(DEFAULT_HEADERS)
        respuesta = session.get(url, timeout=20, allow_redirects=True)
        if respuesta.status_code != 200:
            return f"Error al acceder a la página. Código de estado: {respuesta.status_code}"

        respuesta.encoding = respuesta.apparent_encoding or 'utf-8'
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        partes: list[str] = []
        for extractor in (
            _extract_text_from_meta,
            _extract_text_from_json_ld,
            _extract_text_from_itemprops,
            _extract_text_from_attributes,
        ):
            texto = extractor(soup)
            if texto:
                partes.append(texto)

        visible_soup = BeautifulSoup(respuesta.text, 'html.parser')
        texto_visible = _extract_visible_text(visible_soup)
        if texto_visible:
            partes.append(texto_visible)

        if partes:
            return _normalize_text('\n\n'.join(partes))

        return "No se encontró texto extraíble en la página."
    except requests.RequestException as e:
        return f"Ocurrió un error de red: {e}"
    except Exception as e:
        return f"Ocurrió un error: {e}"


if __name__ == "__main__":
    url_objetivo = "https://example.com"
    resultado = extraer_texto_url(url_objetivo)
    print(resultado)
