#-*- coding: UTF-8 -*-
from tkinter import Message
from PIL import Image
# import tesseract
import pytesseract
import pyautogui
import time

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

    # text = "(1234,567),"
    text = "1234,567"    
    start = 0
    end = len(text)-1
    for i in range(len(text)):
        if text[i] == "(":
            start = i+1
        elif text[i] == ")":
            end = len(text)-i
    if ")" not in text:
        end = len(text)
        xy = text[start:]
    else:                
        xy = text[start:][:-end]
    print(xy)

