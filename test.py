#encoding: utf-8
import urllib
#文件的删除
import os
#字符串的替换
import re



#读取网页
def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html



#获取正文内容
def getContent(html):
	str = '<div id="content">'
	content = html.partition(str)[2]
	str2 = '<div class="bottem">'
	content = content.partition(str2)[0]
	return content

#写入正文文件
def content_write(data):
	fo = open("G:/new/new.txt", "a+")
	fo.write("\n\n\n\n\n")
	data = data.replace("<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;", "\n");
	fo.write(data)
	fo.write("\n\n\n\n\n")
	fo.close()
"""
content = content(getHtml("https://www.biquge.info/46_46766/4557102.html"))
data_write(content)
"""
#对list进行循环 获取内容
def getStr(str):
	fo = open("G:/new/find.txt", "a+")
	data = re.findall(r'https.*?html', str)
	print data
	for html in data:
		fo.write(html)
		fo.write("\n")
		content_write(getContent(getHtml(html)))
	fo.close()

#获取目录
def getList(html):
	str = '<dl>'
	content = html.partition(str)[2]
	str2 = '</dl>'
	content = content.partition(str2)[0]
	return content

#写入目录文件
def list_write(data, url):
	"""
	os.remove("G:/new/list.txt");
	fo = open("G:/new/list.txt", "a+")
	"""
	data = re.sub(r'html".+\n.+<a href="', 'html\n'+url, data)
	data = re.sub(r'<dd><a href="', url, data)
	data = re.sub(r'" title=".+</dd>', '', data)
	data = re.sub(r'\n', '', data)
	"""
	fo.write(data)
	fo.close()
	"""
	return data
url = input("Please input the url: (when input please write with [\"\"])")
#"https://www.biquge.info/46_46766/"
content = getList(getHtml(url))
list = list_write(content, url)

getStr(list);