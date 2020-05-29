"""
请求拉勾网python前十页的招聘数据，并将信息写入到一个txt文件
（速度不要太快，小心被封）

需求1：获取以下信息
    'city'：城市
    'companyFullName'：公司名
    'companySize'：公司规模
    'education'：学历
    'positionName'：职位名称
    'salary'：薪资
    'workYear'：工作了多长时间

需求2：以逗号分隔信息内容，写入文件。要求文件名为’拉勾职位信息.csv‘
例如：
    上海，上海沸橙信息科技有限公司，150-500人，本科，python，8k-12k，不限

"""
import json
import requests
import pprint
import time

url = 'https://www.lagou.com/jobs/positionAjax.json'
params = 'px=default&needAddtionalResult=false'

headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python/p-city_215?px=default',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


def get_cookies():
    # 创建会话（自动更新服务器给设置的cookie）
    session = requests.session()
    rst = session.get('https://www.lagou.com/jobs/list_python/p-city_0?px=default', headers=headers)
    return rst.cookies.get_dict()


def get_sid():
    ses = requests.session()
    rs = ses.post(url=url, params=params, headers=headers, cookies=get_cookies(), allow_redirects=False)
    sid = json.loads(rs.text)["content"]["showId"]
    print(sid)
    # print(sid["content"]["showId"])
    return sid


def get_data(page, sid=None):
    if page == 1:
        return {
            'first': 'true',
            'pn': {page},
            'kd': 'python',
        }
    else:
        return {
            'first': 'false',
            'pn': {page},
            'kd': 'python',
            'sid': sid
        }


def get_mes(page, cookies):
    sid = None
    data = get_data(page, sid=sid)
    response = requests.post(url=url,
                             params=params,
                             data=data,
                             headers=headers,
                             cookies=cookies,
                             allow_redirects=False)
    mes_dict = json.loads(response.text)
    result = mes_dict['content']['positionResult']['result']
    # pprint.pprint(result)
    with open("拉勾职位信息.csv", "a", encoding='utf-8-sig') as f:
        for one in result:
            one_page_msg = f"{one['city']}, {one['companyFullName']}, {one['companySize']}, {one['education']}, {one['positionName']}, {one['salary']}, {one['workYear']}"
            f.write(one_page_msg + '\n')


if __name__ == '__main__':
    cookies = get_cookies()
    for i in range(1, 31):
        if i % 5 == 0:
            cookies = get_cookies()
        get_mes(i, cookies)
        time.sleep(3)
        print('succeed')