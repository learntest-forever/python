# -*- encoding=utf-8 -*-
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

def open_application():
    os.startfile(r'D:\soft\xyaz\Microvirt\MEmu\MEmuConsole.exe')
    time.sleep(10)
def close_application():
    os.system("taskkill /F /IM MEmuConsole.exe")
def start_mnq(x,y):
    pyautogui.leftClick(x=x,y=y,duration=0.5)
def start_sgzapp():
    # 找到sgz-jy的模拟器，多个时需要确认同一排即y相差不大
    sgz_path = r"D:\code\mypython\python\sgz\picture\sgz-jy.png"
    pointinfo_sgz = find_pic(sgz_path)
    # 找到启动按钮
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\start.png")
    # point_infos = (pointinfo_sgz.left + 400, pointinfo_sgz.top, point_infos.width, point_infos.height)
    dest_node = gen_destnode(pointinfo_sgz.left + 399, pointinfo_sgz.top, point_infos.width, point_infos.height)
    start_mnq(dest_node[0],dest_node[1])
    
    # time.sleep(20)
    # 查找sgz_app并启动
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\sgz_app.png")
    print("sgz_app is :",point_infos)
    find_click(point_infos)
    time.sleep(40)
    # 选择点击进入
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\dian.png")
    print("dian is :",point_infos)
    find_click(point_infos)
    time.sleep(20)

def login(username,passwd,zoneid,name):
    pass

def new_role():
    # time.sleep(20)
    num = 0
    while True:
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",20,0.8)
        print("new_role_next :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            num = num + 1
            print("num is: ",num)
            if num == 7:
                break

    answer_quest()

    for i in range(2):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",20,0.8)
        print("new_role_next :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quedingxuanze.png",20,0.8)
    print("quedingxuanze :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)    
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jinruluanshi.png",20,0.8)
    print("jinruluanshi :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    for i in range(3):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",20,0.8)
        print("new_role_next :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(5)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jiangdong.png",20,0.8)
    print("jiangdong :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\ruzhu.png",20,0.8)
    print("ruzhu :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jinruchangjingzhong.png",20,0.8)
        print("jinruchangjingzhong :",point_infos)
        if point_infos == None:
            # 发送告警通知，人工介入
            print("当前服务器已满，请更换选择")


def answer_quest():
    num = 0
    while True:
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\1_5.png",20,0.8)
        print("1_5 :",point_infos)
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\2_5.png",20,0.8)
        print("2_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\3_5.png",20,0.8)
        print("3_5 :",point_infos)   
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\4_5.png",20,0.8)
        print("4_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\5_5.png",20,0.8)
        print("5_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])

        num = num + 1
        if num >= 5:
            break

def qianwang():
    # 选择前往征战
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\qianwang.png")
    print("goto is :",point_infos)
    find_click(point_infos)
    time.sleep(10)


def getinput(timeout=10):
    pass
    start_time=time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            input = msvcrt.getwche()
        if len(input) != 0 or (time.time()-start_time > timeout):
            break
    if len(input) > 0:
        return (input)
    else:
        return ("2")

# 一直查下，查下10次后等待用户输入选择操作,含超时时间
def find_pic(picture_path):
    i = 1
    while True:
        point_info = pyautogui.locateOnScreen(picture_path,confidence=0.8)
        if point_info != None:
            print(point_info)
            return point_info
        elif point_info == None and i >= 10:
            # 发送告警消息，钉钉
            print("未找到指定图片,请输入您的选择：1：跳过此步；2：继续查找")
            choice_op = getinput(10)
            if choice_op == "1":
                break
            else:
                i = 1
                print("10次未找到，继续下一轮查下")
                continue 
        else:
            i = i + 1
            continue
    return None

# 一直查下，查下10次后等待用户输入选择操作
def find_pic_old(picture_path):
    # grayscale 是否转灰度
    # point_info = pyautogui.locateCenterOnScreen(r"D:\code\mypython\python\sgz\picture\txsp.png",grayscale=True)
    i = 1
    while True:
        point_info = pyautogui.locateOnScreen(picture_path,confidence=0.8)
        # point_info = pyautogui.locateCenterOnScreen(picture_path,grayscale=True,confidence=0.9)   
        if point_info == None:
            # time.sleep(1)
            i = i + 1
            continue
        elif i > 10:
            print("未找到指定图片")
            time.sleep(10)
            choice_op = input("请选择要执行的操作编号1或2：1：跳过此步；2：继续查找")
            if choice_op == "1":
                break
            else:
                i = 1
                continue 
        else:
            print(point_info)
            return point_info

# 查下10次，查不到返回None
def find_pic_10(picture_path):
    i = 1
    for i in range(10):
        point_info = pyautogui.locateOnScreen(picture_path,confidence=0.9)
        if point_info == None:
            i = i + 1
            continue
        elif i >= 10:
            print("10次未找到指定图片")
            break
        else:
            print(point_info)
            return point_info
    return None

def find_pic_num_confidence(picture_path,num,confidence):
    i = 1
    for i in range(num):
        point_info = pyautogui.locateOnScreen(picture_path,confidence=confidence)
        if point_info == None:
            i = i + 1
            continue
        elif i >= num:
            print(num,"次未找到指定图片")
            break
        else:
            print(point_info)
            return point_info
    return None

def find_pic_all(picture_path):
    i = 1
    for pointinfo in pyautogui.locateAllOnScreen(picture_path,confidence=0.8):
        if pointinfo == None:
            i = i + 1
            continue
        elif i > 10:
            print("未找到指定图片")
            time.sleep(10)
            choice_op = input("请选择要执行的操作编号1或2：1：跳过此步；2：继续查找")
            if choice_op == "1":
                break
            else:
                i = 1
                continue 
        else:
            print(pointinfo)


def gen_destnode(left,top,width,height):
    return(left + random.random()*width, top + random.random()*height)

def find_click(point_infos):
    if point_infos == None:
        print("未找到对应图片，请确认")
    else:
        dest_node = gen_destnode(point_infos.left,point_infos.top,point_infos.width,point_infos.height)
        start_mnq(dest_node[0],dest_node[1])

def zhaomu():
    point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\zhaomu_hong.png")
    print("zhaomu_hong :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\mingjiang_hong.png")
        # point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\pk_mingjiang.png")
        print("mingjiang_hong :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\zhaomu1_free.png")
            print("zhaomu1_free :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                zhaomu_cheng()
                point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\zhaomu1_half.png")
                print("zhaomu1_half :",point_infos)
                if point_infos != None:
                    find_click(point_infos)
                    zhaomu_cheng()

def zhaomu_cheng():
    # 招募后判断是否出现下一步按钮，招募到橙有交互
    point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\next.png")
    print("next :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\zhaocheng_dianjifanhui.png")
        print("招募到橙，点击其他区域返回 :",point_infos)
        if point_infos != None:
            find_click(point_infos)

def saodang(level,x,y,team_num):
    pass

def dingwei_zhucheng():
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\dibiao1.png ")
    find_click(point_infos)
    # point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\zhucheng_dingwei.png ")
    # print("主城定位：",point_infos)
    # find_click(point_infos)
    time.sleep(1)
    dest_node = gen_destnode(point_infos.left, point_infos.top + 34, point_infos.width, point_infos.height)
    start_mnq(dest_node[0],dest_node[1])
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\rucheng.png ")
    print("rucheng : ",point_infos )
    find_click(point_infos)

def chengjian():
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\chengjian.png ")
    find_click(point_infos)    
    point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\sheng.png ")
    print("sheng 可升级建设坐标 is: ",point_infos)
    # find_click(point_infos)
    if point_infos != None:
        point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\shengji.png ")
        find_click(point_infos)
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\meiyouduilie.png")
        if point_infos != None:
            time.sleep(10)     
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\shengji_queren.png ")
        find_click(point_infos)
        
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\junshi.png ")
    print("junshi is: ",point_infos)
    find_click(point_infos)
    point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\sheng.png ")
    print("sheng 可升级建设坐标 is: ",point_infos)
    # find_click(point_infos)     
    if point_infos != None:
        point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\shengji.png ")
        find_click(point_infos)
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\meiyouduilie.png")
        if point_infos != None:
            time.sleep(10)     
        point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\shengji_queren.png ")
        find_click(point_infos)

if __name__=="__main__":
    time.sleep(5)

    # # 打开模拟器
    # open_application()
    # time.sleep(10)
    # # 打开sgz_app
    # start_sgzapp()
    # qianwang()

    # time.sleep(5)
    zhaomu_time = 0
    while True:
        # time_now = time.time()
        # if time_now - zhaomu_time >= 3600:
        #     zhaomu_time = time_now
        #     zhaomu()
        #     print("zhaomu end")

        # # point_infos = find_pic("zhucheng_logo.png ")
        # # find_click(point_infos)

        # dingwei_zhucheng()
        # chengjian()
        new_role()

        # first login
        point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\xuanze.png")
        if point_infos == None:
            print("not first login")
        else:
            pass


        print("game script End")

        # close_application()