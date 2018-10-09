# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-10-01 13:18:42
# @Last Modified by:   Marte
# @Last Modified time: 2018-10-01 13:38:28
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>ret>>>", ret)
        a, b = b, a+b

        current_num += 1

obj = create_num(10)

# obj.send(None) send 一般不会放在第一次启动生成器，如果非要这么做，传值None即可

ret = next(obj)
print(ret)

# send 里面的数据会 传递给第五行,当作yield a 的结果,然后ret保存这个结果,,,
# send的结果是下一次调用yield时,yield后面的值
ret = obj.send("hahahhaha")

print(ret)