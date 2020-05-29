import asyncio
from pyppeteer import launch
import random


async def main():
    # launch 方法会新建一个 Browser 对象，然后赋值给 browser
    browser = await launch({
        # 路径就是你刚才解压的驱动的位置
        'executablePath': 'F:\\BaiduNetdiskDownload\\chrome-win\\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器，所以要显示需要给False
        'headless': False
    })
    # 调用 newPage 方法相当于浏览器中新建了一个选项卡，同时新建了一个 Page 对象
    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})
    # Page 对象调用了 goto 方法就相当于在浏览器中输入了这个 URL，浏览器跳转到了对应的页面进行加载，加载完成之后再调用 content 方法，返回当前浏览器页面的源代码
    await page.goto('https://www.wjx.cn/jq/78696684.aspx')
    # 单选题随机选取
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 22, 28]:
        simple_sel = await page.querySelectorAll(f'#divquestion{i} ul li label')
        await random.choice(simple_sel).click()
        await asyncio.sleep(1)
    # 多选题随机选取两个
    for j in [12, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]:
        multiple_sel = await page.querySelectorAll(f'#divquestion{j} ul li label')
        # 这里使用sample而不用choice，因为要避免choice的重复
        lis = random.sample(multiple_sel, k=2)
        for li in lis:
            await li.click()
    # 填空题
    await page.type('#divquestion29 textarea', 'hello world')
    c = input('请输入1或0（1表示提交，其他表示不提交）：')
    if c == 1:
        # 找到提交按钮提交
        await page.querySelectorAll('submit_table')
    else:
        await page.close()

asyncio.get_event_loop().run_until_complete(main())
