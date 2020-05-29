import random
from selenium import webdriver


# 这里是单选题
def ans_simple(elements):
	# 从提取的29个元素（看下面的main）中选取单选题，比如下面的0就是第一题
    simple_sel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 21, 27]
    for i in simple_sel:
        try:
            # 列表里面存放的是元素 使用css选择器提取
            lis = elements[i].find_elements_by_css_selector('ul li')
            # 随机选择一个元素
            li = random.choice(lis)
            # 点击
            li.click()
        except:
            pass


# 这里是多选题
def ans_multiple(elements):
    multiple_sel = [11, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26]
    for j in multiple_sel:
        try:
            lis = elements[j].find_elements_by_css_selector('ul li')
            # choice可能重复 sample不会,k=2选取两个
            li = random.sample(lis, k=2)
            for l in li:
                l.click()
        except:
            pass


# 这里是填空题
def ans_blank(elements):
    fill_blank = [28]
    for k in fill_blank:
        try:
            textarea = elements[k].find_element_by_css_selector('textarea')
            textarea.send_keys('hello world')
        except:
            pass


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    url = 'https://www.wjx.cn/jq/78696684.aspx'
    driver.get(url)
    # 隐式等待，单位为秒  注意是等页面加载完毕，而不是元素加载，显式等待才是等元素加载
    driver.implicitly_wait(10)
    # 提取29个题目
    elements = driver.find_elements_by_css_selector('.div_question')
    # 执行单选题
    ans_simple(elements)
    # 执行多选题
    ans_multiple(elements)
    # 执行填空题
    ans_blank(elements)
    c = input('请输入1或0（1表示提交，其它表示不提交）：')
    if c == 1:
        submit = driver.find_element_by_id('submit_table')
    else:
        driver.quit()
