#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket

def portScanner(host,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print('[+] %d open' % port)
        s.close()
    except Exception as e:
        print('[-] %d close' % port)


def main():
    socket.setdefaulttimeout(1)
    for p in range(1,1024):
        portScanner('192.168.0.100',p)


if __name__ == '__main__':
    main()