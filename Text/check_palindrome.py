# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Check if Palindrome(4.判断是否为回文)
判断用户输入的字符串是否为回文。
回文是指正反拼写形式都是一样的词，譬如"racecar"。
'''
import sys


# 逆转字符串
def rev_str(s):
    if isinstance(s, str):
        rev_list = list(s)
        rev_list.reverse()
        rev_s = "".join(rev_list)
        return rev_s
    else:
        raise Exception('逆转字符串错误:输入参数为'+type(s).__name__+'类型，请输入str类型')


# 判断是否为回文
def check_par(s):
    rev_s = rev_str(s)
    if s == rev_s and s is not '' :
        return True
    else:
        return False


def print_check_par(s):
    try:
        res = check_par(s)
        if res is True:
            print(s, "为回文字符串")
        else:
            print(s, "为非回文字符串")
    except Exception as e:
        print(str(e))


# 测试print_check_par(s)
def test():
    print("现在进行回文字符串测试......")
    test_arr = [123, "", "12321"]
    for test in test_arr:
        print_check_par(test)
    print("回文字符串测试完成!")


def main(args=sys.argv):
    # print(args)
    if len(args)<=1:
        s = 'test'
    else:
        s = args[1]
    print_check_par(s)

# 测试代码
if __name__ == "__main__":
    test()
    # main()