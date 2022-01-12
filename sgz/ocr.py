#-*- coding: UTF-8 -*-
from tkinter import Message
from PIL import Image
# import tesseract
import pytesseract
import pyautogui
import time
from aip import AipOcr

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

def success(msg):
    print("method success!!!!,msg is : ",msg)
def debug(msg):
    print("method debug!!!!,msg is : ",msg)
def other(msg):
    print("method other!!!!,msg is : ",msg)
    
def notify_result(num,msg):
    numbers = {
        0 : success,
        1 : debug
    }
    method = numbers.get(num,other)
    if method:
        method(msg)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == "__main__":
    # reader = easyocr.Reader(['ch_sim','en'])
    # result = reader.readtext("D:\project\FR\script\pic1.png")
    # print(result)

    # text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\pic2.png'),lang='chi_sim')
    # print(text)
    # print("end")
    # time.sleep(3)
    # for i in range(4):
    #     pyautogui.press("backspace")
    #     time.sleep(0.1)
    # pyautogui.typewrite(message=str(456))

    # text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\sgz\level5_tie.png'))
    # print(text)
    # text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\sgz\level5_tie.png'),lang='chi_sim')
    # print(text)

    # pointinfo = pyautogui.locateOnScreen(r"D:\code\mypython\python\sgz\level5_tie.png")

    # filepath = r'D:\code\mypython\python\sgz\status-idle.png'
    # image = get_file_content(filepath)
    # APP_ID = "22db84bb626d40eaa316c4c58864f26b"
    # API_KEY = 'dc4662b5852d420a9d44a1b4e236f528'
    # SECRET_KEY = '4b14e073956b42fab33d7e6b435272fe'
    # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # result = client.basicGeneral(image)
    # print(result)
    # print(result["words_result"][0]["words"])
    # print(result["words_result"][1]["words"])

    # result = {'words_result': [{'words': '状态'}, {'words': '闲置'}], 'words_result_num': 2, 'log_id': 1479068192281292552}    
    # print(result["words_result"][0]["words"])
    # print(result["words_result"][1]["words"])
    # print(type(result["words_result"][1]["words"]))

    # notify_result(0,"test 0")
    # notify_result(3,"test 3")

    
    # you = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\you.png",10,0.8)
    # if you != None:
    #     who_lock = 3
    #     print("you is: ",you)
    # # 颜色有偏差，放弃颜色区分，改为文字判断，自己的可以筑城，扫荡，盟友的可以驻守，（自己的建筑也只能行军驻守，如何区分？）
    # # 有主公，且有"攻占/攻城"，则为敌对 who_lock = 4；
    # # 无主公 无城池，有攻占/攻城，则为空地或不可占领
    # # 有"城池" 则为城池 
    # else:
    #     lvse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\lvse_zhugong2.png",10,0.87)
    #     if lvse_zhugong != None:
    #         who_lock = 1
    #         print("lvse_zhugong is: ",lvse_zhugong)
    #     else:
    #         lanse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\lanse_zhugong.png",10,0.87)
    #         if lanse_zhugong != None:
    #             who_lock = 2
    #             print("lanse_zhugong is: ",lanse_zhugong)
    #         # else:
    #         #     qianlan_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\qianlan_zhugong.png",10,0.92)
    #         #     if qianlan_zhugong != None:
    #         #         who_lock = 3
    #         #         print("qianlan_zhugong is: ",qianlan_zhugong)
    #         else:
    #             hongse_zhugong = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\hongse_zhugong.png",10,0.87)                
    #             hongse_zhugong2 = find_pic_num_confidence(r"D:\code\mypython\python\sgz\picture\hongse_zhugong2.png",10,0.87)
    #             if hongse_zhugong != None or hongse_zhugong2 != None :
    #                 who_lock = 4
    #                 print("hongse_zhugong is: ",hongse_zhugong,hongse_zhugong2)
    #             else:
    #                 who_lock = 0
    
    # region 参数 左上角，lef  top， 右下角 left top
    # pointinfo = pyautogui.locateOnScreen(r"D:\code\mypython\python\sgz\picture\gongzhan.png",region=(1,1,1366,768))
    pointinfo = pyautogui.locateOnScreen(r"D:\code\mypython\python\sgz\picture\lvse_zhugong.png",region=(1070,160,1200,190),confidence=0.7)

    print(pointinfo)