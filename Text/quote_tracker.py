import requests
from bs4 import BeautifulSoup
import traceback
import re
# import socket
import time


def getHTMLText(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def main():
    url = "https://gupiao.baidu.com/stock/hkHSI.html"
    # sock = socket.socket()
    # hostname = socket.gethostname()
    # print(hostname)
    # port = 3000
    # sock.connect((hostname, port))
    while True:
        html = getHTMLText(url)
        soup1 = BeautifulSoup(html, 'html.parser')
        soup = soup1
        stockInfo = soup1.find('div', attrs={'class': 'price'})
        date = soup.find('span', attrs={'class': 'state'})
        stockInfo_str = str(stockInfo)
        date_str = str(date)
        stockInfo_str += "\r\n"
        print(stockInfo_str + date_str)
        b = bytes(stockInfo_str + date_str, encoding="utf-8")
        # sock.send(b)
        print("Content Sent")
        # time.sleep(30)


main()