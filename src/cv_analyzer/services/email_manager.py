"""
Descripción:   Script para la creacion de la clase para envio de correos
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from email_automation import EmailManager

from config import CUENTA, PASSWORD

email = EmailManager(CUENTA, PASSWORD, smtp_server="smtp.gmail.com")
