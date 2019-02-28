import geoip2.database

reader = geoip2.database.Reader('D:/Programs/Python/Python36/Lib/site-packages/geoip2/databases/'+
                                'GeoLite2-City/GeoLite2-City.mmdb')
# ip_adr = input()  # '123.123.123.123','223.6.6.6'
ip_adr = '123.123.123.123'
c= reader.city(ip_adr)
# print(type(c), c)
# print(c.country.name)  # 国家名
print('IP地址：' + c.traits.ip_address)
print('大陆：' + c.continent.names.get('zh-CN', ''))
print('注册国家：' + c.registered_country.names.get('zh-CN', ''))
print('所在国家：' + c.country.names.get('zh-CN', ''))
print('城市：' + c.city.names.get('zh-CN', ''))
print ("纬度：", c.location.latitude)
print ("经度：", c.location.longitude)
# 纬度： 34.7725
# 经度： 113.7266


print()