"""
Description:   Genera un reporte de seguimiento de oportunidades laborales basado en el análisis del CV del candidato y la resultado correspondiente.
Author:        David Jiménez Cooper - SpiderCoop
Date:          2026-09-21
"""

from cv_analyzer.states.alignment_state import AlignmentState


def crear_reporte_oportunidad_laboral(resultado: AlignmentState) -> str:
    """
    Genera un cuerpo de correo enfocado en la resultado para el seguimiento de oportunidades.
    Muestra detalles exhaustivos del puesto y solo métricas clave de compatibilidad del candidato.
    """
    # 1. Lógica de Ajuste y Semáforo de Compatibilidad
    if resultado.get("porcentaje_ajuste") >= 80:
        color, nivel_adj, mensaje, metric_color = (
            "🟢",
            "EXCELENTE OPCIÓN",
            "Alta probabilidad de éxito. ¡Postúlate!",
            "#28a745",
        )
        rec_style = (
            "background-color: #d4edda; color: #155724; border-left: 5px solid #28a745;"
        )
        rec_titulo = "🎯 ESTRATEGIA: POSTULACIÓN PRIORITARIA"
        rec_texto = "Tu perfil cubre los pilares del puesto. Ajusta los detalles sugeridos abajo y envía tu CV de inmediato."
    elif resultado.get("porcentaje_ajuste") >= 60:
        color, nivel_adj, mensaje, metric_color = (
            "🟡",
            "BUENA OPCIÓN",
            "Compatible, requiere énfasis en tus fortalezas.",
            "#ffc107",
        )
        rec_style = (
            "background-color: #fff3cd; color: #856404; border-left: 5px solid #ffc107;"
        )
        rec_titulo = "⚠️ ESTRATEGIA: ADAPTACIÓN DE CV"
        rec_texto = "Cuentas con la base necesaria. Es indispensable reestructurar tu CV para resaltar las habilidades solicitadas antes de aplicar."
    else:
        color, nivel_adj, mensaje, metric_color = (
            "🔴",
            "COMPATIBILIDAD BAJA",
            "Brecha técnica alta o cambio de rumbo.",
            "#dc3545",
        )
        rec_style = (
            "background-color: #f8d7da; color: #721c24; border-left: 5px solid #dc3545;"
        )
        rec_titulo = "❌ ESTRATEGIA: EVALUAR DETENIDAMENTE"
        rec_texto = "El puesto demanda requisitos que no están visibles en tu perfil actual. Evalúa si vale la pena el esfuerzo de adaptación."

    salario_texto = (
        f"${resultado.get('salario_puesto'):,}"
        if resultado.get("salario_puesto") > 0
        else "No especificado"
    )

    # 2. Construcción del HTML
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; color: #333333; line-height: 1.6; max-width: 700px; margin: 0 auto; padding: 20px; }}
            h2 {{ color: #1e1e1e; border-bottom: 2px solid #e6e9ef; padding-bottom: 6px; margin-top: 25px; font-size: 18px; }}
            h3 {{ margin-bottom: 5px; color: #444; font-size: 15px; }}
            ul, ol {{ padding-left: 20px; margin-top: 5px; margin-bottom: 5px; font-size: 14px; }}
            li {{ margin-bottom: 4px; }}
            .divider {{ border: 0; height: 1px; background: #e6e9ef; margin: 20px 0; }}
            .metric-box {{ text-align: center; background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #e6e9ef; margin-bottom: 20px; }}
            .resultado-box {{ background-color: #f4f6f9; border-left: 4px solid #1d80dc; padding: 12px; margin-bottom: 10px; border-radius: 4px; font-size: 14px; }}
            .alert-box {{ padding: 15px; border-radius: 4px; margin-top: 15px; font-weight: bold; font-size: 14px; }}
            .col-table {{ width: 100%; border-collapse: collapse; }}
            .col-td {{ width: 50%; vertical-align: top; padding-right: 10px; }}
        </style>
    </head>
    <body>
        <h1>🔍 Análisis de Oportunidad: {resultado.get("puesto")}</h1>
        <p>Reporte de viabilidad generado para evaluar la posición en <b>{resultado.get("empresa")}</b>.</p>
        <p>Enlace a la vacante: <a href="{resultado.get("puesto_url")}">{resultado.get("puesto")}</a></p>
        
        <!-- ================= COMPATIBILIDAD COYUNTURAL ================= -->
        <div class="metric-box">
            <span style="font-size: 12px; color: #666; text-transform: uppercase; font-weight: bold;">Tu Ajuste con la resultado</span>
            <div style="font-size: 38px; font-weight: bold; color: {metric_color}; margin: 2px 0;">{resultado.get("porcentaje_ajuste")}%</div>
            <div style="font-size: 15px; font-weight: bold;">{color} {nivel_adj}</div>
            <p style="margin: 3px 0 0 0; color: #666; font-size: 13px;">{mensaje}</p>
        </div>

        <div class="alert-box" style="{rec_style}">
            <div style="margin-bottom: 4px;">{rec_titulo}</div>
            <span style="font-weight: normal;">{rec_texto}</span>
        </div>

       <h3>📝 Justificación de la evaluación:</h3>
        <p style="font-size: 14px; background-color: #fafafa; padding: 12px; border: 1px solid #eee; border-radius: 4px; margin-top:5px;">
            {resultado.get("justificacion")}
        </p>

        <div class="divider"></div>

        <!-- ================= DETALLES DEL PUESTO ================= -->
        <h2>📌 Datos Clave de la resultado</h2>
        <table class="col-table">
            <tr>
                <td class="col-td">
                    <div class="resultado-box"><b>🏢 Empresa:</b> {resultado.get("empresa")}</div>
                    <div class="resultado-box"><b>🌍 Modalidad:</b> {resultado.get("modalidad_puesto")}</div>
                </td>
                <td class="col-td">
                    <div class="resultado-box"><b>📈 Nivel:</b> {resultado.get("nivel_puesto").capitalize()}</div>
                    <div class="resultado-box"><b>💰 Salario Ofrecido:</b> {salario_texto}</div>
                </td>
            </tr>
        </table>

        <h3>📝 Descripción de la Oferta:</h3>
        <p style="font-size: 14px; background-color: #fafafa; padding: 12px; border: 1px solid #eee; border-radius: 4px; margin-top:5px;">
            {resultado.get("descripcion_puesto")}
        </p>

        <!-- Funciones y Responsabilidades -->
        <h3>🎯 Funciones Principales del Rol:</h3>
        <ul>
    """
    for funcion in resultado.get("funciones_puesto"):
        html += f"<li>{funcion}</li>"

    html += """
        </ul>

        <div class="divider"></div>

        <!-- ================= REQUISITOS FILTRADOS ================= -->
        <h2>📋 Perfil Técnico y Requisitos</h2>
        <table class="col-table">
            <tr>
                <td class="col-td">
                    <h3 style="color: #c92a2a;">🔴 Obligatorios:</h3>
                    <ul>
    """
    for req in resultado.get("requisitos_obligatorios"):
        html += f"<li>{req}</li>"

    html += """
                    </ul>
                </td>
                <td class="col-td">
                    <h3 style="color: #2b8a3e;">🟢 Deseables / Plus:</h3>
                    <ul>
    """
    for deseable in resultado.get("requisitos_deseables"):
        html += f"<li>{deseable}</li>"

    html += """
                    </ul>
                </td>
            </tr>
        </table>

        <!-- Beneficios -->
        <h3>🎁 Beneficios y Prestaciones:</h3>
        <ul>
    """
    if resultado.get("beneficios"):
        for beneficio in resultado.get("beneficios"):
            html += f"<li>{beneficio}</li>"
    else:
        html += "<li>No especificados en la publicación.</li>"

    html += """
        </ul>

        <div class="divider"></div>

        <!-- ================= ESTRATEGIA DE POSTULACIÓN ================= -->
        <h2>🛠️ Plan de Acción para tu CV</h2>
        <table class="col-table">
            <tr>
                <td class="col-td">
                    <h3 style="color: #1d80dc;">💪 Tus Fortalezas para este Rol:</h3>
                    <ol>
    """
    if resultado.get("fortalezas"):
        for fortaleza in resultado.get("fortalezas"):
            html += f"<li>{fortaleza}</li>"
    else:
        html += "<li>Sin fortalezas claras detectadas en el texto actual.</li>"

    html += """
                    </ol>
                </td>
                <td class="col-td">
                    <h3 style="color: #e67e22;">💡 Sugerencias y areas de mejora:</h3>
                    <ol>
    """

    if resultado.get("areas_mejora"):
        for rec in resultado.get("areas_mejora"):
            html += f"<li>{rec}</li>"
    else:
        html += "<li>No se requieren cambios críticos adicionales.</li>"

    html += """
                    </ol>
                </td>
            </tr>
        </table>

        <p style="margin-top: 35px; font-size: 11px; color: #999; text-align: center;">Reporte de optimización de perfil generado para uso personal.</p>
    </body>
    </html>
    """
    return html
