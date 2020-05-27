"""
爬取网易新闻第一页数据，分别将数据保存为json与csv格式
保存字段需要以下内容

title、channelname、docurl、imgurl、label、source、tlastid、tlink
以及新闻的内容 text

"""
import requests
import re
import parsel

news_rst = []
headers = {
    'Host': 'temp.163.com',
    'Referer': 'https://news.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Cookie': '_ntes_nuid=ae04de3dfd91d260b6858b3d5bcf5f40; _ntes_nnid=4611aa25bd0b7df1c23400ee7d1ad9e7,1589972790049; s_n_f_l_n3=7c473844b35fc7e51589972790059; Province=020; City=020; NNSSPID=69b5812e6ce8454880c3b5c2df4ff820; UM_distinctid=17231c376803fe-0f1a4a33732fd3-d373666-144000-17231c376817c5; ne_analysis_trace_id=1589973123713; NTES_hp_textlink1=old; pgr_n_f_l_n3=7c473844b35fc7e515899738210615664; vinfo_n_f_l_n3=7c473844b35fc7e5.1.0.1589972790059.0.1589973872798'
}
for i in range(2, 6):
    url = f'https://temp.163.com/special/00804KVA/cm_yaowen20200213_0{i}.js?callback=data_callback'
    # print(url)
    response = requests.get(url=url, headers=headers).text
    # print(response)
    title_rst = re.findall('"title":"(.*?)"', response, re.S)
    channelname_rst = re.findall('"channelname":"(.*?)"', response, re.S)
    imgurl_rst = re.findall('"imgurl":"(.*?)"', response, re.S)
    label_rst = re.findall('"label":"(.*?)"', response, re.S)
    source_rst = re.findall('"source":"(.*?)"', response, re.S)
    tlastid_rst = re.findall('"tlastid":"(.*?)"', response, re.S)
    tlink_rst = re.findall('"tlink":"(.*?)"', response, re.S)
    # print(tlink_rst)
with open('data.json', mode='w', encoding='utf-8') as f:
    for i in range(0, len(title_rst)):
        f.write(title_rst[i] + channelname_rst[i] + imgurl_rst[i] + label_rst[i] + source_rst[i] + tlastid_rst[i] + tlink_rst[i] + '\n')

# for link in tlink_rst:
#     response = requests.get(url=link, headers=headers).text
#     content = re.findall('<p class="otitle".*?<p>(.*?)</p>', response, re.S)
#     print(content)