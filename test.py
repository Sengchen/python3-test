#!/usr/bin/python3 -*- coding: UTF-8 -*-

# new spider python3
import urllib.request
from html.parser import HTMLParser as hp
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import chardet
import io
import sys

class spider(object):
	"""docstring for spider"""
	def __init__(self, arg):
		super(spider, self).__init__()
		self.arg = arg

	def excute():
		print(dt.now())
		response = urllib.request.urlopen('http://www.baidu.com')

		print(response.status)
		return response.read()

class parser(hp):
	def handle_starttag(self, tag, attrs):
		"""
		recognize start tag, like <divhtml>
		:param tag:
		:param attrs:
		:return:
		"""
		print("<", tag, '>')

	def handle_endtag(self, tag):
		"""
		recognize end tag, like </div>
		:param tag:
		:return:
		"""
		print("<", tag, '>')

	def handle_data(self, data):
		"""
		recognize data, html content string
		:param data:
		:return:
		"""
		print(data)

	def handle_startendtag(self, tag, attrs):
		"""
		recognize tag that without endtag, like <img />
		:param tag:
		:param attrs:
		:return:
		"""
		print("<", tag, attrs[0], '/>')

	def handle_comment(self,data):
		"""

		:param data:
		:return:
		"""
		print("Encountered comment :", data)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # 改变标准输出的默认编码

result = spider.excute()
result = bs(result.decode('utf-8'), 'html.parser')
titles = result.find_all('a')
for title in titles:
	print(title)
# parser = parser()
# parser.feed(str('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1><img src = "" />'
#             '<!-- comment --></body></html>'))