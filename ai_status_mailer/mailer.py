import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to_emails):
    sender = os.getenv("EMAIL_ADDRESS")          # ✅ Gmail address
    app_password = os.getenv("EMAIL_APP_PASSWORD")  # ✅ Gmail App Password

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, app_password)   # ✅ App password
            server.send_message(msg)

        print("✅ Email sent successfully via Gmail!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")
