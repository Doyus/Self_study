# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-06 19:47:28
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-06 19:57:36
# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# image = Image.open('a.png')
# text = pytesseract.image_to_string(image)
# text = pytesseract.image_to_string(image,lang='chi_sim')
# print(text)

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

image = Image.open('b.png')
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)
