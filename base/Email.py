import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_config = {'host': 'smtp.qq.com',  # 发邮件服务器
           'sender': 'xxxx@qq.com',  # 发件人,任意邮箱此处QQ邮箱举例
           'password': '*******',  # 第三方客户端授权密码
           'receiver': ['xxxx@qq.com', ],  # 收件人
           }


def send_email(mail_subject, mail_content, mail_application=None, mail_config=_config):
    '''
    :param mail_subject: 邮件标题
    :param mail_content: 邮件内容
    :param mail_application: 附件，填写附件url
    :param mail_config: 邮箱相关信息配置
    :return:
    '''
    host = mail_config['host']
    sender = mail_config['sender']
    password = mail_config['password']
    receiver = mail_config['receiver']

    msg = MIMEMultipart()

    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = ','.join(receiver)

    # 发送html格式会丢失css样式，尚未找到解决办法
    txt = MIMEText(mail_content, 'html')
    msg.attach(txt)

    # 附件
    if mail_application:
        if '\\' in mail_application:
            file_name = mail_application.split('\\')[-1]
        else:
            file_name = mail_application
        _part = MIMEApplication(open(mail_application, 'rb').read())
        _part.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(_part)

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
