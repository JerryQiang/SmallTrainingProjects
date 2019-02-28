# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Count Words in a String(5.统计字符串中的单词数目)
统计字符串中单词的数目，
更复杂的话从一个文本中读出字符串并生成单词数目统计结果。
'''
import sys
import re

REPLACE_STR = '!"#$%&()*+,-./:;<=>?@[\]^_\'{|}~:'
SPLIT_STR = '!"#$%&()*+,-./:;<=>?@[\]^_\'{|}~:'


def count_words_from_str(content):
    if isinstance(content, str):
        for c in REPLACE_STR:
            content = content.replace(c, ' ')
        split_words = content.lower().split()
        count_dict = {}
        for word in split_words:
            count_dict[word] = count_dict.get(word, 0) + 1
        return count_dict
    else:
        raise Exception('统计字符串错误:输入参数为'+type(content).__name__+'类型，请输入str类型')


# # 直接正则分隔？
# def count_words_from_str(string):
#     if isinstance(string, str):
#         split_pattern = re.compile(SPLIT_STR)
#         split_words = re.split(split_pattern, string.lower())
#         count_words = {}
#         for word in split_words:
#             count_words[word] = count_words.get(word, 0) + 1
#         return count_words
#     else:
#         raise Exception('统计字符串错误:输入参数为'+type(string).__name__+'类型，请输入str类型')


def count_words_from_file(filename):
    file = open(filename)
    count_words = {}
    for line in file.readlines():
        for c in REPLACE_STR:
            line = line.replace(c, ' ')
        print(line)
        words = line.lower().split()
        for word in words:
            count_words[word] = count_words.get(word, 0) + 1
    print(len(count_words))
    return count_words


def print_count_words(content):
    try:
        if content.endswith('.txt'):
            count_words = count_words_from_file(content)
        else:
            count_words = count_words_from_str(content)

        for (word, num) in count_words.items():
            print(word, '的统计数量为:'+str(num))

    except Exception as e:
        print(str(e))
        # print(e.args[0])


def test():
    print("现在进行统计字符串单词数量测试......")
    # string = 'The Tragedy of Hamlet, Prince of Denmark'
    # print_count_words(string)
    filename = 'Test/hamlet.txt'
    print_count_words(filename)
    print("统计字符串单词数量测试完成!")


def main(args=sys.argv):
    # print(args)
    if len(args) <= 1:
        string = 'Test/hamlet.txt'
    else:
        string = args[1]
    print_count_words(string)


if __name__ == '__main__':
    # test()
    main()