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
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 22, 28]:
        simple_sel = await page.querySelectorAll(f'#divquestion{i} ul li label')
        await random.choice(simple_sel).click()
        await asyncio.sleep(1)
    for j in [12, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27]:
        multiple_sel = await page.querySelectorAll(f'#divquestion{j} ul li label')
        lis = random.sample(multiple_sel, k=2)
        for li in lis:
            await li.click()
    await page.type('#divquestion29 textarea', 'hello world')
    c = input('请输入1或0（1表示提交，其他表示不提交）：')
    if c == 1:
        await page.querySelectorAll('submit_table')
    else:
        await page.close()

asyncio.get_event_loop().run_until_complete(main())
