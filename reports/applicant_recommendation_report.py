
from models.cv_model import AnalisisCV
from models.pt_model import PuestoTrabajo



def correo_recomendacion_contratacion(resultado: AnalisisCV, vacante: PuestoTrabajo) -> str:
    """
    Genera el cuerpo del correo en HTML basado en los datos de la vacante 
    y el resultado de la evaluación del CV, incluyendo sugerencias de mejora.
    """
    # 1. Lógica de Evaluación Principal (Métricas y Colores del Candidato)
    if resultado.porcentaje_ajuste >= 80:
        color, nivel_adj, mensaje, metric_color = "🟢", "EXCELENTE", "Candidato altamente recomendado", "#28a745"
    elif resultado.porcentaje_ajuste >= 60:
        color, nivel_adj, mensaje, metric_color = "🟡", "BUENO", "Candidato recomendado con reservas", "#ffc107"
    elif resultado.porcentaje_ajuste >= 40:
        color, nivel_adj, mensaje, metric_color = "🟠", "REGULAR", "Candidato requiere evaluación adicional", "#fd7e14"
    else:
        color, nivel_adj, mensaje, metric_color = "🔴", "BAJO", "Candidato no recomendado", "#dc3545"

    # 2. Lógica de la Recomendación Final (Bloques de Alerta)
    if resultado.porcentaje_ajuste >= 70:
        rec_style = "background-color: #d4edda; color: #155724; border-left: 5px solid #28a745;"
        rec_titulo = "✅ CANDIDATO RECOMENDADO"
        rec_texto = "El perfil del candidato está bien alineado con los requisitos del puesto. Se recomienda proceder con las siguientes etapas del proceso de selección."
    elif resultado.porcentaje_ajuste >= 50:
        rec_style = "background-color: #fff3cd; color: #856404; border-left: 5px solid #ffc107;"
        rec_titulo = "⚠️ CANDIDATO CON POTENCIAL"
        rec_texto = "El candidato muestra potencial pero requiere evaluación adicional. Se recomienda una entrevista técnica para validar competencias específicas."
    else:
        rec_style = "background-color: #f8d7da; color: #721c24; border-left: 5px solid #dc3545;"
        rec_titulo = "❌ CANDIDATO NO RECOMENDADO"
        rec_texto = "El perfil no se alinea suficientemente con los requisitos del puesto. Se recomienda continuar la búsqueda de candidatos más adecuados."

    # Formateo del salario de la vacante
    salario_texto = f"${vacante.salario:,}" if vacante.salario > 0 else "No especificado"

    # 3. Construcción del HTML
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; color: #333333; line-height: 1.6; max-width: 700px; margin: 0 auto; padding: 20px; }}
            h2 {{ color: #1e1e1e; border-bottom: 2px solid #f0f2f6; padding-bottom: 8px; margin-top: 30px; }}
            h3 {{ margin-bottom: 5px; color: #444; }}
            .divider {{ border: 0; height: 1px; background: #f0f2f6; margin: 20px 0; }}
            .metric-box {{ text-align: center; background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid #e6e9ef; }}
            .info-box {{ background-color: #e8f4fd; border-left: 4px solid #1d80dc; padding: 12px; margin-bottom: 10px; border-radius: 4px; font-size: 14px; }}
            .vacante-box {{ background-color: #f4f6f9; border-left: 4px solid #6c757d; padding: 12px; margin-bottom: 10px; border-radius: 4px; font-size: 14px; }}
            .skill-badge {{ display: inline-block; background-color: #d4edda; color: #155724; padding: 5px 10px; margin: 4px; border-radius: 4px; font-size: 14px; }}
            .alert-box {{ padding: 15px; border-radius: 4px; margin-top: 15px; font-weight: bold; }}
            .col-table {{ width: 100%; border-collapse: collapse; margin-bottom: 10px; }}
            .col-td {{ width: 50%; vertical-align: top; padding: 0 10px 0 0; }}
        </style>
    </head>
    <body>
        <h1>📄 Reporte de Evaluación de Candidato</h1>
        <p>Estimado equipo, se adjunta el análisis de compatibilidad del candidato frente a la siguiente posición activa:</p>
        
        <h2>📌 Detalles de la Vacante</h2>
        <table class="col-table">
            <tr>
                <td class="col-td">
                    <div class="vacante-box"><b>🏢 Empresa:</b> {vacante.empresa}</div>
                    <div class="vacante-box"><b>💼 Puesto:</b> {vacante.puesto}</div>
                    <div class="vacante-box"><b>🌍 Modalidad:</b> {vacante.modalidad}</div>
                </td>
                <td class="col-td">
                    <div class="vacante-box"><b>📈 Nivel:</b> {vacante.nivel.capitalize()}</div>
                    <div class="vacante-box"><b>💰 Salario:</b> {salario_texto}</div>
                </td>
            </tr>
        </table>
        
        <h3>📝 Descripción General del Puesto</h3>
        <p style="font-size: 14px; background-color: #fafafa; padding: 10px; border: 1px solid #eee; border-radius: 4px;">
            {vacante.descripcion}
        </p>

        <div class="divider"></div>

        <h2>📊 Resultado del Análisis</h2>
        
        <div class="metric-box">
            <span style="font-size: 14px; color: #555; text-transform: uppercase; font-weight: bold;">Porcentaje de Ajuste al Puesto</span>
            <div style="font-size: 42px; font-weight: bold; color: {metric_color}; margin: 5px 0;">{resultado.porcentaje_ajuste}%</div>
            <div style="font-size: 16px; font-weight: bold;">{color} {nivel_adj}</div>
            <p style="margin: 5px 0 0 0; color: #555;">{mensaje}</p>
        </div>

        <h3>👤 Perfil del Candidato</h3>
        <table class="col-table">
            <tr>
                <td class="col-td">
                    <div class="info-box"><b>👨‍💼 Nombre:</b> {resultado.nombre_candidato}</div>
                    <div class="info-box"><b>⏱️ Experiencia:</b> {resultado.experiencia_años} años</div>
                </td>
                <td class="col-td">
                    <div class="info-box"><b>🎓 Educación:</b> {resultado.education}</div>
                </td>
            </tr>
        </table>

        <h3>💼 Experiencia Relevante del Candidato</h3>
        <div class="info-box" style="background-color: #f8f9fa; border-left: 4px solid #6c757d; color: #333;">
            {resultado.experiencia_relevante.replace('\n', '<br>')}
        </div>

        <div class="divider"></div>

        <h2>🛠️ Habilidades Técnicas Identificadas</h2>
    """

    if resultado.habilidades_clave:
        for habilidad in resultado.habilidades_clave:
            html += f'<span class="skill-badge">✅ {habilidad}</span>'
    else:
        html += '<p style="color: #856404; background-color: #fff3cd; padding: 10px; border-radius:4px;">No se identificaron habilidades técnicas específicas</p>'

    html += """
        <div class="divider"></div>

        <table class="col-table">
            <tr>
                <td class="col-td">
                    <h2>💪 Fortalezas Principales</h2>
    """
    
    if resultado.fortalezas:
        html += "<ol style='padding-left: 20px; margin-top:0;'>"
        for fortaleza in resultado.fortalezas:
            html += f"<li>{fortaleza}</li>"
        html += "</ol>"
    else:
        html += "<p>No se identificaron fortalezas específicas</p>"

    html += """
                </td>
                <td class="col-td">
                    <h2>📈 Áreas de Desarrollo</h2>
    """
    
    if resultado.areas_mejora:
        html += "<ol style='padding-left: 20px; margin-top:0;'>"
        for area in resultado.areas_mejora:
            html += f"<li>{area}</li>"
        html += "</ol>"
    else:
        html += "<p>No se identificaron áreas de mejora específicas</p>"

    html += f"""
                </td>
            </tr>
        </table>

        <div class="divider"></div>

        <h2>📋 Recomendación Final</h2>
        <div class="alert-box" style="{rec_style}">
            <div style="margin-bottom: 8px;">{rec_titulo}</div>
            <span style="font-weight: normal; font-size: 15px;">{rec_texto}</span>
        </div>
    """

    # ================= SECCIÓN NUEVA: RECOMENDACIONES DE MEJORA =================
    html += """
        <div class="divider"></div>
        <h2>💡 Sugerencias para Resaltar la Candidatura</h2>
    """
    
    if hasattr(resultado, 'recomendaciones') and resultado.recomendaciones:
        html += "<ul style='padding-left: 20px; color: #444;'>"
        for recomendacion in resultado.recomendaciones:
            html += f"<li style='margin-bottom: 6px;'>{recomendacion}</li>"
        html += "</ul>"
    else:
        html += "<p style='color: #6c757d; font-style: italic;'>No se generaron recomendaciones adicionales para este perfil.</p>"

    # Cierre del archivo HTML
    html += """
        <p style="margin-top: 30px; font-size: 13px; color: #777;">Este es un reporte automatizado generado por el pipeline de evaluación de IA.</p>
    </body>
    </html>
    """
    return html