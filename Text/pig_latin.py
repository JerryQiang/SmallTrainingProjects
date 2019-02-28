# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Pig Latin(2.拉丁猪文字游戏)
这是一个英语语言游戏。
基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay
（譬如"banana"会变成"anana-bay"），除了a、e、i、o、u 5个元音字母外,其余都是辅音。

'''
import sys
import re


def pig_latin_v1(s):
    if isinstance(s, str):
        arr = 'aeiou'
        for (i, c) in enumerate(s.lower()):
            if c not in arr:
                s = s[0:i]+ s[i+1:] + '-' + c + 'ay'
                break
        return s
    else:
        raise Exception('拉丁猪文字游戏出错:输入参数为'+type(s).__name__+'类型，请输入str类型')


def pig_latin_v2(s):
    if isinstance(s, str):
        re_str = '[^aeiou]'
        pattern = re.compile(re_str, re.IGNORECASE|re.MULTILINE)
        # print(type(pattern))
        search_obj = pattern.search(s)
        # print(type(search_obj))
        start_position, end_position = search_obj.span()
        # print(s[start_position:end_position])
        new_s = s[0:start_position] + s[end_position:] + '-' + s[start_position] + 'ay'
        return new_s
    else:
        raise Exception('拉丁猪文字游戏出错:输入参数为'+type(s).__name__+'类型，请输入str类型')


pig_latin = pig_latin_v2


def print_pig_latin(s):
    try:
        new_s = pig_latin(s)
        print(s+'单词转换为'+new_s)
    except Exception as e:
        print(str(e))


def main(args=sys.argv):
    # print(args)
    if len(args) <= 1:
        s = 'banana'
    else:
        s = args[1]
    print_pig_latin(s)


if __name__ == '__main__':
    main()

