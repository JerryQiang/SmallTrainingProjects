# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Count Vowels(3.统计元音字母)
输入一个字符串，统计处其中元音字母的数量。
更复杂点的话统计出每个元音字母的数量。
a、e、i、o、u 5个元音字母
'''
import sys

VOWELS_STR = 'aeiou'


def count_vowels(s):
    if isinstance(s, str):
        d = {}
        for c in s.lower():
            if c in VOWELS_STR:
                d[c] = d.get(c, 0) + 1
        d['count'] = 0
        for c in VOWELS_STR:
            d['count'] += d.get(c, 0)
        return d
    else:
        raise Exception('统计元音字母出错:输入参数为'+type(s).__name__+'类型，请输入str类型')


def print_count_vowels(s):
    try:
        d = count_vowels(s)
        print(s, '元音字母一共有', d['count'], '个')
        for c in VOWELS_STR:
            print(c+'有', d.get(c, 0), '个', end=',')
    except Exception as e:
        print(str(e))


def main(args=sys.argv):
    # print(args)
    if len(args) <= 1:
        s = 'favourite'
    else:
        s = args[1]
    print_count_vowels(s)


if __name__ == '__main__':
    main()

