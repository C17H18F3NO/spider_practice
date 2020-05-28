import requests
import parsel


def download_video(page_url):
    response = requests.get(page_url)
    sel = parsel.Selector(response.text)
    video_url = sel.re('srcUrl="(.*?)"')
    video_name = sel.re('<h1 class="video-tt">(.*?)</h1>')

    print(video_url, video_name)

    response = requests.get(video_url[0])
    with open(video_name[0] + '.mp4', mode='wb') as f:
        f.write(response.content)


response = requests.get('https://www.pearvideo.com/category_2')
print(response.text)
sel = parsel.Selector(response.text)
video_list = sel.re('<a href="(video_\d+)" class="vervideo-lilink actplay">')
for url in video_list:
    print(video_list)
    download_video(page_url='https://www.pearvideo.com/' + url)