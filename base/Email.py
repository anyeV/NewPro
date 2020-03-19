import smtplib
import email.mime.multipart
import email.mime.text

_config = {'host': '',  # 发邮件服务器
           'sender': '',  # 发件人
           'password': '',  # 第三方客户端授权密码
           'receiver': '',  # 收件人
           }


def send_email(mail_subject, mail_content, email_config=_config):
    '''
    :param mail_subject: 邮件标题
    :param mail_content: 邮件内容
    :param email_config: 邮箱相关信息配置
    :return:
    '''
    host = email_config['host']
    sender = email_config['sender']
    password = email_config['password']
    receiver = email_config['receiver']

    msg = email.mime.multipart.MIMEMultipart()

    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = receiver

    # 发送html格式会丢失css样式，尚未找到解决办法
    txt = email.mime.text.MIMEText(mail_content, 'html')
    msg.attach(txt)

    # 3.7的SMTP_SSL需要给个参数server_host，否则会报错哦
    smtp_server = smtplib.SMTP_SSL(host)
    smtp_server.connect(host, 465)
    # 登录
    smtp_server.login(sender, password)
    # 发送邮件
    smtp_server.sendmail(sender, receiver, msg.as_string())
    # 退出
    smtp_server.quit()
    print("邮件发送成功")


if __name__ == "__main__":
    subject = "嘿嘿嘿"
    with open("test_report_20200319_19_32_35.html", "r", encoding="utf-8") as f:
        content = f.read()

    send_email(subject, content)
