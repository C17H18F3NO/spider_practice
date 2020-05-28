"""
思路：
1. 利用requests请求网页
2. 找到所有评论并存入二位列表
3. 将所存数据下载到文本
4. 生成专属词云
"""

import requests
import wordcloud
from bs4 import BeautifulSoup
import PIL.Image as image
import numpy as np


# 获取网页
def getHtmlText(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        data = response.content.decode('utf-8')
        return data
    except:
        return ''


# 2. 找到所有评论并将其存入二维列表
def fillList(html, list):
    soup = BeautifulSoup(html, 'html.parser')
    itotal = soup.find('i')
    dtotals = itotal.find_all('d')
    for dtotal in dtotals:
        danmu = dtotal.text
        List.append([danmu])

# 3. 将二维列表中的所有数据下载到文本
def down_danmu(list):
    for list in List:
        with open('./后浪弹幕.txt', 'a', encoding='utf-8-sig') as f:
            s = str(list).replace('[', '').replace(']', '') + '\n'
            s = s.replace("'", '').replace(',', '')
            f.write(s)
    print("文件写入成功！")

# 4. 生成专属词云图
def showPic():
    img = np.array(image.open('demo.jpg'))
    with open('后浪弹幕.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        w = wordcloud.WordCloud(font_path = "msyh.ttc", mask=img, scale=15, width=1000, height=700, background_color='white')
        w.generate(text)
        w.to_file("Houlang.png")

List = []
# 在network里面找所有弹幕的一个链接
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=189702747'
html = getHtmlText(url)
fillList(html, List)
down_danmu(List)
showPic()