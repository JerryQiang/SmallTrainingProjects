# synctime.py
# 精准校时

import os
import ntplib
import datetime

c = ntplib.NTPClient()

hosts = ['edu.ntp.org.cn', 'tw.ntp.org.cn', 'us.ntp.org.cn', 'cn.pool.ntp.org', 'jp.ntp.org.cn']


for host in hosts:
    try:
        response = c.request(host)
        print(response, type(response))
        if response:
            break
    except Exception as e:
        print(host+'同步失败')
        pass

current_time = response.tx_time
_date, _time = str(datetime.datetime.fromtimestamp(current_time))[:22].split(' ')
print()
print("系统当前时间", str(datetime.datetime.now())[:22])
print("北京标准时间", _date, _time)

a, b, c = _time.split(':')

c = float(c) + 0.5

_time = "%s:%s:%s" % (a, b, c)

s = 'date %s && time %s' % (_date, _time)
print(s)
os.system(s)

print("同步后时间:", str(datetime.datetime.now())[:22])

# os.system("pause")