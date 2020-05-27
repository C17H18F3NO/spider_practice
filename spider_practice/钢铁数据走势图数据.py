"""目标网址: https://index.mysteel.com/price/indexPrice.html

要求: 上图信息中的钢铁数据走势图中的数据。"""
import requests
import re
import json
import pprint

url = 'https://index.mysteel.com/newprice/getChartMultiCity.ms'
params = {
    'callback': 'callback'
}
form_data = {
    'catalog': '%E8%9E%BA%E7%BA%B9%E9%92%A2_:_%E8%9E%BA%E7%BA%B9%E9%92%A2',
    'city': '%E4%B8%8A%E6%B5%B7,%E5%8C%97%E4%BA%AC,%E5%B9%BF%E5%B7%9E',
    'spec': 'HRB400%2020MM_:_HRB400_20MM',
    'startTime': '2019-05-22',
    'endTime': '2020-05-22'
}
headers = {
    'Host': 'index.mysteel.com',
    'Origin': 'https://index.mysteel.com',
    'Referer': 'https://index.mysteel.com/price/indexPrice.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.post(url=url, params=params, data=form_data, headers=headers).text
# print(response)
rst = re.findall('callback\((.*?)\)', response, re.S)[0]
# print(rst)
res_dict = json.loads(rst)
title = res_dict['title']
print(title)
pat = '"lineName":"(.*?)","dateValueMap":\[(.*?)\]'
result = re.findall(pat, rst, re.S)
# print(result)
for i in range(0, 3):
    print(result[i])
