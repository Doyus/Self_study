# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 13:03:34
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 13:16:49
def create_num(all_num):
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "ok.........."

obj = create_num(50)


while True:
    try:
        ret = next(obj)
        print(ret)

    except Exception as ret:
        print(ret.value)
        break