import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMTPServer:
    def __init__(self, host, port, email, password):
        self.host = host,
        self.port = port,
        self.email = email
        self.password = password
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password)
    
    def send_email(this, subject, content, email):
        message = MIMEMultipart()
        message['From'] = os.environ.get()
        message['Subject'] = subject
        message.attach(MIMEText(content, 'html'))
        message['To'] = email
        
        this.server.sendmail(message['From'], message['To'], message.as_string())

smtp_server = SMTPServer(
    os.environ.get('SMTP_HOST'),
    os.environ.get('SMTP_PORT'),
    os.environ.get('SMTP_EMAIL'),
    os.environ.get('SMTP_PASSWORD')
)
