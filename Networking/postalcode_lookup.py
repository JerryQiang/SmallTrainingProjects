import urllib
import requests
import lxml.html


# add parameter: num_retries
def download(url, num_retries=2):
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
                return download(url, num_retries-1)
    return html


def get_postalcode():
    postalcode = input()
    if not postalcode:
        postalcode = '425000'  # 默认我家乡编码，33000我本科学校编码

    url = 'http://www.ip138.com/post/search.asp?zip=' + postalcode + '&action=zip2area'
    html = download(url)
    tree = lxml.html.fromstring(html)
    tds = tree.cssselect("td.tdc2")
    datas = []
    for td in tds:
        cnt = td.text
        # print(cnt)
        if cnt:
            datas.append(cnt)
    data = datas[0].split()
    province = data[1]
    city = data[2]
    postalCode = data[3].split('：')[1]
    areaCode = data[4].split('：')[1]
    print('省份：' + province)
    print('城市：' + city)
    print('邮编：'+ postalCode)
    print('区号：'+ areaCode)


if __name__ == '__main__':
    get_postalcode()