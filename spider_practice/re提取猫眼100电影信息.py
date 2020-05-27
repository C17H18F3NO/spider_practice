"""
    使用 正则表达式 将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import re

score_list = []
headers = {
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(0, 11):
    url = f'https://maoyan.com/board/4?offset={i*10}'
    html = requests.get(url=url, headers=headers).content.decode('utf-8')
    print(html)
    name_pat = '<p class="name"><a href=".*?" title="(.*?)"'
    name = re.findall(name_pat, html, re.S)
    print(name)
    star_pat = '<p class="star">(.*?)</p>'
    star = re.findall(star_pat, html, re.S)
    print(star)
    releaseTime_pat = '<p class="releasetime">(.*?)</p> '
    releaseTime = re.findall(releaseTime_pat, html, re.S)
    print(releaseTime)
    score_pat = '<i class="integer">(\d\.)</i><i class="fraction">(\d)</i>'
    score = re.findall(score_pat, html, re.S)
    # for a, b in score:
    #     real_score = a + b
    #     score_list.append(real_score)
    # print(score_list)
    print(score)
