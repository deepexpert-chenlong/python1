import urllib
import urllib2
url='www.baidu.com'
user_agent='Mozilla/4.0(compatible;MSIE5.5;Windows NT)'
values={'name':'cl',
        'location':'sz'}
headers={'User-Agent':user_agent}
data=urllib.urlencode(values)
req=urllib2.Request(url,data,headers)
response=urllib2.urlopen(req)
tage=response.read()
print tage