# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Encrypted SMS(6.密码短信)
可以将数据加密解密，并能将其发送给朋友。
base64简单加解密

cryptography
DES加解密
AES加解密
RSA

文本使用对称加密，客户端非对称加密公钥加密对称密钥，服务器端非对称加密私钥解密
得到对称密钥，再解密文本，反之亦然。
'''
import base64
from cryptography.fernet import Fernet

CIPHER_KEY = 'h62AYEnxQOcZVAa2A54VpiR7BrRal9RgMTQuEDXrmLA='


# base64简单加密
def base64_encrypt(plaintext):
    ciphertext = base64.b64encode(plaintext.encode('utf-8'))
    return ciphertext


# base64简单解密
def base64_decrypt(ciphertext):
    plaintext = base64.b64decode(ciphertext).decode('utf-8')
    return plaintext


# fernet加密
def fernet_encrypt(plaintext):
    cipher = Fernet(CIPHER_KEY)
    byte_txt = bytes(plaintext, 'utf-8')
    ciphertext = cipher.encrypt(byte_txt)
    return ciphertext


# fernet解密
def fernet_decrypt(ciphertext):
    cipher = Fernet(CIPHER_KEY)
    plaintext = cipher.decrypt(ciphertext)
    str_txt = str(plaintext, 'utf-8')
    return str_txt


# encrypt = base64_encrypt
# decrypt = base64_decrypt


encrypt = fernet_encrypt
decrypt = fernet_decrypt


def send_message(message):
    print("模拟发送信息......")
    print("发送"+message)
    print("发送成功")
    return encrypt(message)


def receive_message(message):
    print("模拟接收信息......")
    message = decrypt(message)
    print("接收"+message)
    print("接收成功")
    return message


def main():
    message = '2019：猪年大吉，诸事顺利'
    ciphertext = send_message(message)
    plaintext = receive_message(ciphertext)


if __name__ == '__main__':
    main()
