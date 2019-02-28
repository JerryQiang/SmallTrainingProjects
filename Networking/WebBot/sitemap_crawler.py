# -*- coding: utf-8 -*-
import re

from common import download


# sitemap爬虫
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall("<loc>(.*?)</loc>", sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...
        print(html)


if __name__ == "__main__":
    crawl_sitemap("http://example.webscraping.com/sitemap.xml")