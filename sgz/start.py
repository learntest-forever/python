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
from aip import AipOcr

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def my_ocr(filepath):
    image = get_file_content(filepath)
    APP_ID = "22db84bb626d40eaa316c4c58864f26b"
    API_KEY = 'dc4662b5852d420a9d44a1b4e236f528'
    SECRET_KEY = '4b14e073956b42fab33d7e6b435272fe'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    result = client.basicGeneral(image)
    print("my_ocr result is : ",result)
    return result

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
        time.sleep(25)
        # 攻占后如果等待100秒，可以不点击跳过按钮
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\tiaoguo.png",200,0.8)
        print("tiaoguo  :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(15)
        else:
            time.sleep(100)


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

def find_pic_list(picture_path,confidence):
    i = 1
    pointinfos = []
    for pointinfo in pyautogui.locateAllOnScreen(picture_path,confidence=confidence):
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
            pointinfos.append(pointinfo)
            print(pointinfo)
    return pointinfos

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
def fanhui_1():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui.png",30,0.8)
    print("fanhui :",point_infos)
    if point_infos != None:
        find_click(point_infos)
        time.sleep(2)
def fanhui_1_small():
    point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\fanhui_2.png",30,0.8)
    print("fanhui_2 小返回 :",point_infos)
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

        # 偶尔出现坐标最后多一个逗号的情况，需要处理
        start = 0
        end = len(text)-1
        for i in range(len(text)):
            if text[i] == "(":
                start = i+1
            elif text[i] == ")":
                end = len(text)-i
        if ")" not in text:
            end = len(text)
            zuobiao_xy = text[start:]
        else:                
            zuobiao_xy = text[start:][:-end]
        print(zuobiao_xy)

        # zuobiao_xy = text[start:][:end]
        # zuobiao_xy = text[1:][:-2]
        zuobiao_x = zuobiao_xy.split(",")[0]
        zuobiao_y = zuobiao_xy.split(",")[1]
        return(int(zuobiao_x),int(zuobiao_y))

def kuaisu_fenbing(teamnum):
    dingwei_zhucheng()
    teamids = get_teamid()
    # teamnum = len(teamids)
    for i in range(teamnum):
        find_click(teamids[i])
        time.sleep(2)
        point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\kuaisufenbing.png",30,0.9)
        print("kuaisufenbing :",point_infos)
        if point_infos != None:
            find_click(point_infos)
            time.sleep(2)
            point_infos_fenbing = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\querenfenbing.png",30,0.9)
            print("querenfenbing :",point_infos_fenbing)
            if point_infos_fenbing != None:
                find_click(point_infos_fenbing)
                time.sleep(2)
                fanhui_1()
            else:
                find_click(point_infos)
                fanhui_1()
        else:
            fanhui_1()
    fanhui_1_small()


def zhengbing():
    dingwei_zhucheng()
    cha_quxiao = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\cha_quxiaozhengbing.png",50,0.9)
    print("cha_quxiaozhengbing is: ",cha_quxiao)
    if cha_quxiao != None:
        find_click(cha_quxiao)
        time.sleep(1)
        queding = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\queding.png",50,0.9)
        print("queding is: ",queding)
        if queding != None:
            find_click(queding)
            time.sleep(1) 
    zhengbing = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zhengbing.png",50,0.9)
    print("zhengbing is: ",zhengbing)
    if zhengbing != None:
        find_click(zhengbing)
        time.sleep(1)
        zuida = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zuida.png",50,0.9)
        print("zuida is: ",zuida)
        if zuida != None:
            find_click(zuida)
            time.sleep(1)
            kaishizhengbing = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\kaishizhengbing.png",50,0.9)
            print("kaishizhengbing is: ",kaishizhengbing)
            if kaishizhengbing != None:
                find_click(kaishizhengbing)
                time.sleep(1)
                queren = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\queren.png",50,0.9)
                print("queren is: ",queren)
                if queren != None:
                    find_click(queren)
                    time.sleep(1) 
    fanhui_1_small()


def get_teamid():
    team_ids = []
    team_info = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\duiwu_1.png",50,0.9)
    print("team_1 is: ",team_info)
    # pyautogui.moveTo(team_info.left,team_info.top)
    if team_info != None:
        team_ids.append(team_info)
    else:
        return team_ids
    team_info = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\duiwu_2.png",50,0.9)
    print("team_2 is: ",team_info)
    if team_info != None:
        team_ids.append(team_info)
    else:
        return team_ids
    team_info = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\duiwu_3.png",50,0.9)
    print("team_3 is: ",team_info)
    if team_info != None:
        team_ids.append(team_info)
    else:
        return team_ids
    team_info = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\duiwu_4.png",50,0.9)
    print("team_4 is: ",team_info)
    if team_info != None:
        team_ids.append(team_info)
    else:
        return team_ids
    team_info = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\duiwu_5.png",50,0.9)
    print("team_5 is: ",team_info)
    if team_info != None:
        team_ids.append(team_info)
    else:
        return team_ids
    print("teamids : ",team_ids)
    print("team0 x is : ",team_ids[0].left)
    return team_ids

# 输入坐标跳转到指定点
def toxy(x,y):
    print("toxy x,y: ",x,y)
    ditu = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\ditu.png",50,0.8)
    if ditu != None:
        find_click(ditu)
        time.sleep(2)
        # 根据 坐标输入框前的“坐标图标“ 计算坐标偏移量x y
        zuobiao_biaoshi = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zuobiao_biaoshi.png",50,0.9)
        if zuobiao_biaoshi != None:
            print("zuobiao_biaoshi: ",zuobiao_biaoshi)           
            # 输入X 偏移量待确认55是否准确
            dest_node = gen_destnode(zuobiao_biaoshi.left + 55, zuobiao_biaoshi.top, zuobiao_biaoshi.width + 10, zuobiao_biaoshi.height)
            start_mnq(dest_node[0], dest_node[1])
            time.sleep(2)
            wancheng = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\wancheng.png",50,0.8)
            if wancheng != None:
                dest_node = gen_destnode(wancheng.left-400, wancheng.top, wancheng.width, wancheng.height)
                # start_mnq(dest_node[0], dest_node[1])
                pyautogui.leftClick(dest_node[0], dest_node[1])
                pyautogui.mouseDown()
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)
                quanxuan = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quanxuan.png",50,0.8)
                if quanxuan != None:
                    print("quanxuan : ",quanxuan)
                    find_click(quanxuan)
                    time.sleep(1)      
                # print("x del")
                # for i in range(4):
                #     print("backspace",i)
                #     pyautogui.press("backspace",interval=2)
                # time.sleep(1)
                pyautogui.typewrite(message=str(x))
                find_click(wancheng)
                time.sleep(2)

            # 输入Y，偏移量待确认
            dest_node = gen_destnode(zuobiao_biaoshi.left + 165, zuobiao_biaoshi.top, zuobiao_biaoshi.width + 10, zuobiao_biaoshi.height)
            start_mnq(dest_node[0], dest_node[1])
            time.sleep(2)
            wancheng = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\wancheng.png",50,0.8)
            if wancheng != None:
                dest_node = gen_destnode(wancheng.left-400, wancheng.top, wancheng.width, wancheng.height)
                pyautogui.leftClick(dest_node[0], dest_node[1])
                pyautogui.mouseDown()
                time.sleep(2)
                pyautogui.mouseUp()
                time.sleep(1)
                quanxuan = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quanxuan.png",50,0.8)
                if quanxuan != None:
                    print("quanxuan : ",quanxuan)
                    find_click(quanxuan)
                    time.sleep(1)    
                pyautogui.typewrite(message=str(y))
                find_click(wancheng)
                qianwang_xy = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qianwang_xy.png",50,0.9)
                if qianwang_xy != None:
                    find_click(qianwang_xy)
                    time.sleep(3)

def get_landinfo(x,y):
    toxy(x,y)
    # # 通过查找图片，确认地块等级(如果记录类型，需要更多图片 1级木 1级石 1级粮 1级铁，2级...)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\kongdi.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\1ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\2ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\3ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\4ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\5ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\6ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\7ji.png",50,0.8)
    # pointinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\8ji.png",50,0.8)

    # 通过图片识别(需要保证准确性)，确认地块信息：等级 所属 类型 todo
    # 截图中间一定区域内(相对地表获取区域) 保存land_tmp.png, 识别地块信息，根据“级”分割，保存等级和资源类型；
    # 查找关键字图片，攻占（无主或敌方），驻守（己方，友方）----初期不考虑攻占他人与飞地。todo后期优化
    # 如果为资源地，则查询所属（红 蓝 主公，友等图片），写入文件landinfo.txt或写入数据库；
    # x,y,level(0-10,11其他),type(0-6,7其他),who_lock；

    dibiao_zuobiao = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao1.png",20,0.8)
    print("dibiao is: ",dibiao_zuobiao)
    # pyautogui.moveTo(dibiao_zuobiao.left,dibiao_zuobiao.top)
    time.sleep(2)
    # # 地块信息 todo landinfo 待确认位置
    # landinfo = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\landinfo.png",20,0.8)
    # print("landinfo is: ",landinfo)
    # # pyautogui.moveTo(landinfo.left,landinfo.top)
    # time.sleep(2)

    # dibiao is:  Box(left=1258, top=124, width=55, height=15)
    # landinfo is:  Box(left=719, top=144, width=89, height=22)
    # left - 539 , top + 20 

    # 计算偏移量(待确认)，截图地块信息做文字识别
    pyautogui.moveTo(dibiao_zuobiao.left - 539,dibiao_zuobiao.top + 20)
    time.sleep(3)
    pyautogui.moveTo(1,1)
    time.sleep(1)
    tmp_shot = pyautogui.screenshot(region=(dibiao_zuobiao.left - 539,dibiao_zuobiao.top + 20, 89, 22))
    tmp_shot.save(r"D:\code\mypython\python\sgz\picture\tmp_shot.png")
    time.sleep(1)
    # pytesseract ocr 中文包版本待确认；
    # text = pytesseract.image_to_string(Image.open(r"D:\code\mypython\python\sgz\picture\tmp_shot.png"))
    result = my_ocr(r"D:\code\mypython\python\sgz\picture\tmp_shot.png")
    print('''result["words_result"][0]["words"] is : ''', result["words_result"][0]["words"])
    text = str(result["words_result"][0]["words"])
    print(text)
    # 获取信息 0 1 2 3 4 5 6 空 粮 木 石 铁 铜 其他
    for i in range(len(text)):
        if text[i] == "级":
            land_level = int(text[:i])
        if "空地" in text:
            land_level = 0
            land_type = 0            
        elif "粮食" in text:
            land_type = 1
        elif "石料" in text:
            land_type = 2
        elif "木材" in text:
            land_type = 3
        elif "铁矿" in text:
            land_type = 4
        elif "铜矿" in text:
            land_type = 5
        else:
            land_level = 11
            land_type = 6
            
    # who_lock: 0 空，1 自己，2 盟友，3友盟，4 敌对，5 未知
    you = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\you.png",10,0.8)
    if you != None:
        who_lock = 3
        print("you is: ",you)
    # if land_type != 6:
    else:
        lvse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\lvse_zhugong.png",10,0.9)
        if lvse_zhugong != None:
            who_lock = 1
            print("lvse_zhugong is: ",lvse_zhugong)
        else:
            lanse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\lanse_zhugong.png",10,0.9)
            if lanse_zhugong != None:
                who_lock = 2
                print("lanse_zhugong is: ",lanse_zhugong)
            else:
                qianlan_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qianlan_zhugong.png",10,0.8)
                if qianlan_zhugong != None:
                    who_lock = 3
                    print("qianlan_zhugong is: ",qianlan_zhugong)
                else:
                    hongse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\hongse_zhugong.png",10,0.8)
                    if hongse_zhugong != None:
                        who_lock = 4
                        print("hongse_zhugong is: ",hongse_zhugong)
                    else:
                        who_lock = 0
    else:
        who_lock = 5


    mapinfo = [x,y,land_level,land_type,who_lock]
    print("land_level 0-11 空-10级 11未知； land_type 0-6 空 粮 石 木 铁 铜 6未知； who_lock: 0-5 空 自己 盟友 友盟 敌对 5未知")
    print(mapinfo)

def get_land_wholock(x,y,land_level,land_type):
    
    pass

# todo 待截图，计算查询偏移量
def saodang(team_id,x,y):
    toxy(x,y)
    time.sleep(2)
    saodang = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\saodang.png",50,0.8)
    if saodang != None:
        find_click(saodang)
        time.sleep(2)
        xuanzebudui = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\xuanzebudui.png",50,0.7)
        if xuanzebudui != None:
            print("xuanzebudui: ",xuanzebudui)
            time.sleep(2)
            # 获取5个队伍时 绿色"待命"与 "选择部队" 的偏移量
            daimings = find_pic_list(r"D:\code\mypython\python\sgz\picture\daiming_5dui.png",0.7)
            print("daimings: ",daimings)
            if len(daimings) >0:
                daiming_lists = [daimings[0]]
                # for i in range(len(daimings)):
                for j in range(len(daimings)):
                    if daimings[j].left-daiming_lists[-1].left > 200:
                        # print(daimings[j])
                        daiming_lists.append(daimings[j])
                        # pyautogui.moveTo(daimings[j].left,daimings[j].top)
                        # time.sleep(1)
                    else:
                        print("daiming j and i is same points: ",daimings[j])                        
            print("daming_lists is: ",daiming_lists)
            print("team_id is: ",team_id)
            print("team_daiming is: ",daiming_lists[team_id])
            find_click(daiming_lists[team_id])

            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zanshiwufaxingdong.png",50,0.7)
            if point_infos != None:
                print("zanshiwufaxingdong: ",point_infos)
                fanhui_1()
                return

            point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\saodang_2.png",50,0.7)
            if point_infos != None:
                print("saodang_2: ",point_infos)
                find_click(point_infos)
                point_infos = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\jianchichuzheng.png",50,0.7)
                if point_infos != None:
                    print("jianchichuzheng: ",point_infos)
                    find_click(point_infos)
                    time.sleep(60)
                else:
                    time.sleep(60)           
            # "选择部队":  
            # Box(left=719, top=487, width=85, height=17)
            # 5个待命 （队伍数不同相对距离不同）
            # Box(left=373, top=533, width=39, height=19)
            # Box(left=605, top=533, width=39, height=19)
            # Box(left=838, top=533, width=39, height=19)
            # Box(left=1071, top=533, width=39, height=19)
            # Box(left=1303, top=533, width=39, height=19) 
            # 相对距离         
            # xuanzebudui.left-346
            # xuanzebudui.left-114
            # xuanzebudui.left+119
            # xuanzebudui.left+352
            # xuanzebudui.left+584

    


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
        # xy = get_zhucheng()
        # print(xy[0],xy[1])
        # teamids = get_teamid()
        
        # kuaisu_fenbing(2)
        # zhengbing()

        # xy = get_zhucheng()
        # print("xy[0]",xy[0],"xy[1]",xy[1])
        # input_x = xy[0] - 2
        # input_y = xy[1] - 1
        # print("inputx inputy : ",input_x,input_y)
        # toxy(input_x, input_y)

        # saodang(0,input_x, input_y)
        # fanhui_1()
        # kuaisu_fenbing(1)
        # fanhui_1()
        # zhengbing()

        # get_landinfo(x=817,y=946)
        get_landinfo(x=817,y=948)

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