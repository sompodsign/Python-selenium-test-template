import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import datetime
import time
import os
from datetime import datetime


def readWrite(pathOfFile):
    fileToRead = open(pathOfFile, 'r+')
    data = int(fileToRead.read())
    # print(type(data))

    newData = (data + 1)

    fileToRead.seek(0)
    fileToRead.write(str(newData))
    fileToRead.truncate()
    fileToRead.close()

    fileToReadForNewData = open(pathOfFile, 'r')
    readNewDatanum = fileToReadForNewData.read()
    fileToReadForNewData.close()

    return readNewDatanum


def sendMail(rreceiver, htmlPath, pdfPath, mail_content):
    sender = 'Report.DsiDrm@gmail.com'
    receiver = rreceiver
    username = 'Report.DsiDrm@gmail.com'
    password = 'asdfghqwerty#12'

    # Email Subject
    mail_title = 'Subject: Test Report at' + str(datetime.now())

    print("*" * 80)
    # print(PdfPath)
    f = open(htmlPath, 'rb')
    mail_body = "Dear Sir, Here I am sharing the executed test result for the following test cases::-"
    f.close()

    # Mail content, format, encoding
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    message.attach(MIMEText(mail_body))

    # build the attachment
    att1 = MIMEBase('application', 'octet-stream')
    att2 = MIMEBase('application', 'octet-stream')
    att1.set_payload(open(htmlPath, 'rb').read())
    att2.set_payload(open(pdfPath, 'rb').read())

    encoders.encode_base64(att1)
    encoders.encode_base64(att2)
    att1.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(htmlPath))
    att2.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(pdfPath))
    message.attach(att1)
    message.attach(att2)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(sender, receiver, message.as_string())
        print("Send email successfully!!!")
        server.close()

    except:
        print("Failed to send mail!!!")
