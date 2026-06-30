"""
Descripción:   Script para la creacion de la clase para envio de correos
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

import os
from email_automation import EmailManager
from dotenv import load_dotenv


load_dotenv()
cuenta = os.environ.get("CUENTA")
password = os.environ.get("PASSWORD")


email = EmailManager(cuenta, password, smtp_server="smtp.gmail.com")



