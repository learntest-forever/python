from msilib.schema import Class
import time
from turtle import distance
from cv2 import destroyAllWindows
from matplotlib.pyplot import connect
from numpy import datetime_data, true_divide, who
import pyautogui
import os
import win32api
# import psreadline
import datetime
import random
import msvcrt
# import cv2
from PIL import Image
# import tesseract
import pytesseract
import string
from aip import AipOcr


class Sgz(object):
    def getinput(self,timeout=10):
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
    def find_pic(self,picture_path):
        i = 1
        while True:
            point_info = pyautogui.locateOnScreen(picture_path,confidence=0.8)
            if point_info != None:
                print(point_info)
                return point_info
            elif point_info == None and i >= 10:
                # 发送告警消息，钉钉
                print("未找到指定图片,请输入您的选择：1：跳过此步；2：继续查找")
                choice_op = self.getinput(10)
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
    def find_pic_old(self,picture_path):
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
    def find_pic_10(self,picture_path):
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

    def find_pic_num_confidence(self,picture_path,num,confidence):
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

    def find_pic_num_confidence_zone(self,picture_path,zone,num,confidence):
        i = 1
        # pyautogui.moveTo(zone[0],zone[1])
        # time.sleep(5)
        # pyautogui.moveTo(zone[0]+zone[2],zone[1]+zone[3])
        # time.sleep(5)
        for i in range(num):
            point_info = pyautogui.locateOnScreen(picture_path,region=zone,confidence=confidence)
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

    def find_pic_all(self,picture_path):
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

    def find_pic_list(self,picture_path,confidence):
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

    def gen_destnode(self,left,top,width,height):
        return(left + random.random()*width, top + random.random()*height)

    def start_mnq(self,x,y):
        pyautogui.leftClick(x=x,y=y,duration=0.5)

    def find_click(self,point_infos):
        if point_infos == None:
            print("未找到对应图片，请确认")
        else:
            dest_node = self.gen_destnode(point_infos.left,point_infos.top,point_infos.width,point_infos.height)
            self.start_mnq(dest_node[0],dest_node[1])
            pyautogui.moveTo(1,1,duration=0.3)


    def get_zhucheng(self):
        point_infos = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao_zuobiao.png",20,0.8)
        print("dibiao_zuobiao: ",point_infos)
        if point_infos != None:
            self.find_click(point_infos)
            # 地标与主城坐标距离 通过查下获取差值，将插值作为“地标的”偏移量获取主城坐标位置
            dest_node = self.gen_destnode(point_infos.left-122, point_infos.top + 50, 77, 25)
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

    # def judge_land_level(self,x,y):
    def judge_land_level(self):
        # self.toxy(x,y)
        dibiao = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao1.png",10,0.8)
        if dibiao != None:
            zone = (dibiao.left - 550, dibiao.top, 90,50)
            print("zone is : ",zone)
            pyautogui.moveTo(zone[0],zone[1])
            time.sleep(3)
            pyautogui.moveTo(zone[0]+90,zone[1] + 50)
            time.sleep(3)
        else:
            print("未找到定位地标")
            return None        
        if self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level0_kongdi.png",zone,20,0.85) !=None:
            print("land level is 0 空地 ")
            level = 0
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level1_2.png",zone,20,0.85) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level1.png",zone,20,0.85) !=None:
            print("pointinfo is level1")
            level = 1         
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level2.png",zone,20,0.85) != None:
            print("pointinfo is level2")
            level = 2
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level3_2.png",zone,20,0.85) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level3.png",zone,20,0.85) != None:
            print("pointinfo is level3")
            level = 3
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level4.png",zone,20,0.85) != None:
            print("pointinfo is level4")
            level = 4
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level5_2.png",zone,20,0.9) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level5.png",zone,20,0.9) != None:
            print("pointinfo is level5")
            level = 5
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level6_2.png",zone,20,0.9) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level6.png",zone,20,0.9) != None:
            print("pointinfo is level6")
            level = 6
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level7.png",zone,20,0.9) != None:
            print("pointinfo is level7")
            level = 7
        elif self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\level8.png",zone,20,0.9) != None:
            print("pointinfo is level8")
            level = 8
        else:
            print("未找到对应等级 level 大于8级或是建筑物或不可占领")
            level = 99
        return level

    def judge_land_lock(self):
        # who_lock: 0 空，1 自己，2 盟友，3友盟，4 敌对，5 未知
            you = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\you.png",20,0.8)
            if you != None:
                who_lock = 3
                print("you is: ",you)
            else:
                dibiao = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao1.png",10,0.8)
                if dibiao != None:
                    zone = (dibiao.left - 400, dibiao.top + 23, 120,100)
                    print("zone is : ",zone)
                    pyautogui.moveTo(zone[0],zone[1])
                    time.sleep(3)
                    pyautogui.moveTo(zone[0]+120,zone[1] + 100)
                    time.sleep(3)
                else:
                    return None
                lvse_zhugong = self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lvse_zhugong.png",zone,10,0.95)
                if lvse_zhugong != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lvse_zhugong2.png",zone,10,0.95) or  self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lvse_zhugong3.png",zone,10,0.95) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lvse_zhugong4.png",zone,10,0.95) != None:
                    who_lock = 1
                    print("lvse_zhugong")
                else:
                    lanse_zhugong = self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lanse_zhugong.png",zone,10,0.95)
                    if lanse_zhugong != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lanse_zhugong2.png",zone,10,0.95) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lanse_zhugong3.png",zone,10,0.95) != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\lanse_zhugong4.png",zone,10,0.95) != None:
                        who_lock = 2
                        print("lanse_zhugong",lanse_zhugong)
                    else:
                        hongse_zhugong3 = self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\hongse_zhugong3.png",zone,10,0.95)
                        if hongse_zhugong3 != None or self.find_pic_num_confidence_zone(r"D:\code\mypython\python\sgz\picture\hongse_zhugong4.png",zone,10,0.95) != None:
                            who_lock = 4
                            print("hongse_zhugong ")
                        else:
                            who_lock = 0
                            print("who_lock is 0 ")
            print(who_lock)
            return who_lock    

    # 输入主城中心坐标，获取主城11格，输入num 为以主城中新块加减num相邻地块
    def genmap_zhucheng(self,x,y,num):
        f = open("mapfile.txt","w",encoding='utf-8') 
        # f.write("id\t x\t y\t level\t who_lock\n")
        # 根据中心块x的奇偶性，获取主城占用11格坐标
        my_home = []
        if x%2 == 0:
            my_home = [(x,y),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x+1,y-2),(x,y-1),(x-1,y-2),(x-1,y-1),(x-1,y),(x-1,y+1)]
        else:
            my_home = [(x,y),(x,y+1),(x+1,y+2),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x-1,y+2)]
        
        # id = 0
        id = 1
        # if x %2 == 0:
        for i in range(-num,num,1):
            for j in range(-num,num,1):
                point = (x+i,y+j)
                if point not in my_home:
                    self.toxy(x+i,y+j)

                    dibiao = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\dibiao1.png",10,0.8)
                    if dibiao != None:
                        zone_level = (dibiao.left - 530, dibiao.top, 80,50)
                        zone_lock = (dibiao.left - 400, dibiao.top + 23, 120,100)
                        print("zone_level is : ",zone_level)
                        print("zone_lock is : ",zone_lock)

                        # pyautogui.moveTo(zone_level[0],zone_level[1])
                        # time.sleep(3)
                        # pyautogui.moveTo(zone_level[0]+80,zone_level[1] + 50)
                        # time.sleep(3)      
                        level = self.judge_land_level()

                        # pyautogui.moveTo(zone_lock[0],zone_lock[1])
                        # time.sleep(3)
                        # pyautogui.moveTo(zone_lock[0]+120,zone_lock[1] + 100)
                        # time.sleep(3)
                        who_lock = self.judge_land_lock()

                        print("landinfo x y level who_lock is ",point,level,who_lock)
                        landinfo = (str(id)+"\t"+str(point[0])+"\t"+str(point[1])+"\t"+str(level)+"\t"+str(who_lock) + "\n")
                        f.write(landinfo)
                        f.flush()
                        id = id + 1
                        print("id,point,level,who_lock:",id,point,level,who_lock)
                    else:
                        print("未找到定位地标")
                        f.close()
                        return None                    
        f.close()



    # 输入坐标跳转到指定点
    def toxy(self,x,y):
        print("toxy x,y: ",x,y)
        ditu = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\ditu.png",50,0.8)
        if ditu != None:
            self.find_click(ditu)
            time.sleep(2)
            # 根据 坐标输入框前的“坐标图标“ 计算坐标偏移量x y
            zuobiao_biaoshi = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\zuobiao_biaoshi.png",50,0.9)
            if zuobiao_biaoshi != None:
                print("zuobiao_biaoshi: ",zuobiao_biaoshi)           
                # 输入X 偏移量待确认55是否准确
                dest_node = self.gen_destnode(zuobiao_biaoshi.left + 55, zuobiao_biaoshi.top, zuobiao_biaoshi.width + 10, zuobiao_biaoshi.height)
                self.start_mnq(dest_node[0], dest_node[1])
                time.sleep(2)
                wancheng = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\wancheng.png",50,0.8)
                if wancheng != None:
                    dest_node = self.gen_destnode(wancheng.left-400, wancheng.top, wancheng.width, wancheng.height)
                    # start_mnq(dest_node[0], dest_node[1])
                    pyautogui.leftClick(dest_node[0], dest_node[1])
                    pyautogui.mouseDown()
                    time.sleep(2)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    quanxuan = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quanxuan.png",50,0.8)
                    if quanxuan != None:
                        print("quanxuan : ",quanxuan)
                        self.find_click(quanxuan)
                        time.sleep(1)      
                    # print("x del")
                    # for i in range(4):
                    #     print("backspace",i)
                    #     pyautogui.press("backspace",interval=2)
                    # time.sleep(1)
                    pyautogui.typewrite(message=str(x))
                    self.find_click(wancheng)
                    time.sleep(2)

                # 输入Y，偏移量待确认
                dest_node = self.gen_destnode(zuobiao_biaoshi.left + 165, zuobiao_biaoshi.top, zuobiao_biaoshi.width + 10, zuobiao_biaoshi.height)
                self.start_mnq(dest_node[0], dest_node[1])
                time.sleep(2)
                wancheng = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\wancheng.png",50,0.8)
                if wancheng != None:
                    dest_node = self.gen_destnode(wancheng.left-400, wancheng.top, wancheng.width, wancheng.height)
                    pyautogui.leftClick(dest_node[0], dest_node[1])
                    pyautogui.mouseDown()
                    time.sleep(2)
                    pyautogui.mouseUp()
                    time.sleep(1)
                    quanxuan = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\quanxuan.png",50,0.8)
                    if quanxuan != None:
                        print("quanxuan : ",quanxuan)
                        self.find_click(quanxuan)
                        time.sleep(1)    
                    pyautogui.typewrite(message=str(y))
                    self.find_click(wancheng)
                    qianwang_xy = self.find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qianwang_xy.png",50,0.9)
                    if qianwang_xy != None:
                        self.find_click(qianwang_xy)
                        time.sleep(3)

    def gen_connect_file(self):
        f = open("mapfile.txt","r")
        fc = open("mapfile_connect.txt","w")
        # connect_header = "id\t x\t y\t level\t who_lock\t connect\n"
        # fc.write(connect_header)
        for line in f.readlines():
            # print(line)
            landinfo = line.split("\t")

            land_x = int(landinfo[1])
            land_y = int(landinfo[2])
            land_connect = []
            if land_x%2 == 0:
                land_connect = [(land_x,land_y+1),(land_x+1,land_y),(land_x+1,land_y-1),(land_x,land_y-1),(land_x-1,land_y-1),(land_x-1,land_y)]
            else:
                land_connect = [(land_x,land_y+1),(land_x+1,land_y+1),(land_x+1,land_y),(land_x,land_y-1),(land_x-1,land_y),(land_x-1,land_y+1)]
            fr = open("mapfile.txt","r")
            connect_node = ""
            for j in fr.readlines():
                landinfo2 = j.strip("\n").split("\t")
                if landinfo[1] == landinfo2[1] and landinfo[2] == landinfo2[2]:
                    continue
                elif (int(landinfo2[1]),int(landinfo2[2])) in land_connect:
                    if len(connect_node) == 0:
                        connect_node = landinfo2[0]
                    else:
                        connect_node = connect_node + "," + landinfo2[0]
            # fc.write(line + "\t" + landinfo2[0] + " ")
            fc.write(line.strip("\n") + "\t" + connect_node)
            fc.flush()
            fr.close()
            fc.write("\n")
            fc.flush()
        f.close()
        fc.close

    # def gen_connectids(self,startx,starty,destx,desty):
    def gen_route(self):
        f = open("mapfile_connect.txt","r")
        for line in f.readlines():
            lineinfo = line.strip("\n").split("\t")
            # if lineinfo[1] == startx and lineinfo[2] == starty:
            connectids = lineinfo[5].split(",")
            print(lineinfo)
            for i in range(len(connectids)):
                print(connectids[i])


    # def gen_route(self,startx,starty,destx,desty):
    def gen_short(self):
        f = open("mapfile_connect.txt","r")
        # startid = 0
        # destid = 0
        num = 0
        for line in f.readlines():
            # lineinfo = line.strip("\n").split("\t")
            # if lineinfo[1] == startx and lineinfo[2] == starty:
            #     startid = lineinfo[0]
            #     num = num + 1
            # elif lineinfo[1] == destx and lineinfo[2] == desty:
            #     destid = lineinfo[0]
            #     num = num + 1
            # else:
            #     print("未找到对应点信息")
            #     return None
            num = num + 1
        # print("num is :",num)
        visited = []
        inf = float('inf')
        distance_id = [[inf for i in range(num)] for j in range(num)]
        fc = open("mapfile_connect.txt","r")

        j = 0
        for line in fc.readlines():
            lineinfo = line.strip("\n").split("\t")
            id = lineinfo[0]
            connectids = lineinfo[5].split(",")
            # print(lineinfo)
            # for i in range(len(connectids)):
            for i in connectids:
                # print(connectids)
                distance_id[j][int(i)]=1
            distance_id[j][j] = 0
            j = j + 1
        print(distance_id)
        f.close()
        fc.close()
        return distance_id


