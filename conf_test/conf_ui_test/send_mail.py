
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import datetime
import os
from datetime import datetime


def send_report(receiver_email, htmlPath):
    sender = 'sompodsrkr@gmail.com'
    receiver = receiver_email

    # Email Subject
    mail_title = 'Test Report at' + str(datetime.now())

    print("*" * 80)
    f = open(htmlPath, 'rb')
    mail_body = "Here is the report for the test run at " + str(datetime.now()) + "\n\n"
    f.close()

    # Mail content, format, encoding
    message = MIMEMultipart("alternative")
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    message.attach(MIMEText(mail_body))

    # build the attachment
    att1 = MIMEBase('application', 'octet-stream')
    att1.set_payload(open(htmlPath, 'rb').read())

    encoders.encode_base64(att1)
    att1.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(htmlPath))
    message.attach(att1)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("sompodsrkr@gmail.com", "4423445946644Ss")
        server.sendmail(sender, receiver, message.as_string())
        print("Send email successfully!!!")
        server.close()

    except Exception as e:
        print("Failed to send mail!!!, Error:", e)
