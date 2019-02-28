# sync_time.py
# 精确到毫秒级，管理员执行

import os
import ntplib
from datetime import datetime

client = ntplib.NTPClient()

hosts = ['edu.ntp.org.cn', 'tw.ntp.org.cn', 'us.ntp.org.cn', 'cn.pool.ntp.org', 'jp.ntp.org.cn']

print('可用NTP有：', hosts)
print('每个NTP对应背后都有个原子钟.')
for host in hosts:
    try:
        response = client.request(host)
        if response:
            break
    except Exception as e:
        print(host+'同步失败')
        pass

sys_time = datetime.now()
current_time = response.tx_time
_date, _time = str(datetime.fromtimestamp(current_time))[:22].split(' ')
print("系统当前时间", str(sys_time)[:22])
print("北京标准时间", _date, _time)
a, b, c = _time.split(':')
c = float(c) + 0.5
_time = "%s:%s:%s" % (a, b, c)
s = 'date %s && time %s' % (_date, _time)
os.system(s)
print("同步成功，现在时间为:", str(datetime.now())[:22])
os.system("pause")