import requests
import re


class Spider(object):
    def __init__(self):
        # 放名字
        self.name_list = []
        # self.url_list = []
        # 请求头
        self.headers = {
            'user-agent': '这里是你的user-agent的内容'
        }

    def get_mes(self):
        id_list = []
        for i in range(1, 4):
            page_url = f'https://www.ximalaya.com/youshengshu/16411402/p{i}/'
            response = requests.get(url=page_url, headers=self.headers).content.decode('utf-8')
            pat = '<a title="(.*?)" href="(.*?)">'
            result = re.findall(pat, response, re.S)
            # print(result)
            for title, href in result[6:]:
                self.name_list.append(title)
                id_list.append(href.split('/')[-1])
                # self.url_list = 'https://www.ximalaya.com' + href
        return id_list

    def get_audio(self, id_list):
        j = 0
        for i in id_list:
            audio_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={i}&ptype=1'
            res = requests.get(audio_url, headers=self.headers).content.decode('utf-8')
            pat = '"src":"(.*?)"'
            result = re.findall(pat, res, re.S)
            # print(result[0])
            response = requests.get(result[0])
            if response:
                with open(f'{self.name_list[j]}.m4a', 'wb') as f:
                    f.write(response.content)
                print(f'{self.name_list[j]}爬取成功')
                j += 1

    def run(self):
        id_list = self.get_mes()
        self.get_audio(id_list)


spider = Spider()
spider.run()
