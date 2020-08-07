import configparser
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_send, subject, filename, body):
    print("邮件发送中...")

    config = configparser.ConfigParser()
    config.read("../config.ini")

    email_user = 'mrcoder@qq.com'
    email_password = config.get('EMAIL', 'email_password')

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    # 附件
    if filename is not None:
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)

    # 内容
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    # server.starttls()
    server.login(email_user, email_password)
    server.sendmail(email_user, email_send, text)
    server.quit()
    print("发送成功")


if __name__ == "__main__":
    send_email('zhxhcoder@qq.com', 'Python发送邮件', 'QR.png', '内容-这是远程发来的邮件，请注意接收并查收附件')
