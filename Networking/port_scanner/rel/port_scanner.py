#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from socket import *
import threading


lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % port)
        lock.release()
        s.close()
    except:
        pass

def main():
    host = '118.24.4.66'
    port_range = [1, 1024]
    argv = sys.argv
    par_num = len(argv)
    # print(argv, par_num)
    if par_num > 0:
        host = argv[1]
        for i in range(2, par_num):
            port_range[i-2] = int(argv[i])
    # print(port_range)
    setdefaulttimeout(1)
    print('Scanning the host:%s......' % (host))
    for p in range(port_range[0],port_range[1]):
        t = threading.Thread(target=portScanner,args=(host,p))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('[*] The host:%s scan is complete!' % (host))
    print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()