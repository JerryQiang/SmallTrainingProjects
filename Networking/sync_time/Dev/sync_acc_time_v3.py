# synctime.py

import os
import ntplib
import time
from datetime import datetime


def get_time():
    hosts = ['edu.ntp.org.cn', 'tw.ntp.org.cn', 'us.ntp.org.cn', 'cn.pool.ntp.org', 'jp.ntp.org.cn']
    client = ntplib.NTPClient()
    for host in hosts:
        try:
            response = client.request(host)
            if response:
                break
        except Exception as e:
            print(host+'同步失败')
            pass
    sys_time = time.time()
    cur_time = response.tx_time
    print('相差', cur_time-sys_time)
    return cur_time,sys_time


def sync_sys_time(cur_time, sys_time):
    t1 = time.time()
    _date, _time = str(datetime.fromtimestamp(cur_time))[:22].split(' ')
    a, b, c = _time.split(':')
    _time = "%s:%s:%s" % (a, b, c)
    s = 'date %s && time %s' % (_date, _time)
    t2 = get_time()[1]
    os.system(s)
    t3 = time.time()[1]
    print('t1 - sys_time:', t1 - sys_time)
    print('t2-t1:', t2 - t1)
    print('t3-t2:', t3 - t2)

    cur_time = cur_time + (t1 - sys_time) + 2*(t2 - t1) + (t3 - t2)
    _date, _time = str(datetime.fromtimestamp(cur_time))[:22].split(' ')
    a, b, c = _time.split(':')
    _time = "%s:%s:%s" % (a, b, c)
    s = 'date %s && time %s' % (_date, _time)
    os.system(s)




def sync_time(cur_time, sys_time):

    sync_sys_time(cur_time, sys_time)

    # sync_sys_time(cur_time + (t1 - sys_time) + 2*(t2-t1))
    # sys_time = time.time()
    # print(cur_time - sys_time)
    # show_time(cur_time, sys_time)

def test():
    cur_time, sys_time = get_time()
    sync_sys_time(cur_time, sys_time)
    cur_time, sys_time = get_time()

def show_time(cur_time, sys_time):
    print("系统当前时间", str(datetime.fromtimestamp(sys_time))[:22].split(' '))
    print("北京标准时间", str(datetime.fromtimestamp(cur_time))[:22].split(' '))
#     print("同步后时间:", str(datetime.now())[:22])

# os.system("pause")

if __name__ == '__main__':
    test()