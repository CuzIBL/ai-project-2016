# -*- coding:utf8 -*-
# 访问SCIgen，随机生成假论文，并保存页面源码
import urllib2
from bs4 import BeautifulSoup

for i in range(100,1000):
	outfile = open(str(i)+'.txt', 'w+')
	# 获取页面源码
	url = 'http://pdos.csail.mit.edu/cgi-bin/sciredirect.cgi'
	try:
		request = urllib2.Request(url)
		source_code = urllib2.urlopen(request, timeout=20).read()
	except:
		outfile.close()
		continue

outfile.write(source_code)
outfile.close()
print i
