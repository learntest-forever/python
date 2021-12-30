# -*- encoding=utf-8 -*-
import pyautogui
import os
import win32api
# import psreadline
import time
import random
# import cv2

def open_application():
    # os.startfile(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    os.startfile(r'D:\soft\xyaz\Microvirt\MEmu\MEmuConsole.exe')
    # os.startfile(r'D:\soft\xyaz\Microvirt\MEmu\MEmu.exe')
    # win32api.ShellExecute(0,'open',r'C:\Program Files\Mozilla Firefox\firefox.exe','','',1)
def close_application():
    os.system("taskkill /F /IM MEmuConsole.exe")
def start_mnq(x,y):
    pyautogui.leftClick(x=x,y=y,duration=0.5)

def login(username,passwd,zoneid,name):
    pass

def find_pic(picture_path):
    # grayscale 是否转灰度
    # point_info = pyautogui.locateCenterOnScreen(r"D:\code\mypython\python\txsp.png",grayscale=True)
    for i in range(20):
        point_info = pyautogui.locateOnScreen(picture_path)
        # point_info = pyautogui.locateOnScreen(picture_path,confidence=0.8)
        # point_info = pyautogui.locateCenterOnScreen(picture_path,grayscale=True)
        # point_info = pyautogui.locateCenterOnScreen(picture_path,grayscale=True,confidence=0.9)   
        if point_info == None:
            # time.sleep(1)
            continue
        elif i == 9:
            print("未找到指定图片")
            return None
        else:
            return point_info

def gen_destnode(left,top,width,height):
    return(left + random.random()*width, top + random.random()*height)

def find_click(point_infos):
    if point_infos == None:
        print("未找到对应图片，清确认")
        time.sleep(10)
        exit()
    else:
        dest_node = gen_destnode(point_infos.left,point_infos.top,point_infos.width,point_infos.height)
        start_mnq(dest_node[0],dest_node[1])

if __name__=="__main__":
    open_application()
    time.sleep(5)

    # sgz_path = r"D:\code\mypython\python\sgz-jy.png"
    # pointinfo_sgz = find_pic(sgz_path)
    point_infos = find_pic(r"D:\code\mypython\python\start.png")
    print("start.png is :",point_infos)
    find_click(point_infos)
    time.sleep(20)

    point_infos = find_pic(r"D:\code\mypython\python\sgz_app.png")
    print("sgz_app is :",point_infos)
    find_click(point_infos)
    time.sleep(30)
    point_infos = find_pic(r"D:\code\mypython\python\dian.png")
    print("dian is :",point_infos)
    find_click(point_infos)
    time.sleep(20)
    point_infos = find_pic(r"D:\code\mypython\python\goto.png")
    print("goto is :",point_infos)
    find_click(point_infos)
    time.sleep(20)
    print("End")

    # close_application()