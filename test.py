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