# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 20:00:36
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 20:02:03
import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
    url = ''

    while True:
        request.urlretrieve(url, 'cap.png')
        image = Image.open('cap.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)

if __name__ == "__main__":
    main