#!/usr/bin/env python
#ref https://docs.python.org/2/library/email-examples.html

import smtplib

from email.mime.text import MIMEText

msg = MIMEText("hello this is mail.")
fo="wuminfajoy@gmail.com"
to="wuminfajoy@gmail.com"

msg['Subject'] = 'hello subject.' 
msg['From'] = fo
msg['To'] = to

s = smtplib.SMTP('localhost')
s.sendmail(fo, [to], msg.as_string())
s.quit()
