# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--17:49
'''
装饰器本质是一个callable object（可调用函数），它可以让其他函数在不需要做任何代码变动的前提下
增加额外功能，装饰器的返回值也是一个函数对象
'''
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def warpper(*args,**kwargs):
        start = time.clock()
        ret = func(*args,**kwargs)
        end = time.clock()
        print('used:',end-start)
        return ret

    return warpper
@timeit
def foo():
    print('in foo()',foo())
