# TK 如果出现错误会返回一个消息
import tkinter.messagebox as msgbox
# 做桌面编程的
import tkinter as tk
# 正则表达式
import re

import wangyiyun
import web

class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '网易云音乐下载助手'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='暂时只有一个音乐通道：', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='唯一通道', variable=self.v, value=1, width=10, height=3)
        lable = tk.Label(frame_2, text='请输入音乐连接：')

        # 输入框声明
        # entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        entry = tk.Entry(frame_2, textvariable=self.url, highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='下载', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
        #etb  = tk.Button(frame_2, text='退出', font=('楷体', 12), fg='Purple', width=2, height=1, command=framet.quit)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()

        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def video_play(self):

        # 正则表达式判定是否为合法连接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            # 拿到用户输入的网址
            # 调用下载方法
            ip = self.url.get()
            #网易云音乐
            xy =  wangyiyun.down(ip)
            if xy == 'successful':
                msgbox.showerror(title='下载成功', message='下载成功！！！继续或关闭')
            else:
                msgbox.showerror(title='响应失败', message='网页响应失败，响应码:{0}'.format(xy))
        else:
            msgbox.showerror(title='错误', message='音乐链接地址无效，请重新输入！')

    # 启动GUI程序的函数
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    print('打开网页')
    web.webs()
    app = APP()
    app.loop()