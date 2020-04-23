
import os
import tkinter as tk
from tkinter import filedialog


#  文件保存  弹窗选择文件夹
def dir():
    root = tk.Tk()
    root.withdraw()
    print(root)

    # FPath = filedialog.askopenfilename()
    # print(FPath)

    #获取选择的文件夹
    dir = filedialog.askdirectory()
    #print("dir",dir)


    # 判断有没有选择路径，没有选择则返回默认路径
    if dir != '':
        a = ''
        dirs = dir.split('/')
        for aa in dirs:
            a += aa + '\\'
        return a
        print('保存文件夹路径', a)
    else:
        #判断桌面路径是否存在，存在直接返回，不存在则创建
        if not os.path.exists('C:\\Users\\Administrator\\Desktop\\网易云音乐'):
            os.makedirs('C:\\Users\\Administrator\\Desktop\\网易云音乐')
            return 'C:\\Users\\Administrator\\Desktop\\网易云音乐\\'
        else:
            return 'C:\\Users\\Administrator\\Desktop\\网易云音乐\\'


