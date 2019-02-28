# -*- coding: utf-8 -*-
import whois


def query_website_register(netloc):
    # 查询域名的注册者
    res = whois.whois(netloc)
    show_messages(res)


def show_messages(res):
    # print(type(res))
    # print(res)
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

"""
<class 'whois.parser.WhoisCom'>
{
  "domain_name": [
    "GITHUB.COM",
    "github.com"
  ],
  "registrar": "MarkMonitor, Inc.",
  "whois_server": "whois.markmonitor.com",
  "referral_url": null,
  "updated_date": [
    "2017-06-26 16:02:39",
    "2018-09-27 04:00:28"
  ],
  "creation_date": [
    "2007-10-09 18:20:50",
    "2007-10-09 11:20:50"
  ],
  "expiration_date": [
    "2020-10-09 18:20:50",
    "2020-10-09 11:20:50"
  ],
  "name_servers": [
    "NS-1283.AWSDNS-32.ORG",
    "NS-1707.AWSDNS-21.CO.UK",
    "NS-421.AWSDNS-52.COM",
    "NS-520.AWSDNS-01.NET",
    "NS1.P16.DYNECT.NET",
    "NS2.P16.DYNECT.NET",
    "NS3.P16.DYNECT.NET",
    "NS4.P16.DYNECT.NET",
    "ns-1707.awsdns-21.co.uk",
    "ns4.p16.dynect.net",
    "ns-1283.awsdns-32.org",
    "ns-520.awsdns-01.net",
    "ns-421.awsdns-52.com",
    "ns1.p16.dynect.net",
    "ns2.p16.dynect.net",
    "ns3.p16.dynect.net"
  ],
  "status": [
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)"
  ],
  "emails": [
    "abusecomplaints@markmonitor.com",
    "whoisrequest@markmonitor.com"
  ],
  "dnssec": "unsigned",
  "name": null,
  "org": "GitHub, Inc.",
  "address": null,
  "city": null,
  "state": "CA",
  "zipcode": null,
  "country": "US"
}
"""




if __name__=="__main__":

    netloc = "https://github.com"
    # netloc1 = "http://example.webscraping.com/"
    query_website_register(netloc)