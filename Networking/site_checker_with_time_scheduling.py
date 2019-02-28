#!/bin/bash
# -*- coding:utf-8 -*-
import sys
import os
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def site_checker():
    argv = sys.argv
    ip = 'cose.seu.edu.cn'
    if len(argv) > 1:
        ip = argv[1]
    exit_code = os.system('ping ' + ip)
    if exit_code != 0:
        txt = ip + ' connect failed.'
        send_email(txt)
        # print('connect failed.')
    else:
        # txt = ip + ' connect success.'
        # send_email(txt)
        # print('connect success.')
        pass


def send_email(txt):
    from_addr = '1131233593@qq.com'
    password = 'nlewbjbhqbprhhde'
    smtp_server = 'smtp.qq.com'
    port = 25
    to_addr = 'jzq1131233593@163.com'  # 1131233593@qq.com,3494860985@qq.com,3264713524@qq.com
    # jzq1131233593@163.com,jzq_1131233593@163.com

    msg = MIMEText(txt, 'plain', 'utf-8')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = formataddr((Header('Python爱好者', 'utf-8').encode(), to_addr))
    msg['Subject'] = Header('网站定时连接检查……', 'utf-8').encode()

    print('From:', msg['From'])
    print('To:', msg['To'])
    print('Subject:', msg['Subject'])

    server = smtplib.SMTP(smtp_server, port)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr.split(','), msg.as_string())
    server.quit()


def _format_addr(s):
    name, addr = parseaddr(s)
    # print(s, name, addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))


if __name__ == '__main__':
    if __name__ == '__main__':
        while True:
            site_checker()
            time.sleep(60 * 60)  # 1h检查网站是否联通
