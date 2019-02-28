# -*- coding: utf-8 -*-
"""单个网页下载"""
import urllib.request
import urllib.parse


def download1(url):
    """Simple downloader"""
    return urllib.request.urlopen(url).read()


# add Exception process
def download2(url):
    """Download function that catches errors"""
    print("Downloading:", url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason)
        html = None
    return html


# add parameter: num_retries
def download3(url, num_retries=2):
    """Download function that also retries 5XX errors"""
    # 默认重新再下载两次
    print("Downloading:", url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason, type(e))
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download3(url, num_retries-1)
    return html


# add parameter: user_agent
# Web Scraping with Python
def download4(url, user_agent="wswp", num_retries=2):
    """Download function that includes user agent support"""
    # user_agent="wswp" Web Scraping with Python
    print("Downloading:", url)
    headers = {"User-agent":user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason, type(e))
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download4(url, user_agent, num_retries-1)
    return html


# 下载网页健壮版
# 默认重新下载两次
# add parameter: proxy
def download5(url, user_agent="wswp", proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print("Downloading:", url)
    headers = {"User-agent":user_agent}
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener() # 支持代理
    if proxy:
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib.request.URLError as e:
        print("Download error:", e.reason, type(e))
        html = None
        if num_retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download5(url, user_agent, proxy,num_retries-1)
    return html


# add parameter: headers, data
def download6(url, headers={"User-Agent":"wswp"}, proxy=None, num_retries=2, data=None):
    print("Downloading:", url)
    request = urllib.request.Request(url, data, headers)
    opener = urllib.request.build_opener()
    if proxy:
        # print(type(urlparse.urlparse(url).scheme), urlparse.urlparse(url).scheme)
        proxy_params = {urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        # code有什么用？
        code = response.code
    except urllib.request.URLError as e:
        print("Download error:", e.reason)
        html = ""
        if hasattr(e, "code"):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html


download = download6


if __name__ == "__main__":
    # print(download1("http://example.webscraping.com"))

    # print(download2("http://httpstat.us/500"))

    # print(download3("http://httpstat.us/500"))

    # print(download3("http://www.meetup.com/")) # 默认代理可以爬取，应该是网站更新了
    # print(download4("http://example.webscraping.com", user_agent = "BadCrawler")) # 网站实际并没有禁止代理"BadCrawler"
    # print(download4("http://example.webscraping.com", user_agent = "GoodCrawler"))

    print(download("http://example.webscraping.com"))

    pass # 防止注释所有的print后报错