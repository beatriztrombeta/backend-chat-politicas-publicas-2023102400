import smtplib
from email.mime.text import MIMEText
from app.config import settings

def send_verification_email(email: str, code: str):
    msg = MIMEText(f"Seu código de verificação é: {code}")
    msg["Subject"] = "Código de verificação"
    msg["From"] = settings.SMTP_USER
    msg["To"] = email

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)
