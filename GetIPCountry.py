# -*- coding: utf-8 -*-

import urllib2
import json
import re
import sys
import chardet


class IPInfo:
	"""
	Get ip infomation from url
	"""

	def __init__(self, url = 'http://ip.taobao.com/service/getIpInfo.php?ip='):
		self._url = url

	def get(self, ip):
		org_str = urllib2.urlopen(self._url+ip).read()
		# print 'Original str:', org_str
		cov_str = json.loads(org_str)
		# print 'Convert str:', cov_str
		return cov_str
ip = None
if len(sys.argv) > 1:
	ip = sys.argv[1]

if __name__ == '__main__':
	info = IPInfo().get(ip)
	print 'info', info
	if info[u'code'] == 0:
		data = info[u'data'] # data is unicode coding
		print 'Country is ', data[u'country']
		print 'Country id is', data[u'country_id']
		print 'City is', data[u'city']
	else:
		print info.get('data', 'Unkown Error!')





