import bs4
import requests
import wordcloud
from tkinter import *
from tkinter import messagebox
import time
import json

from openpyxl import Workbook, load_workbook
import collections
import matplotlib.pyplot as plt  #导入matplotlib.pyplot模块，别名取为plt
import numpy as np          #导入numpy库，别名起为np

import pylab
from scipy import interpolate
from matplotlib.font_manager import FontProperties
import jieba
from wordcloud import WordCloud
import PIL.Image as image
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import jieba
import matplotlib.pyplot as plt # 画图的包
from pylab import mpl  # 设置图形中字体样式与大小的包
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.size'] = 6.0
from collections import Counter # 计算列表中元素的包
from wordcloud import WordCloud # 词云包
import pandas as pd
#引用的库太多，搞来搞去删删改改 我也迷了  不改了都放上把


def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    res = requests.get(url, headers=headers)
    
    
    return res
def main():
    BV=e1.get()
    url='http://api.bilibili.com/x/web-interface/view?bvid=%s'%BV
    a=get_html(url)

    data=a.json()
    list_=data.get('data')
    cid=list_['pages'][0]['cid']
    url2='http://api.bilibili.com/x/v1/dm/list.so?oid=%s'%cid
    danmulist=get_html(url2)
    data=danmulist.content.decode('utf-8')
    soup = bs4.BeautifulSoup(data, 'lxml')
    result=soup.find_all('d')
    danmu=''
    danmudic={}
    n=1
    for i in result:
        a=i.text
        if a in danmudic:
            n+=1
        else:
            n=1
        danmudic[a]=n
        danmu+=a
        danmu+=','
    wc=wordcloud.WordCloud(font_path=r'C:\Windows\Font\simfang.ttf',background_color='white',height=800,width=1000)
    wc.generate(danmu)
    image=wc.to_image()
    def show():
        image.show()
    danmu_=sort