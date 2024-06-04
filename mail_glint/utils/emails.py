import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string

from config.settings.base import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST


def send_verification_email(uuid, email, language="en"):

    context = {
        'email': email,
        'uuid': uuid
    }

    if language == "en":
        subject = 'Verify Your Email Address'
        html_content = render_to_string('verify-email.html', context)

    smtp_server = EMAIL_HOST
    smtp_port = 587
    smtp_user = EMAIL_HOST_USER
    smtp_password = EMAIL_HOST_PASSWORD

    # MIMEText 객체 생성
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email
    msg['Subject'] = subject

    # 이메일 본문 추가
    msg.attach(MIMEText(html_content, 'html'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # TLS 보안 시작
    server.login(smtp_user, smtp_password)  # SMTP 서버에 로그인
    server.sendmail(smtp_user, email, msg.as_string())  # 이메일 발송
