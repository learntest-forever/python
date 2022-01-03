# -*- encoding=utf-8 -*-
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

def get_distance():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\mucai.png",200,0.8)
    print("mucai :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhongxiny.png",200,0.8)
    print("zhongxiny :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)

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
    pyautogui.moveTo(1,1,duration=0.3)
    
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
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
        print("new_role_next :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            num = num + 1
            print("num is: ",num)
            if num >= 7 :
                point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\1_5.png",30,0.8)
                print("1_5 出现问答 :",point_infos)
                if point_infos != None:
                    time.sleep(1)          
                    break
  
    answer_quest()

    while True:
        for i in range(2):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
            print("new_role_next :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quedingxuanze.png",200,0.8)
        print("quedingxuanze :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(5)
            break
    while True:
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jinruluanshi.png",200,0.8)
        print("jinruluanshi :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qingchongxinshuru.png",50,0.8)
            print("qingchongxinshuru :",point_infos)
            if point_infos != None:
                point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\suiji.png",30,0.8)
                if point_infos != None:
                    print("suiji :",point_infos)
                    find_click(point_infos)
                    continue
            else:
                break
    # for i in range(3):
    while True:
        for i in range(5):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",50,0.8)
            print("new_role_next :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(5)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jiangdong.png",50,0.8)
        print("jiangdong :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(1)
            break
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\ruzhu.png",200,0.8)
    print("ruzhu :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(40)
        while True:
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jinruchangjingzhong.png",100,0.8)
            print("jinruchangjingzhong :",point_infos)
            if point_infos != None:
                # 发送告警通知，人工介入
                # while True:
                print("当前服务器已满或其他原因无法进入，请输入您的选择：1：跳过此步；2：继续查找")
                choice_op = getinput(20)
                if choice_op == "1":
                    break
            else:
                break
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xiayibu.png",200,0.8)
    print("xiayibu :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(5)
    while True:
        for i in range(6):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",50,0.8)
            print("new_role_next :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(5)
        # zhaomu_hong 改为zhaomu_wuhong
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu_wuhong.png",50,0.8)
        print("zhaomu_wuhong :",point_infos)
        if point_infos != None:
            break

    zhaomu_shouci()

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
    print("new_role_next :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)    
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xuanzezhucheng.png",200,0.8)
    print("xuanzezhucheng :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\rucheng.png",200,0.8)
    print("rucheng :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)    
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dianjibianzhibudui.png",200,0.8)
    print("dianjibianzhibudui :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)

    for i in range(2):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\peizhiwujiang.png",200,0.8)
        print("peizhiwujiang :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)         
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\shangzhen.png",200,0.8)
        print("shangzhen :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)       
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\kuaisufenbing.png",200,0.8)
    print("kuaisufenbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\querenfenbing.png",200,0.8)
    print("querenfenbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",200,0.8)
    print("fanhui :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",200,0.8)
    print("fanhui_2 :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
    print("new_role_next :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    
    # 新手引导 占领空地
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\mucai.png",200,0.8)
    print("mucai :",point_infos)
    if point_infos != None:
        dest_node = gen_destnode(point_infos.left, point_infos.top + 266, point_infos.width, point_infos.height)
        print("空地： ", dest_node)
        start_mnq(dest_node[0],dest_node[1])
        pyautogui.moveTo(1,1,duration=0.3)
        time.sleep(2)   
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\gongzhan.png",200,0.8)
    print("gongzhan :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\daiming.png",200,0.8)
    print("daiming :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\gongzhan_2.png",200,0.8)
    print("gongzhan_2 :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(20)
        # 攻占后如果等待100秒，可以不点击跳过按钮
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\tiaoguo.png",200,0.8)
        print("tiaoguo  :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(15)
        else:
            time.sleep(80)


    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qushou.png",200,0.8)
    print("qushou  :",point_infos)
    if point_infos != None:
        dest_node = gen_destnode(point_infos.left, point_infos.top -70, point_infos.width, point_infos.height)
        start_mnq(dest_node[0],dest_node[1])
        pyautogui.moveTo(1,1,duration=0.3)
        time.sleep(3)
        # # 查看文字取首与资源图标top的间隔距离
        # point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\ziyuan.png",200,0.8)
        # print("ziyuan  :",point_infos)
    while True:
        for i in range(2):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
            print("new_role_next  :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\huicheng.png",200,0.8)
        print("huicheng  :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(23)
            break

    while True:
        for i in range(10):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",50,0.8)
            print("new_role_next  :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)
            if i == 3:
                time.sleep(4)
            if i == 4:
                time.sleep(16)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xuanzezhucheng.png",30,0.8)
        print("xuanzezhucheng :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            break

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\rucheng.png",200,0.8)
    print("rucheng :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\bingzhongqibing.png",200,0.8)
    print("bingzhongqibing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\bingzhongxuanze.png",200,0.8)
    print("bingzhongxuanze :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)      
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qiangbing.png",200,0.8)
    print("qiangbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)   


    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",200,0.8)
    print("fanhui :",point_infos)
    if point_infos != None:
        time.sleep(2)
        find_click(point_infos)        
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",200,0.8)
    print("fanhui_2 :",point_infos)
    if point_infos != None:
        time.sleep(2)
        find_click(point_infos)

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
    print("new_role_next  :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)    
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xuanzemubiaolingdi.png",200,0.8)
    print("xuanzemubiaolingdi  :",point_infos)
    if point_infos != None:
        dest_node = gen_destnode(point_infos.left + 222, point_infos.top, point_infos.width, point_infos.height)
        start_mnq(dest_node[0],dest_node[1])
        pyautogui.moveTo(1,1,duration=0.3)
        time.sleep(2)
    # # 根据义军找到对应left,计算left距离
    # point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\yijun.png",200,0.8)
    # print("yijun  :",point_infos)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xingjun.png",200,0.8)
    print("xingjun  :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\daiming.png",200,0.8)
    print("daiming :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xingjun_2.png",200,0.8)
    print("xingjun_2 yuan :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(20)
        # 攻占后如果等待100秒，可以不点击跳过按钮
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\tiaoguo.png",50,0.8)
        print("tiaoguo  :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(20)
        else:
            time.sleep(80)

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
    print("new_role_next  :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)    

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\huicheng.png",200,0.8)
    print("huicheng  :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(15)    
    while True:
        for i in range(4):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",50,0.8)
            print("new_role_next  :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)    
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaocheng_dianjifanhui.png",200,0.8)
        print("点击其他区域返回 :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            break
    while True:
        for i in range(3):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",100,0.8)
            print("new_role_next  :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)    

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xuanzezhucheng.png",100,0.8)
        print("xuanzezhucheng :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            break
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\rucheng.png",200,0.8)
    print("rucheng :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\bingzhongqiangbing.png",200,0.8)
    print("bingzhongqiangbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xiazhen.png",200,0.8)
    print("xiazhen :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\queren.png",200,0.8)
    print("queren :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\peizhiwujiang_jiahao.png",200,0.8)
    print("peizhiwujiang_jiahao :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\shangzhen.png",200,0.8)
    print("shangzhen :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\kuaisufenbing.png",200,0.8)
    print("kuaisufenbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\querenfenbing.png",200,0.8)
    print("querenfenbing :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)  


    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",200,0.8)
    print("fanhui :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)         
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",200,0.8)
    print("fanhui_2 :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)          

    while True:
        for i in range(4):
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",50,0.8)
            print("new_role_next  :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(3)
        time.sleep(5)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\yimunanfu.png",200,0.8)
        print("yimunanfu :",point_infos)
        if point_infos != None:
            time.sleep(5)
            find_click(point_infos)
            time.sleep(2)
            break

    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qianwangjiaru_tongmeng.png",30,0.8)
    print("qianwangjiaru_tongmeng :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\shenqingjiaru_tongmeng.png",30,0.8)
        print("shenqingjiaru_tongmeng :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",30,0.8)
            print("fanhui_2 :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(2)   
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\queren.png",30,0.8)
    print("queren :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    zhaomu()

def answer_quest():
    num = 0
    while True:
        print("answer times: ",num)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\1_5.png",30,0.8)
        print("1_5 :",point_infos)
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(3)

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\2_5.png",30,0.8)
        print("2_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(3)

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\3_5.png",30,0.8)
        print("3_5 :",point_infos)   
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(3)

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\4_5.png",30,0.8)
        print("4_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(3)

        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\5_5.png",30,0.8)
        print("5_5 :",point_infos)      
        if point_infos != None:
            dest_node = gen_destnode(point_infos.left, point_infos.top-300, point_infos.width, point_infos.height)
            start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(3)
        num = num + 1    
        if num >= 1:
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",30,0.8)
            print("new_role_next 已回答完成5题 :",point_infos)
            if point_infos != None:
                break  
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
        pyautogui.moveTo(1,1,duration=0.3)

def zhaomu_shouci():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu_wuhong.png",200,0.8)
    print("zhaomu_wuhong :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(3)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\mingjiang_hong.png",200,0.8)
        # point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\pk_mingjiang.png")
        print("mingjiang_hong :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu2_free.png",200,0.8)
            print("zhaomu2_free :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(3)
                zhaomu_lan_shouci()
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",200,0.8)
    for i in range(2):
        print("fanhui :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)



def zhaomu():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu_hong.png",20,0.8)
    print("zhaomu_hong :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(3)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\mingjiang_hong.png",20,0.8)
        # point_infos = find_pic_10(r"D:\code\mypython\python\sgz\picture\pk_mingjiang.png")
        print("mingjiang_hong :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu1_free.png",20,0.8)
            print("zhaomu1_free :",point_infos)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(3)
                zhaomu_cheng()
                point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaomu1_half.png",20,0.8)
                print("zhaomu1_half :",point_infos)
                if point_infos != None:
                    find_click(point_infos)
                    time.sleep(1)
                    point_infos_buzu = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jinzhubuzu.png",20,0.8)
                    print("jinzhubuzu :",point_infos_buzu)
                    if point_infos_buzu != None:
                        find_click(point_infos)
                    else:
                        time.sleep(3)
                        zhaomu_cheng()
    fanhui()

def fanhui():
    for i in range(2):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",30,0.8)
        print("fanhui :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)

def fanhui_1_2():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",30,0.8)
    print("fanhui :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",30,0.8)
    print("fanhui_2 :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)

def zhaomu_lan_shouci():
    # 招募后判断是否出现下一步按钮，招募到橙有交互
    for i in range(2):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\next.png",50,0.8)
        print("next :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaocheng_dianjifanhui.png",200,0.8)
        print("点击其他区域返回 :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)

def zhaomu_cheng():
    # 招募后判断是否出现下一步按钮，招募到橙有交互
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\next.png",50,0.8)
    print("next :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(3)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhaocheng_dianjifanhui.png",50,0.8)
        print("点击其他区域返回 :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)
    else:
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",50,0.8)
        print("fanhui :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(3)        

def saodang(level,x,y,team_num):
    pass

def dingwei_zhucheng():
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\dibiao1.png ")
    find_click(point_infos)
    # point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\zhucheng_dingwei.png ")
    # print("主城定位：",point_infos)
    # find_click(point_infos)
    time.sleep(2)
    dest_node = gen_destnode(point_infos.left, point_infos.top + 34, point_infos.width, point_infos.height)
    start_mnq(dest_node[0],dest_node[1])
    pyautogui.moveTo(1,1,duration=0.3)
    time.sleep(2)
    point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\rucheng.png ")
    print("rucheng : ",point_infos )
    find_click(point_infos)
    time.sleep(2)

def chengjian():
    dingwei_zhucheng()
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\chengjian.png",20,0.8)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
    else:
        return
    for i in range(6):
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\sheng.png",20,0.9)
        print("sheng 可升级建设坐标 is: ",point_infos)
        if point_infos != None:
            find_click(point_infos)
        if point_infos != None:
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\shengji.png",20,0.8)
            if point_infos != None:
                find_click(point_infos)
            else:
                point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jianzao.png",20,0.8)
                if point_infos != None:
                    find_click(point_infos)                
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\meiyouduilie.png",30,0.8)
            if point_infos != None:
                print("meiyouduilie")
                time.sleep(10)
                break
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\queren.png",20,0.8)
            if point_infos != None:
                find_click(point_infos)
                time.sleep(1)
        else:
            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\junshi.png",20,0.8)
            print("junshi is: ",point_infos)
            find_click(point_infos)
            time.sleep(2) 
    fanhui_1_2()            

def get_zhucheng():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao_zuobiao.png",20,0.8)
    print("dibiao_zuobiao: ",point_infos)
    if point_infos != None:
        find_click(point_infos)
        # 地标与主城坐标距离 通过查下获取差值，将插值作为“地标的”偏移量获取主城坐标位置
        dest_node = gen_destnode(point_infos.left-122, point_infos.top + 50, 77, 25)
        print("zhucheng_zuobiao: ",dest_node)
        # 截图指定区域，并做文字识别获取字符串
        im = pyautogui.screenshot(region=(point_infos.left - 122,point_infos.top + 50, 77, 28))
        im.save(r"D:\code\mypython\python\sgz\picture\zuobiao_to_str.png")
        time.sleep(1)
        text = pytesseract.image_to_string(Image.open(r"D:\code\mypython\python\sgz\picture\zuobiao_to_str.png"))
        print(text)
        zuobiao_xy = text[1:][:-2]
        zuobiao_x = zuobiao_xy.split(",")[0]
        zuobiao_y = zuobiao_xy.split(",")[1]
        return(int(zuobiao_x),int(zuobiao_y))

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


        # point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\zhucheng_zuobiao.png",20,0.8)
        # print("zhucheng_zuobiao: ",point_infos)
        # time.sleep(2)
        # find_click(point_infos)              

        #     dest_node = gen_destnode(point_infos.left, point_infos.top -70, point_infos.width, point_infos.height)
        #     start_mnq(dest_node[0],dest_node[1])

        # login()
        # new_role()
        # zhaomu()
        # chengjian()
        # get_zhucheng()
        xy = get_zhucheng()
        print(xy[0],xy[1])

        # for i in range(5):
        #     point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\new_role_next.png",200,0.8)
        #     print("new_role_next  :",point_infos)
        #     if point_infos != None:
        #         find_click(point_infos)
        #         time.sleep(2)


        # first login
        point_infos = find_pic(r"D:\code\mypython\python\sgz\picture\xuanze.png")
        if point_infos == None:
            print("not first login")
        else:
            pass


        print("game script End")

        # close_application()