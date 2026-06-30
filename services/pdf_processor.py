import fitz

import fitz  # PyMuPDF

def extraer_texto_pdf(archivo_o_ruta, num_pags: int | list = None):
    try:
        # CORRECCIÓN DE RUTA / MEMORIA: Detectar si es un objeto en memoria (bytes) o una ruta string
        if hasattr(archivo_o_ruta, "read"):
            # Si tiene el método .read(), es un archivo en memoria (ej. Streamlit, BytesIO)
            contenido_bytes = archivo_o_ruta.read()
            document = fitz.open(stream=contenido_bytes, filetype="pdf")
        elif isinstance(archivo_o_ruta, bytes):
            # Si pasas los bytes directamente
            document = fitz.open(stream=archivo_o_ruta, filetype="pdf")
        else:
            # Si es un string, asume que es una ruta física en el disco
            document = fitz.open(archivo_o_ruta)
            
        total_pages = document.page_count
        
        # Mapeo de páginas (Conversión base 1 a base 0 interna de fitz)
        if num_pags is None:
            num_pags = list(range(1, total_pages + 1))
        elif not isinstance(num_pags, list):
            num_pags = [num_pags]

        text = ''
        for page_number in num_pags:
            # Validación de rangos para evitar IndexError
            if page_number < 1 or page_number > total_pages:
                raise ValueError(f"El número de página {page_number} está fuera de rango (1 - {total_pages})")
            
            page = document.load_page(page_number - 1)
            texto_pagina = page.get_text()
            
            # Formateo opcional para mantener la estructura visual por página como tu primer código
            if texto_pagina.strip():
                text += f"\n--- PÁGINA {page_number} ---\n"
                text += texto_pagina + "\n"

        text = text.strip()
        document.close()  # Es buena práctica cerrar el documento para liberar memoria en C

        if not text:
            return "Error: El PDF parece estar vacío o contener solo imágenes."
            
        return text

    except Exception as e:
        return f"Error al procesar el archivo PDF con fitz: {str(e)}"