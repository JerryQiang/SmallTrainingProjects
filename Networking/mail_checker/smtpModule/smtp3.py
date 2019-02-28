# coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# 发送html格式的邮件

# 发送邮箱
sender = "1131233593@qq.com"
# 接收邮箱
receiver = "jzq1131233593@163.com"
# 发送邮件主题
subject = "自动发送邮件测试2018/12/22"
# 发送邮箱服务器
smtpserver = "smtp.qq.com"
# 发送邮箱用户/密码
username = "1131233593@qq.com"
password = "nlewbjbhqbprhhde"

# HTML形式的邮件
msg = MIMEText("<html><h1>1.找Outlook的授权码，下周五以邮件给我答复结果\
2.把排序写成函数--排列组合\
3.众数--思考一下\
</h1></html>", "html", "utf-8")
msg["Subject"] = Header(subject, "utf-8")

smtp = smtplib.SMTP_SSL(smtpserver, 465)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
