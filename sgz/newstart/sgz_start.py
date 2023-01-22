#-*- encoding:utf-8 -*-
# version 2.0.1  20230118

import os
import time
import pyautogui
import msvcrt
import random
import win32gui
import win32process
from goto import with_goto
import json
import requests
import threading
from PIL import Image


pyautogui.FAILSAFE = False
def screencap_dzq(moniqi_line):
    while True:
        device_ipport = "emulator-" + str(5555 + int(moniqi_line[0]) * 2 - 1)
        screen_status = os.system(leidian_path + "adb -s " + device_ipport + " shell screencap -p /sdcard/Pictures/" +  moniqi_line[1] + ".png")
        if screen_status == -1:
            print("emulator not match")
        else:
            print(moniqi_line[1],"emulator screen shot success")
            adb_device_ipport = device_ipport
            return adb_device_ipport

        device_ipport = "127.0.0.1:" + str(5555 + int(moniqi_line[0]) * 2)
        screen_status = os.system(leidian_path + "adb -s " + device_ipport + " shell screencap -p /sdcard/Pictures/" +  moniqi_line[1] + ".png")
        if screen_status == -1:
            print("127.0.0.1 not match")
        else:
            print(moniqi_line[1],"127.0.0.1 screen shot success")
            adb_device_ipport = device_ipport
            return adb_device_ipport
        print("adb can't match emulator or 127.0.0.1")


def open_application():
    # os.startfile(r'D:\soft\xyaz\Microvirt\MEmu\MEmuConsole.exe')
    os.startfile(r'F:\soft\leidian\LDPlayer4\dnmultiplayer.exe')
    time.sleep(10)
def close_application():
    # os.system("taskkill /F /IM MEmuConsole.exe")
    os.system("taskkill /F /IM dnmultiplayer.exe")

def find_pic(picture_path,src_image):
    i = 1
    while True:
        point_info = locateOnScreen_dzq(picture_path,confidence=0.8, src_image=src_image)
        if point_info != None:
            print("找到坐标：",picture_path,point_info)
            return point_info
        elif point_info == None and i >= 10:
            # 发送告警消息，钉钉
            print("未找到指定图片,请输入您的选择：1：跳过此步；2：继续查找",picture_path)
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

def find_pic_confidence(picture_path,confidence,src_image):
    while True:
        point_info = locateOnScreen_dzq(picture_path,confidence=confidence, src_image=src_image)
        if point_info == None:
            print("未找到: ",picture_path)
            continue
        else:
            print("找到坐标：",picture_path,point_info)
            return point_info
    return None

def find_pic_num_confidence(picture_path,num,confidence,src_image):
    i = 1
    for i in range(num):
        point_info = locateOnScreen_dzq(picture_path,confidence=confidence, src_image=src_image)
        if point_info == None:
            i = i + 1
            continue
        elif i >= num-1:
            print(num,"次未找到指定图片: ",picture_path)
            break
        else:
            print("找到坐标：",picture_path,point_info)
            return point_info
    return None

def find_num_on_image(picture_path,num,confidence,src_image,moniqi_line):
    for i in range(num):
        point_info = locateOnScreen_dzq(picture_path,confidence=confidence, src_image=src_image)
        if point_info != None:
            print("找到坐标：",picture_path,point_info)
            xy_result = gen_destnode(point_info.left,point_info.top,point_info.width,point_info.height)
            time.sleep(1)
            return xy_result
        elif i >= num-1:
            print(num,"次未找到指定图片: ",picture_path)
            break
        elif i == int((num-1)/2):
            print(picture_path,i," 次未找到指定图片,重新截图 ")
            screencap_dzq(moniqi_line)         
            time.sleep(5)
        else:
            time.sleep(1)
            continue
    return None

def find_always_on_image(picture_path,confidence,src_image,moniqi_line):
    i = 0
    while True:
        i = i + 1
        point_info = locateOnScreen_dzq(picture_path,confidence=confidence, src_image=src_image)
        if point_info != None:
            print("找到坐标：",picture_path,point_info)
            xy_result = gen_destnode(point_info.left,point_info.top,point_info.width,point_info.height)
            time.sleep(1)
            return xy_result            
        elif i%20 == 0:
            print(picture_path,i," 次未找到指定图片,重新截图 ")
            screencap_dzq(moniqi_line)         
            time.sleep(5)
        else:
            time.sleep(1)
            continue
    # return None

def adb_tap(x,y,adb_device_ipport):
        time.sleep(1)
        adb_result = os.system(leidian_path + "adb -s " + adb_device_ipport + " shell input tap " +  str(x) + " " + str(y))
        return adb_result


def find_on_image_click(picture_path,num,confidence,src_image,moniqi_line):
    adb_device_ipport = screencap_dzq(moniqi_line)
    time.sleep(1)
    if num > 0:
        xy_result = find_num_on_image(picture_path,num,confidence,src_image,moniqi_line)
    else:
        xy_result = find_always_on_image(picture_path,confidence,src_image,moniqi_line)

    if xy_result != None:
        time.sleep(2)
        adb_tap_result = -1
        print(xy_result[0], xy_result[1],adb_device_ipport)
        while adb_tap_result == -1:
            adb_tap_result = adb_tap(xy_result[0], xy_result[1], adb_device_ipport)
            print("adb_tap_result is : ",adb_tap_result)
            




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

def gen_destnode(left,top,width,height):
    return(left + random.random()*width, top + random.random()*height)
def start_mnq(x,y):
    pyautogui.leftClick(x=x,y=y,duration=0.5)
def find_click(point_infos):
    if point_infos == None:
        print("未找到对应图片")
    else:
        time.sleep(1)
        dest_node = gen_destnode(point_infos.left,point_infos.top,point_infos.width,point_infos.height)
        start_mnq(dest_node[0],dest_node[1])
        pyautogui.moveTo(1,1,duration=0.3)

def qidong(picturename):
    # 找到启动按钮
    # point_infos = find_pic(picpath + picturename)
    point_infos = find_pic_confidence(picpath + picturename,0.9)
    print(picturename," 坐标 ",point_infos)
    # dest_node = gen_destnode(point_infos.left + 330, point_infos.top+10, point_infos.width, point_infos.height) 
    # find_click(dest_node)
    start_mnq(point_infos.left+330 , point_infos.top+10 )
    pyautogui.moveTo(1,1,duration=0.3)    

def qidong_backup(picturename):
    # 找到启动按钮
    point_infos = find_pic(picpath + r"\qidong2.png")
    find_click(point_infos)

def start_sgzapp(picturename):
    # 找到sgz-jy的模拟器，多个时需要确认同一排即y相差不大
    # sgz_path = picpath + r"\sgz-jy.png"
    sgz_path = picpath + picturename
    pointinfo_sgz = find_pic(sgz_path)

    # 找到启动按钮
    point_infos = find_pic(picpath + r"\qidong2.png")
    # point_infos = (pointinfo_sgz.left + 400, pointinfo_sgz.top, point_infos.width, point_infos.height)
    # dest_node = gen_destnode(pointinfo_sgz.left + 399, pointinfo_sgz.top, point_infos.width, point_infos.height)
    # dest_node = gen_destnode(pointinfo_sgz.left, pointinfo_sgz.top, point_infos.width, point_infos.height)
    find_click(point_infos)

    # print(dest_node)
    # start_mnq(dest_node[0],dest_node[1])
    start_mnq(point_infos.left,point_infos.top)
    pyautogui.moveTo(1,1,duration=0.3)
    
    time.sleep(60)
    # 查找sgz_app并启动
    point_infos = find_pic(picpath + r"\sgz_app2.png")
    print("sgz_app is :",point_infos)
    find_click(point_infos)
    time.sleep(60)
    # 选择点击进入
    point_infos = find_pic(picpath + r"\dianjijinruyouxi.png")
    print("dian is :",point_infos)
    find_click(point_infos)
    time.sleep(20)

def close_window_name(window_name):
    hld = win32gui.FindWindow(None,window_name)
    print(window_name," 句柄is: ",hld)
    hread_id,process_id = win32process.GetWindowThreadProcessId(hld)
    print(window_name,"进程ID is: ",process_id)    
    return process_id

def killpid(pid):
    cmd = 'taskkill /pid ' + str(pid) + ' /f'
    try:
        os.system(cmd)
    except Exception as e:
        print(e)

def write_taskinfo(filepath,filename,moniqi_status):
    # task_f= open("C:\Users\Administrator\Documents\leidian\Pictures\\"+"taskinfo.txt",appstatus,"w")
    task_f= open(filepath + filename,"w")
    task_f.write(moniqi_status)
    task_f.flush()
    task_f.write("\n")
    task_f.flush()
    task_f.close()


def replace_taskinfo(filepath,filename,childstr):
    task_f= open(filepath + filename,"r+")
    lines = task_f.readlines()
    for i in range(len(lines)):
        if lines[i] == childstr + " closing\n":
            lines[i] = childstr + " close\n"
    task_f.close()
    f_new = open(filepath + filename,"w+")
    f_new.writelines(lines)
    f_new.flush()
    f_new.close()

def leidian_cmd(leidian_cmd):
    result1 = os.popen(leidian_cmd)
    result = result1.read().strip().split("\n")
    result1.close()
    return result

def leidian_cmd_src_result(leidian_cmd):
    result1 = os.popen(leidian_cmd)
    result = result1.read()
    result1.close()
    return result

@with_goto     #必须有
def judge_moniqi_status():
    windows_num = 0
    # current_window_name = []
    for moniqi_info in moniqi_infos:
        label .judgeapp
        f_read = open(filepath + filename,"r",encoding='UTF-8')
        lines = f_read.readlines()
        f_read.close()
        for lineinfo in lines:
            # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            if  "closing" in lineinfo:
                for moniqi_name_kill in moniqi_infos:
                    if moniqi_name_kill[1] in lineinfo:
                        replace_taskinfo(filepath,filename,moniqi_name_kill[1])
                        pro_id = close_window_name(moniqi_name_kill[0])
                        killpid(pro_id)
                        windows_num = windows_num - 1
        
        if windows_num < 2:
            # 雷电 dnconsole 开启模拟器
            leidian_cmd_src_result(leidian_path + "dnconsole launch --name " + moniqi_info[0])
            print("已启动 模拟器 ",moniqi_info[0])
            time.sleep(10)

            # 判断模拟器状态是否已启动完成
            moniqi_online = 0
            while moniqi_online == 0:
                result = leidian_cmd(leidian_path + "dnconsole list2")
                for line in result:
                    moniqi_line = line.split(",")
                    # list2 获取的名字与 配置中模拟器名字一致
                    if moniqi_line[1] == moniqi_info[0]:
                        # 模拟器已启动完成
                        # windows_num = windows_num + 1
                        if moniqi_line[4] == "1":
                            # 雷电 启动按键精灵
                            time.sleep(60)
                            leidian_cmd_src_result(leidian_path + "dnconsole.exe runapp --name " + moniqi_info[0] + " --packagename com.cyjh.mobileanjian")
                            print("已启动 按键精灵 ",moniqi_info[0])
                            # time.sleep(30)
                            time.sleep(3)
                            moniqi_online = 1
                            
                            src_image = screencap_path + moniqi_line[1] + ".png"

                            find_on_image_click(picpath + r"\adb-hulue.png", 20, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            find_on_image_click(picpath + r"\adb-quxiao.png", 20, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            find_on_image_click(picpath + r"\adb-bianxie.png", -1, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            find_on_image_click(picpath + r"\adb-weifenlei.png", -1, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            find_on_image_click(picpath + r"\adb-jiaoben.png", -1, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            find_on_image_click(picpath + r"\adb-jiazai.png", 20, 0.8, src_image, moniqi_line)
                            time.sleep(3)
                            find_on_image_click(picpath + r"\adb-qidong.png", 20, 0.8, src_image, moniqi_line)
                            time.sleep(2)
                            
                            print("按键精灵脚本已启动")
                            break
                        else:
                            print(moniqi_info[0]," 模拟器启动未完成")
                            time.sleep(10)
                            break
            # pyautogui.hotkey("win","d")



            # # 关闭所有模拟器，提示是否关机。需要最for循环外的 关闭最后两个模拟器 继续分析，关闭流程，应该在什么位置，是num<2 以内，还是for 遍历模拟器之外？
            # if moniqi_info[1] == moniqi_infos[len(moniqi_infos)-1][1]:
            #     time.sleep(300)
            #     while True:
            #         close_num = 0
            #         f_read = open(filepath + filename,"r")
            #         lines = f_read.readlines()
            #         f_read.close()
            #         for lineinfo in lines:
            #             # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            #             if  "closing" in lineinfo:
            #                 for moniqi_name_kill in moniqi_infos:
            #                     if moniqi_name_kill[1] in lineinfo:
            #                         pro_id = close_window_name(moniqi_name_kill[0])
            #                         killpid(pro_id)
            #             elif  "close" in lineinfo:
            #                 close_num = close_num + 1
            #         if  close_num == len(lines):
            #             print("所有模拟器已关闭，是否关机？ 待补充弹窗确认")
            #             exit(0)

        else:
            time.sleep(150)
            goto .judgeapp

    # 对最后两个模拟器kill操作
    time.sleep(60)
    while True:
        f_read = open(filepath + filename,"r",encoding='UTF-8')
        lines = f_read.readlines()
        f_read.close()
        close_num = 0
        for lineinfo in lines:
            print("lineinfo is : ",lineinfo)
            # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            if  "closing" in lineinfo:
                for moniqi_name_kill in moniqi_infos:
                    if moniqi_name_kill[1] in lineinfo:
                        replace_taskinfo(filepath,filename,moniqi_name_kill[1])
                        pro_id = close_window_name(moniqi_name_kill[0])
                        killpid(pro_id)
                        time.sleep(2)
                        close_num = close_num + 1
            elif "close" in lineinfo:
                close_num = close_num + 1
        print("close_num is : ",close_num)
        if close_num == len(lines):
            print("所有模拟器已关闭，是否关机？ 待补充弹窗确认")
            send_ding_msg("已完成所有模拟器操作，是否关机？")
            # exit(0)
            os._exit(0)
        else:
            time.sleep(30)


@with_goto     #必须有
def judge_moniqi_status_bak():
    windows_num = 0
    # current_window_name = []
    for moniqi_info in moniqi_infos:
        label .judgeapp
        f_read = open(filepath + filename,"r",encoding='UTF-8')
        lines = f_read.readlines()
        f_read.close()
        for lineinfo in lines:
            # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            if  "closing" in lineinfo:
                for moniqi_name_kill in moniqi_infos:
                    if moniqi_name_kill[1] in lineinfo:
                        replace_taskinfo(filepath,filename,moniqi_name_kill[1])
                        pro_id = close_window_name(moniqi_name_kill[0])
                        killpid(pro_id)
                        windows_num = windows_num - 1
        
        if windows_num < 2:
            # 打开模拟器
            open_application()
            windows_num = windows_num + 1
            pyautogui.moveTo(1,1,duration=0.3)
            time.sleep(10)

            # 启动模拟器
            # windows_num = windows_num + 1
            moniqiname = "\\" + moniqi_info[0] + ".png"
            print("模拟器名字is ",moniqiname)
            qidong(moniqiname)
            time.sleep(60)

            # 打开按键精灵
            point_infos = find_pic(picpath + r"\ajjl.png")
            print("按键精灵app坐标: ",point_infos)
            find_click(point_infos)
            time.sleep(40)

            # 忽略更新 todo 待补充截图
            pth = picpath + r"\ajjl-hulue.png"
            point_infos = find_pic_num_confidence(pth,20,0.8)
            # point_infos = find_pic(picpath + r"\ajjl-hulue.png")
            print("忽略更新坐标: ",point_infos)
            find_click(point_infos)
            time.sleep(20)

            # 取消获取系统权限
            pth = picpath + r"\ajjl-quxiao.png"
            point_infos = find_pic_num_confidence(pth,20,0.8)
            find_click(point_infos)
            time.sleep(20) 

            # # 取消获取系统权限
            # point_infos = find_pic(picpath + r"\ajjl-quxiao.png")
            # print("按键精灵app坐标: ",point_infos)
            # find_click(point_infos)
            # time.sleep(5)   
            #     
            # 编写
            point_infos = find_pic(picpath + r"\ajjl-bianxie.png")
            print("找到编写坐标：",point_infos)
            find_click(point_infos)
            time.sleep(10)      
            # 选择未分类目录
            point_infos = find_pic(picpath + r"\ajjl-weifenlei.png")
            find_click(point_infos)
            time.sleep(8) 
            # 选择脚本
            point_infos = find_pic(picpath + r"\ajjl-jiaoben.png")
            find_click(point_infos)
            time.sleep(10) 
            # 加载脚本
            point_infos = find_pic(picpath + r"\ajjl-jiazai.png")
            find_click(point_infos)
            time.sleep(10) 
            # 启动脚本
            point_infos = find_pic(picpath + r"\ajjl-qidong.png")
            find_click(point_infos)
            time.sleep(5) 
            pyautogui.hotkey("win","d")

            # # 关闭所有模拟器，提示是否关机。需要最for循环外的 关闭最后两个模拟器 继续分析，关闭流程，应该在什么位置，是num<2 以内，还是for 遍历模拟器之外？
            # if moniqi_info[1] == moniqi_infos[len(moniqi_infos)-1][1]:
            #     time.sleep(300)
            #     while True:
            #         close_num = 0
            #         f_read = open(filepath + filename,"r")
            #         lines = f_read.readlines()
            #         f_read.close()
            #         for lineinfo in lines:
            #             # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            #             if  "closing" in lineinfo:
            #                 for moniqi_name_kill in moniqi_infos:
            #                     if moniqi_name_kill[1] in lineinfo:
            #                         pro_id = close_window_name(moniqi_name_kill[0])
            #                         killpid(pro_id)
            #             elif  "close" in lineinfo:
            #                 close_num = close_num + 1
            #         if  close_num == len(lines):
            #             print("所有模拟器已关闭，是否关机？ 待补充弹窗确认")
            #             exit(0)

        else:
            time.sleep(150)
            goto .judgeapp

    # 对最后两个模拟器kill操作
    time.sleep(60)
    while True:
        f_read = open(filepath + filename,"r",encoding='UTF-8')
        lines = f_read.readlines()
        f_read.close()
        close_num = 0
        for lineinfo in lines:
            print("lineinfo is : ",lineinfo)
            # if moniqi_info[1] in lineinfo and "closing" in lineinfo:
            if  "closing" in lineinfo:
                for moniqi_name_kill in moniqi_infos:
                    if moniqi_name_kill[1] in lineinfo:
                        replace_taskinfo(filepath,filename,moniqi_name_kill[1])
                        pro_id = close_window_name(moniqi_name_kill[0])
                        killpid(pro_id)
                        time.sleep(2)
                        close_num = close_num + 1
            elif "close" in lineinfo:
                close_num = close_num + 1
        print("close_num is : ",close_num)
        if close_num == len(lines):
            print("所有模拟器已关闭，是否关机？ 待补充弹窗确认")
            send_ding_msg("已完成所有模拟器操作，是否关机？")
            # exit(0)
            os._exit(0)
        else:
            time.sleep(30)

def mywarn():
    time.sleep(10)
    while True:
        for minfo in moniqi_infos:
            warnfile = "warninfo-" + minfo[1] + ".txt"
            f_read = open(filepath + warnfile,"r",encoding='UTF-8')
            lines = f_read .readlines()
            f_read.close()
            for lineinfo in lines:
                if  "send warn" in lineinfo:
                    # localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # msg_info = f"{localtime} : {lineinfo}\n".format(localtime,lineinfo) + msg_info
                    print("lineinfo is : ",lineinfo)
                    msg_info = f"模拟器 {lineinfo}\n".format(minfo,lineinfo)
                    send_ding_msg(msg_info)
                    f = open(filepath + warnfile,"w",encoding='UTF-8')
                    f.write(" ")
                    f.flush()
                    f.close()
        time.sleep(10)

def send_ding_msg(msg):
    # 请求的URL，WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=8d3a0cac0bb37ec689e2333ae099561f7f8d3f6ffd42843d2b54475ff96ed254  '
    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    message = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "isAtAll": False
        }
    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)

    # 发送请求
    info = requests.post(url=webhook, data=message_json.encode("utf-8"), headers=header)
    # 打印返回的结果

def locateOnScreen_dzq(image, src_image, minSearchTime=0, **kwargs):
    """TODO - rewrite this
    minSearchTime - amount of time in seconds to repeat taking
    screenshots and trying to locate a match.  The default of 0 performs
    a single search.
    """
    start = time.time()
    while True:
        try:
            # screenshotIm = pyautogui.screenshot(region=None) # the locateAll() function must handle cropping to return accurate coordinates, so don't pass a region here.
            # retVal = pyautogui.locate(image, screenshotIm, **kwargs)

            screenshotIm = Image.open(src_image)
            # 图片如果是1080 1920 则逆时针旋转90度
            # if screenshotIm.width == 1080 and screenshotIm.height == 1920:
            #     screenshotIm = screenshotIm.rotate(90, expand = True)
            #     screenshotIm.show()
            retVal = pyautogui.locate(image, screenshotIm, **kwargs)

            try:
                screenshotIm.fp.close()
            except AttributeError:
                # Screenshots on Windows won't have an fp since they came from
                # ImageGrab, not a file. Screenshots on Linux will have fp set
                # to None since the file has been unlinked
                pass
            if retVal or time.time() - start > minSearchTime:
                return retVal
        except pyautogui.ImageNotFoundException:
            if time.time() - start > minSearchTime:
                if pyautogui.USE_IMAGE_NOT_FOUND_EXCEPTION:
                    raise
                else:
                    return None

if __name__=="__main__":
    time.sleep(5)
    leidian_path = r"F:\soft\leidian\LDPlayer4\\"
    picpath = r'H:\pycode\python\sgz\picture'
    filepath = r"C:\Users\Administrator\Documents\leidian\Pictures\\"
    filename = "taskinfo.txt"
    screencap_path = r"C:\Users\Administrator\Documents\leidian\Pictures\\"
    # screencap_path = r"G:\autogame_picture\\"

    # moniqi_infos = [("1-1","010067022632332"),("3-3","010138026629481"),("liu001","010305026177593"),("4-4","010139023165222"),("5-5","010305027142000"),("myjy002","353512023556225")]
    # moniqi_infos = [("liu001","010305026177593"),("4-4","010139023165222"),("5-5","010305027142000"),("myjy002","353512023556225"),("1-1","010067022632332"),("3-3","010138026629481")]
    # moniqi_infos = [("liu001","010305026177593"),("4-4","010139023165222"),("5-5","010305027142000"),("1-1","010067022632332"),("3-3","010138026629481")]
    moniqi_infos = [("7-7","358522025888836"),("6-6","010138028661276")]

    # 初始化close , ajjl start, ajjl closing, python close
    # 初始化模拟器状态文件
    task_f= open(filepath + filename,"w")
    for moniqi in moniqi_infos:
        task_f.write(moniqi[1] + " close\n")
        task_f.flush()
    task_f.close()

    # 初始化各模拟器告警文件
    for moniqi in moniqi_infos:
        warninfo = "warninfo-" + moniqi[1] + ".txt"
        warnf1= open(filepath + warninfo, "w")
        warnf1.write(" ")
        warnf1.flush()
    warnf1.close()

    print("模拟器状态信息初始化文件完成")

    try:
        warn_list = [judge_moniqi_status,mywarn]
        # warn_list = [task_notmove]
        t = []
        for warn in warn_list:
            # t.append(threading.Thread(target=warn,args=[host_db, user, password, database]))
            t.append(threading.Thread(target=warn))
        try:
            for tx in t:
                tx.start()
        except:
            print("Error: 无法启动线程")
        for tx in t:
            tx.join()

    except Exception as e:
        # logging.error(f'=======出现错误-，{e}')
        send_ding_msg("====== python程序运行异常, error is : {}".format(e))   
        print("====== robot programe failed, error is : {}".format(e))






