import urllib.request
from lxml import etree
"""
这个文件我用来测试xpath路径问题，并不是scrapy框架中的部分
"""

html = urllib.request.urlopen("http://blog.jobbole.com/113956/").read().decode("utf-8")
et = etree.HTML(html)
print(et.xpath("/html/body/div[1]/div[3]/div[1]/div[2]/p/text()")[0].strip().replace(" ·", ""))
# title_list = []
# date_list = []
# for i in range(1, 21):
#     title_list.append(et.xpath("/html/body/div[1]/div[3]/div[{0}]/div[1]/a/@title".format(i))[0])
#     date_list.append(et.xpath("/html/body/div[1]/div[3]/div[{0}]/div[2]/p/text()".format(i))[1].strip().replace(" ·",""))
# for i, j in zip(title_list, date_list):
#     print(i, j)