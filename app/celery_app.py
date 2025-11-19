from celery import Celery
from dotenv import load_dotenv
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Load .env
load_dotenv()

# RabbitMQ broker URL
broker_url = 'amqp://guest:guest@localhost:5672//'

celery_app = Celery('tasks', broker=broker_url)

@celery_app.task
def send_email_task(to_email):
    msg = EmailMessage()
    msg.set_content('This is a test email from your messaging system from venkat.')
    msg['Subject'] = 'Test Email'
    msg['From'] = os.getenv('EMAIL_USER')
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        smtp.send_message(msg)
    return f'Email sent to {to_email}'

@celery_app.task
def log_time_task():
    with open('logs/app.log', 'a') as f:
        f.write(f'{datetime.now()}\n')
    return 'Time logged'

