import random
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://www.wjx.cn/jq/78696684.aspx'
driver.get(url)

simple_sel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 21, 27]
multiple_sel = [11, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26]
fill_blank = [28]
driver.implicitly_wait(10)
# 提取29个题目
elements = driver.find_elements_by_css_selector('.div_question')

for i in simple_sel:
    try:
        # 列表里面存放的是元素
        lis = elements[i].find_elements_by_css_selector('ul li')
        # 随机选择一个元素
        li = random.choice(lis)
        li.click()
    except:
        pass

for j in multiple_sel:
    try:
        lis = elements[j].find_elements_by_css_selector('ul li')
        # choice可能重复 sample不会,k=2选取两个
        li = random.sample(lis, k=2)
        for l in li:
            l.click()
    except:
        pass

for k in fill_blank:
    try:
        textarea = elements[k].find_element_by_css_selector('textarea')
        textarea.send_keys('hello world')
    except:
        pass

c = input('请输入1或0（1表示提交，其它表示不提交）：')
if c == 1:
    submit = driver.find_element_by_id('submit_table')
else:
    driver.quit()