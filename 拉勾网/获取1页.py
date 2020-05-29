import json
import requests
import pprint
import time

url = 'https://www.lagou.com/jobs/positionAjax.json'
params = 'px=default&needAddtionalResult=false'
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
headers = {
    'authority': 'www.lagou.com',
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


def get_cookie():
    u = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    session = requests.session()
    rst = session.get(url=u, headers=headers)
    cookies = rst.cookies.get_dict()
    return cookies


response = requests.post(url=url,
                         params=params,
                         data=data,
                         headers=headers,
                         cookies=get_cookie())
mes_dict = json.loads(response.text)
result = mes_dict['content']['positionResult']['result']
# pprint.pprint(result)
with open("拉勾职位信息.csv", "a+", encoding='utf-8-sig') as f:
    for one in result:
        one_msg = f"{one['city']}, {one['companyFullName']}, {one['companySize']}, {one['education']}, {one['positionName']}, {one['salary']}, {one['workYear']}"
        # print(one_msg)
        f.write(one_msg + '\n')
