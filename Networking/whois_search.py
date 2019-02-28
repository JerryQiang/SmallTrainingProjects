# -*- coding: utf-8 -*-
import whois


def query_website_register(netloc):
    # 查询域名的注册者
    res = whois.whois(netloc)
    show_messages(res)


def show_messages(res):

    print('domain_name:',res.domain_name[-1])
    print('org:', res.org)
    print('country:', res.country)
    print('registrar:', res.registrar)
    print('creation_date:', res.creation_date[-1])
    print('updated_date:', res.updated_date[-1])
    print('expiration_date:', res.updated_date[-1])
    print('name_servers:', res.name_servers)
    print('status:', res.status)
    print('emails:', res.emails)
    print('creation_date:', res.creation_date[-1])
    print('updated_date:', res.updated_date[-1])
    print('expiration_date:', res.updated_date[-1])


if __name__ == "__main__":
    netloc = input()
    if not netloc:
        netloc = "https://github.com"
    query_website_register(netloc)