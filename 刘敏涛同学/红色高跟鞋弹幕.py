"""
思路：
1. 利用requests请求网页并使用正则获取弹幕
2. 生成专属词云
"""

import requests
import re
import wordcloud
import PIL.Image as image
import numpy as np


# 获取网页和数据
def getHtmlText(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    data = response.content.decode('utf-8')
    pat = '<d p=".*?">(.*?)</d>'
    all_comment = re.findall(pat, data, re.S)
    # print(allComment)
    with open('./弹幕.txt', 'a', encoding='utf-8-sig') as f:
        for i in all_comment:
            f.write(i + '\n')
    print("写入成功！")


# 4. 生成专属词云图
def showPic():
    img = np.array(image.open('demo.jpg'))
    with open('弹幕.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        w = wordcloud.WordCloud(font_path = "msyh.ttc", mask=img, scale=15, width=1000, height=700, background_color='white')
        w.generate(text)
        w.to_file("taojie.png")
    print("生成成功！")


if __name__ == '__main__':
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=187988454'
    getHtmlText(url)
    showPic()