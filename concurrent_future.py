#from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

# 线程池  可以替代semaphore 可以获取状态

# futures可以让线程和多进程接口一致
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

excutor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中  submit是立即返回
task1 = excutor.submit(get_html, (3))
task2 = excutor.submit(get_html, (2))


print(task1.done())  # 判断任务是否完成
time.sleep(3)
print(task2.done())

print(task1.result()) # 获取返回结果



