import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = 'mrcoder@qq.com'
email_password = ''
email_send = 'zhxhcoder@qq.com'

# 主题
subject = '主题-这是Python发送的邮件'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

# 附件
filename = 'QR.png'
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)

# 内容
body = '内容-这是远程发来的邮件，请注意接收并查收附件' + filename
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
# server.starttls()
server.login(email_user, email_password)
print("邮件发送...")
server.sendmail(email_user, email_send, text)
print("发送成功")
server.quit()
