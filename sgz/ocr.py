#-*- coding: UTF-8 -*-
from PIL import Image
# import tesseract
import pytesseract


if __name__ == "__main__":
    # reader = easyocr.Reader(['ch_sim','en'])
    # result = reader.readtext("D:\project\FR\script\pic1.png")
    # print(result)

    # text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\pic2.png'),lang='chi_sim')
    # print(text)
    # print("end")
    text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\sgz\level5_tie.png'))
    print(text)
    text = pytesseract.image_to_string(Image.open(r'D:\code\mypython\python\sgz\level5_tie.png'),lang='chi_sim')
    print(text)


