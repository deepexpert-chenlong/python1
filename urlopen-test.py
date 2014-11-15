import urllib2
url='http://www.zgsj.com/domain_reg/'
response=urllib2.urlopen(url)
test=response.read()
print test