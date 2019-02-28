# MUA(Mail User Agent)邮箱用户代理
# MTA(Mail Tranfer Agent)邮箱传输代理
# MDA(Mail Delivery Agent)邮箱投递代理

# STMP发送邮件
# email负责构造邮件 smtplib负责发送邮件

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# Email地址和口令
from_addr = "1131233593@qq.com"
password = ""

# 收件人地址
to_addr = "To"

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
