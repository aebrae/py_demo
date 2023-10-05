#!/usr/bin/env python3
""" email definitions for compiling an email with PDF attachement and for sending via SMTP """
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(From,To,subject_line,body,attachment_path):
        message = EmailMessage()
        message['From']    = From
        message['To']      = To
        message['Subject'] = subject_line
        message.set_content(body)
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
                message.add_attachment(ap.read(),
                maintype=mime_type,
                subtype=mime_subtype,
                filename=os.path.basename(attachment_path))
        return message

def generate_error_report(From,To,subject_line,body):
        message = EmailMessage()
        message['From']    = From
        message['To']      = To
        message['Subject'] = subject_line
        message.set_content(body)
        return message

def send_email(message):
        mail_server = smtplib.SMTP_SSL()
        mail_server.send_message(message)
        mail_server.quit()

#source_path = "/home/report.pdf"
#print(generate_email("automation@example.com","aebrae@gmail.com","subject","body",source_path))
#send_email(generate_email("automation@exmaple.com","recipient@gmail.com","subject","body",source_path))
