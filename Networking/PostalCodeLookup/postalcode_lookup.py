import urllib
import requests
import lxml.html


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


postalcode = '425000'  # 33000
url = 'http://www.ip138.com/post/search.asp?zip=' + postalcode + '&action=zip2area'
html = download3(url)
# print(html)
tree = lxml.html.fromstring(html)
tds = tree.cssselect("td.tdc2")
print(tds)
print([td.text for td in tds])
print(tds[1], tds[1].text)
datas = []
for td in tds:
    cnt = td.text
    # print(cnt)
    if cnt:
        datas.append(cnt)
print(datas)
print(type(datas[0]), datas[0])
data = datas[0].split()
print(data)
province = data[1]
city = data[2]
postalCode = data[3].split('：')[1]
areaCode = data[4].split('：')[1]
print('省份：' + province)
print('城市：' + city)
print('邮编：'+ postalCode)
print('区号：'+ areaCode)