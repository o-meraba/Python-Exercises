import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def sending_mail(mail_address, mail_subject, mail_text):
    message = MIMEMultipart()
    message['From'] = "voyager.maker@gmail.com"
    message['To'] = mail_address
    message["Subject"] = mail_subject
    message_text = mail_text
    message_body = MIMEText(message_text,"plain")
    message.attach(message_body)

    try:
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("voyager.maker@gmail.com","test21deneme")
        mail.sendmail(message["From"],message["to"],message.as_string())
        print("Mail sending is successful")
        mail.close()
    except:
        sys.stderr.write("Mail sending is fail")
        sys.stderr.flush()

def main_func():
    mail_address = input("Please enter receiver mail address: ")
    mail_subject = input("Please enter mail subject: ")
    mail_text = input("Please enter mail text: ")
    sending_mail(mail_address,mail_subject,mail_text)

#main_func()