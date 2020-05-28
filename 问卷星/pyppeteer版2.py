import asyncio
from pyppeteer import launch
import random


async def main():
    browser = await launch({
        'executablePath': 'F:\\BaiduNetdiskDownload\\chrome-win\\chrome.exe',
        'headless': False
    })
    page = await browser.newPage()
    await page.setViewport(viewport={'width': 1280, 'height': 800})
    await page.goto('https://www.wjx.cn/jq/78696684.aspx')
    simple_sel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 21, 27]
    multiple_sel = [11, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26]
    await asyncio.sleep(10)
    # 提取29个题目
    elements = await page.querySelectorAll('.div_question')

    for i in simple_sel:
        try:
            # 列表里面存放的是元素
            lis = elements[i].querySelectorAll('ul li')
            print(lis)
            # 随机选择一个元素
            li = random.choice(lis)
            li.click()
        except:
            pass
    #
    # for j in multiple_sel:
    #     try:
    #         lis = elements[j].querySelectorAll('ul li')
    #         # choice可能重复 sample不会,k=2选取两个
    #         li = random.sample(lis, k=2)
    #         for l in li:
    #             l.click()
    #     except:
    #         pass
    #
    # await page.type('#divquestion29 textarea', 'hello world')
    #
    # c = input('请输入1或0（1表示提交，其他表示不提交）：')
    # if c == 1:
    #     await page.querySelectorAll('submit_table')
    # else:
    #     await page.close()
    #
asyncio.get_event_loop().run_until_complete(main())