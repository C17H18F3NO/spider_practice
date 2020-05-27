"""
    使用python请求此页面：https://www.pearvideo.com/video_1639869 将在获取的文本中会有下面这段内容

    var contId="1639869",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/adshort/20200107/cont-1639869-14773063_adpkg-ad_hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
var player;

    请将其中的视频连接提取出来，并将视频下载到本地。视频名为页面的标题
"""
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


download_video(page_url='https://www.pearvideo.com/video_1639869')

# ctr + r正则表达式
