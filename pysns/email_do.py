import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'mrcoder@qq.com'
email_password = ''
email_send = 'zhxhcoder@qq.com'

subject = 'subjec11t'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body, 'plain'))

filename = 'QR.png'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
# server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)

server.quit()
