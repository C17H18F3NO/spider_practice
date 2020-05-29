"""
使用代理爬取猫眼100
代理获取地址: http://134.175.188.27:5010/get/
(可以尝试自己在本地搭建代理池)
"""
import requests
import parsel

headers = {
    'Host': 'maoyan.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


def get_proxy():
    response = requests.get('http://134.175.188.27:5010/get/')
    data = response.json()
    proxy = data['proxy']
    print(proxy)
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy
    }
    return proxies


def get_mes():
    for i in range(0, 11):
        url = f'https://maoyan.com/board/4?offset={i*10}'
        try:
            html = requests.get(url=url, headers=headers, proxies=get_proxy())
            selector = parsel.Selector(html.text)
            dds = selector.css('div.main dd')
            for dd in dds:
                name = dd.css('p.name a::text').get()
                star = dd.css('p.star::text').get().strip()
                releaseTime = dd.css('p.releasetime::text').get()
                score = dd.css('i.integer::text').get() + dd.css('i.fraction::text').get()
                print(f'电影：{name}；{star}；{releaseTime}；评分：{score}')
        except:
            get_mes()


if __name__ == '__main__':
    get_mes()
