# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Random Gift Suggestions(7.帮你挑礼物)
输入一堆你可能会送的礼物，当有人过生日时，该程序会随机选择一样礼物。
也可以加上一个额外功能，可以告知哪里可以弄到这个礼物。给淘宝搜索链接
'''
import random


def random_gift(gifts):
   index =  random.randint(0, len(gifts)-1)
   gift = gifts[index]
   url = 'https://s.taobao.com/search?q = ' + gift
   return(gift, url)


def choose_gift(gifts):
    gift, url = random_gift(gifts)
    print('帮你挑选的礼物是:',gift)
    print('url:', url)


def main():
    gifts = ['玫瑰', '音乐盒', '巧克力', '口红', '包包', '我']
    choose_gift(gifts)


if __name__ == '__main__':
    main()