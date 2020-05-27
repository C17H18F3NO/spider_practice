"""
    使用 xpath 将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
from lxml import etree

score_list = []
headers = {
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(0, 11):
    url = f'https://maoyan.com/board/4?offset={i*10}'
    response = requests.get(url=url, headers=headers).text
    html = etree.HTML(response)
    data = html.xpath('//dl[@class="board-wrapper"]')
    for da in data:
        name = da.xpath('.//div//a/text()')
        print(name)
        star = da.xpath('.//p[@class="star"]/text()')
        print(star)
        releasetime = da.xpath('//p[@class="releasetime"]/text()')
        print(releasetime)
        score = da.xpath('//i[@class="integer"]/text()') + da.xpath('//i[@class="fraction"]/text()')
        print(score)