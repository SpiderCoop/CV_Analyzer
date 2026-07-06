"""
Descripción:   Script para la creacion de la clase para envio de correos
Autor:         David Jiménez Cooper - SpiderCoop
Fecha:         2026-06-29
"""

from email_automation import EmailManager
from cv_analyzer.services.config import *


email = EmailManager(CUENTA, PASSWORD, smtp_server="smtp.gmail.com")



