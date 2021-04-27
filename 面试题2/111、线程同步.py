# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/24--10:57
'''
一、setDaemon(False)
当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行的最小单位，当设置多线程时，
主线程会创建多个子线程，在python中，默认情况下就是setDaemon(False),主线程执行完自己的任务以后，
就退出了，此时子线程会继续执行自己的任务，直达自己的任务结束。
'''
# import threading
# import time
#
# def thread():
#     time.sleep(2)
#     print('-----子线程结束-------')
#
# def main():
#     t1 = threading.Thread(target=thread)
#     t1.start()
#     print('-----主线程---结束---')
#
# if __name__ == '__main__':
#     main()

'''
二、setDaem（True）
当我们使用setDaem(True)时，这是子进程为守护线程，主线程一旦执行结束，则全部子线程被强制终止
'''
# import threading
# import time
#
# def thread():
#     time.sleep(2)
#     print('-----子线程结束-------')
# def main():
#     t1 = threading.Thread(target=thread)
#     t1.setDaemon(True)   #设置子线程守护主线程，主线程结束，子线程就被强制结束，无论子线程是否执行
#     t1.start()
#     print('------主线程结束-------')
#
# if __name__ == '__main__':
#     main()

'''
三、join（线程同步）
join所完成的工作就是线程同步，即主线程任务结束以后，进入堵塞状态，一直等待所有的子线程结束以后，
主线程再终止

当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死改子线程，最后退出程序，
所以说，如果有10个子线程，全部的等待时间就是每个timeou的累加和，简单的来说，就是给每个子线程
一个timeou的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死

没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，主线程结束，但
是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，程序退出
'''
import threading
import time

def thread():
    time.sleep(2)
    print('------子线程结束-------')

def main():
    t1 = threading.Thread(target=thread)
    t1.setDaemon(True)
    t1.start()
    t1.join(timeout=5)    #1、线程同步，主线程堵塞1s，然后主线程结束，子线程继续执行
                          #2、如果不设置timeout参数就等于子线程结束主线程再结束
                          #3、如果设置了setDaemon=True和timeout=1主线程等待1s后悔强制杀死子进程，然后主线程结束
    print('------主线程结束---------')

if __name__ == '__main__':
    main()