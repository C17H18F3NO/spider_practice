"""
使用selenium或者pyppeteer访问下面这个网站
https://www.wjx.cn/jq/78696684.aspx

1. 将所有的单选题随机选择
2. 所有的多选题随机选择两个
3. 填空题随便填入一句话
4. 点击提交按钮之前,让人进行选择是否提交
"""
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--headless')
#
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
# driver.get('https://www.wjx.cn/jq/78696684.aspx')
# sleep(10)
# html = driver.page_source
# with open('wjx.html', 'w') as f:
#     f.write(html)

driver = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://www.wjx.cn/jq/78696684.aspx'
driver.get(url)


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 22, 28]:
    simple_sel = driver.find_elements_by_css_selector(f'#divquestion{i} ul li label')
    simple_sel[random.randint(0, len(simple_sel) - 1)].click()
    sleep(1)
for j in [12, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]:
    multiple_sel = driver.find_elements_by_css_selector(f'#divquestion{j} ul li label')
    k = random.randint(2, len(multiple_sel) - 1)
    while k:
        multiple_sel[random.randint(0, len(multiple_sel) - 1)].click()
        sleep(1)
        k -= 1
        if k == -1:
            break
fill_blank = driver.find_element_by_css_selector('#divquestion29 textarea')
fill_blank.send_keys('hello world')
c = input('请输入1或0（1表示提交，0表示不提交）：')
if c == 1:
    submit = driver.find_element_by_id('submit_table')
input()
driver.quit()