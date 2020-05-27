"""
    使用 css 选择器将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import parsel


headers = {
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(0, 11):
    url = f'https://maoyan.com/board/4?offset={i*10}'
    html = requests.get(url=url, headers=headers)
    selector = parsel.Selector(html.text)
    dds = selector.css('div.main dd')
    for dd in dds:
        name = dd.css('p.name a::text').get()
        # print(name)
        star = dd.css('p.star::text').get().strip()
        # print(star)
        releaseTime = dd.css('p.releasetime::text').get()
        # print(releaseTime)
        score = dd.css('i.integer::text').get() + dd.css('i.fraction::text').get()
        # print(score)
        print(f'电影：{name}；{star}；{releaseTime}；评分：{score}')
