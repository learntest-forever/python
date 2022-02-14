# -*- encoding=utf-8 -*-
from pickle import TRUE
from cv2 import destroyAllWindows
from numpy import datetime_data, true_divide
import pyautogui
import os
import win32api
# import psreadline
import time
import datetime
import random
import msvcrt
# import cv2
from PIL import Image
# import tesseract
import pytesseract
import string
from aip import AipOcr

from sgz.sgz_class.sgz_2021 import Sgz

if __name__ == "__main__":
    sgz_client = Sgz()
    # 获取主城坐标，也可根据主城坐标手动设置x y值；
    # (x,y) = sgz_client.get_zhucheng()
    # print("主城坐标：",x,y)
    # 手动设定主城坐标：x y 
    # x = 1057
    # y = 1362

    # x = 1075
    # y = 1342
    # sgz_client.toxy(x,y)

    # while True:
    #     level = sgz_client.judge_land_level()
        # who_lock = sgz_client.judge_land_lock()
        # print("地块信息 level is ",level,"lock is ",who_lock)
        # time.sleep(5)

    # # 获取地图文件
    # sgz_client.genmap_zhucheng(x,y,2)
    # sgz_client.gen_connect_file()

    # 生成二维数据G 
    G = sgz_client.gen_short()
    
    # sgz_client.gen_route(1433,842,1434,840)

    # sgz_client.find_pic_10()
