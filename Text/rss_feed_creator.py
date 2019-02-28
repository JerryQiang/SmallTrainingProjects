import feedparser

def rss(rss_url):
    file = feedparser.parse(rss_url)
    print([item.title for item in file.entries])
    print([item.link for item in file.entries])

if __name__ == '__main__':
    rss_url = input()
    if not rss_url:
        rss_url = 'http://feed.cnblogs.com/blog/u/161528/rss'
    rss(rss_url)