# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--16:05
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])

'''
结果为[6, 6, 6, 6]
产生此结果的原因是python的闭包延迟绑定，这意味着内部函数被调用时，参数的值在闭包内进行查找。
因此，当任何由multipliers()返回的函数被调用时，i的值将在附近的范围进行查找。那时，不管返回的
汉是否被调用，for循环已经完成，i被赋予了最终的值3。
'''
#解决办法一
# def multipliers():
#     for i in range(4):
#         yield lambda x:i*x
# print([m(2) for m in multipliers()])

#解决办法二
def multipliers():
    return [lambda x,i = i: i*x for i in range(4)]
print([m(2) for m in multipliers()])

