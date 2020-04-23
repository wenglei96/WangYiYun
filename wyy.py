# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

import os

if __name__ == '__main__':
    # 指定爬取路径
    # 这是网易云音乐歌单的链接，注意 一定要去掉#号
    url = "https://music.163.com/#/playlist?id=4875494884"
    a = url.split('#')

    # 伪造浏览器头部
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Referer': 'http://93.174.95.27',
    }

    # 获取页面相应值
    r = requests.get(a[0]+a[1], headers=header)
    print('页面相应', r.status_code)

    # 页面返回值为200，表示响应成功
    if r.status_code == 200:
        # 获取二进制 html数据
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup)

        # 通过分析网页源代码发现排行榜中的歌曲信息全部放在类名称为 f-hide 的 ul 中
        # 于是根据特殊的类名称查找相应 ul，然后找到里面的全部 a 标签
        songs = soup.find("ul", class_="f-hide").select("a")
        # print(songs)
        # print('获取歌曲数',len(songs))

        # 循环遍历每一个 a 标签
        i = 1
        for s in songs:
            # 获取 歌曲 href 地址    '/song?id=1346474112'
            href = s['href']
            song_id = (href.split('='))[1]
            # 获取歌曲名称
            song_name = s.text
            # 进行URL路径拼接
            song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
            print("第 " + str(i) + " 首歌曲：" + song_down_link)
            print("正在下载...")

            request = requests.get(song_down_link, headers=header).content
            # 判断文件夹是否存在，不存在则创建
            if not os.path.exists('F:\\音乐'):
                os.mkdir('F:\\音乐')

            f = open('F:\\音乐\\' + song_name + ".mp3", 'wb')
            f.write(request)
            f.close()
            print("下载完成！\n\r")
            i = i + 1
    else:
        print('页面响应失败!!!')


