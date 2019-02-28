# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
CD Key Generator(14)CD-Key生成器
利用某种算法生成一个唯一的key。软件开发者可以用它来作为软件的激活器。
CDKey就是产品公司用于识别客户身份的一串字母或是数字混合的序列号。
使用md5算法，生成128 bit，即32位16进制数
也可采用SHA1, SHA256, SHA512等其它算法
'''
import sys
import hashlib


def md5_cd_key(s):
    if isinstance(s, str):
        md5 = hashlib.md5(s.encode('utf-8'))
        return md5.hexdigest()
    else:
        raise Exception('CD-Key生成器错误:输入参数为'+type(s).__name__+'类型，请输入str类型')


def print_cd_key(s):
    try:
        cd_key = md5_cd_key(s)
        print(s+'生成的cd_key为：'+cd_key)
    except Exception as e:
        print(str(e))
        # print(e.args[0])


def test():
    print("现在进行CD-Key生成测试......")
    arr = ['how to use md5 in python hashlib?', '1131233593@qq.com']  # 结果依次为：
    for s in arr:
        print_cd_key(s)
    print("CD-Key生成测试完成!")


def main(args=sys.argv):
    # print(args)
    if len(args)<=1:
        s = '1131233593@qq.com'
    else:
        s = args[1]
    print_cd_key(s)

if __name__ == '__main__':
    # test()
    main()

