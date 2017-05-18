# -*- coding: utf-8 -*-

import smtplib

class EmailPropio():
    #Atributos del Email_package
    USR = ''
    PWD = ''
    FROM = ''
    TO = ''
    CC = ''
    SUBJECT = ''
    TEXT = ''
    message = ''

    def __init__(self,usuario,contrasena,ejecutivo,asunto,mensaje):

        self.USR = usuario
        self.PWD = contrasena
        self.FROM = usuario
        self.TO = ejecutivo.email if type(ejecutivo.email) is list else [ejecutivo.email]
        self.CC = ejecutivo.cc if type(ejecutivo.cc) is list else [ejecutivo.cc]
        asunto = str(asunto)
        asunto.encode(encoding='utf-8',errors='strict')
        self.SUBJECT = asunto
        self. TEXT = mensaje

    def enviarEmail(self):

        # Prepare actual message
        self.message = u"""From: %s\nTo: %s\nCc: %s\nSubject: %s\n\n%s
        """ % (self.FROM, ", ".join(self.TO), ", ".join(self.CC), self.SUBJECT, self.TEXT.getMensaje())

#        try:
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.ehlo()
        server.starttls()
        server.login(self.USR, self.PWD)
        server.sendmail(self.FROM, self.TO, self.message)
        server.close()
        print('successfully sent the mail')
#        except:
#            print("failed to send mail")

    def verEmail(self):
        # Prepare actual message
        self.message = """ASR: %s\nPWD: %s\nFrom: %s\nTo: %s\nCc: %s\nSubject: %s\n\n%s
        """ % (self.USR, self.PWD, self.FROM, ", ".join(self.TO), ", ".join(self.CC), self.SUBJECT, self.TEXT.getMensaje())
        print (self.message)

