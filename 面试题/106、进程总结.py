# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--23:18
'''
进程：程序运行在操作系统上的一个实例，就称之为进程。进程需要相应的系统资源：内存、时间片、pid
创建进程：
首先要导入multiprocessing中的Process
创建一个Process对象
创建Process对象时，可以传递参数

p = Process（target=xxx，args=（tuple），kwargs={key：value}
target = xxx  指定的任务函数，不加（）
args=（tuple，）kwargs={key:value}给任务函数传递的参数

使用start()启动进程
结束进程
给子进程指定函数传递参数Demo
'''
#
import os
from multiprocessing import Process
import time
from multiprocessing.queues import Queue


def pro_func(name, age, **kwargs):
    for i in range(5):
        print("子进程正在运行中，name=%s，age=%d,pid=%d" % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建Process
    p = Process(target=pro_func, args=('小明', 18), kwargs={'m': 20})
    # 启动进程
    p.start()
    time.sleep(1)
    # 1秒钟之后，立即结束子进程
    p.terminate()
    p.join()
