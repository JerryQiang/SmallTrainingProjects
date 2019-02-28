# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reverse a String（1.逆转字符串）
输入一个字符串，将其逆转并输出。
'''
import sys


def rev_str(s):
    if isinstance(s, str):
        rev_list = list(s)
        rev_list.reverse()
        rev_s = "".join(rev_list)
        return rev_s
    else:
        raise Exception('逆转字符串错误:输入参数为'+type(s).__name__+'类型，请输入str类型')


def print_rev_str(s):
    try:
        new_s = rev_str(s)
        print(s+'逆转为'+new_s)
    except Exception as e:
        # print(str(e))
        print(e.args[0])


def test():
    print("现在进行逆转字符串测试......")
    arr = [123, None, '', 'abc']  # 结果依次为：
    for s in arr:
        print_rev_str(s)
    print("逆转字符串测试完成!")


def main(args=sys.argv):
    # print(args)
    if len(args)<=1:
        s = 'test'
    else:
        s = args[1]
    print_rev_str(s)


if __name__ == '__main__':
    # test()
    main()

