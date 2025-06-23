from email.mime.text import MIMEText
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import json
def send_email():
    sender = os.environ["EMAIL_SENDER"]
    receiver = os.environ["EMAIL_RECEIVER"]
    password = os.environ["EMAIL_PASSWORD"]
    smtp_server = os.environ["SMTP_SERVER"]
    smtp_port = int(os.environ["SMTP_PORT"])

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    
    # Attach the email body as plain text
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver.split(','), msg.as_string())

if __name__ == "__main__":
    try:
       
        subject = "Model Training & Deployment Successful"
        body = (
            f"Model trained and evaluated successfully.\n"
            f"📄 View hosted model at"
            f" https://huggingface.co/danielle2003/normal-session"
                    )

    except Exception as e:
        subject = "Model Training or Deployment Failed"
        body = f"An error occurred:\n{e}"
    send_email()
