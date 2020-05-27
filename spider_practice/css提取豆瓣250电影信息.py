"""
    使用 css 选择器将豆瓣 250 的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250
    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
"""
import requests
import parsel
import time

url = 'https://movie.douban.com/top250'
headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
for i in range(0, 11):
    time.sleep(2)
    params = {
        'start': i*25,
        'filter': ''
    }
    html = requests.get(url=url, headers=headers, params=params)
    selector = parsel.Selector(html.text)
    lis = selector.css('div.article li')
    for li in lis:
        title = li.css('span.title::text').get()
        # print(title)
        info = li.css('div.bd>p::text').get().strip()
        # print(info)
        score = li.css('span.rating_num::text').get()
        # print(score)
        follow = li.css('div.star span::text')[1].get()
        # print(follow)
        print(f'电影：{title}；{info}；评分：{score}；{follow}')