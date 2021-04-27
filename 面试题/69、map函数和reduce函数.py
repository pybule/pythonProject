# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--12:01
# map函数  遍历列表的每一个

from functools import reduce

l1 = map(lambda x: x * x, [1, 2, 3, 4, 5])
print(list(l1))

l2 = map(lambda x, y: x * y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
print(list(l2))

l3 = map(lambda x, y: (x * y, x + y), [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
print(list(l3))

# 通过map还可以实现类型转换
# 将元组转换为list
l4 = map(int, (1, 2, 3))
print(list(l4))
# 可以直接把元组转换为列表
a = (1, 2, 3)
print(list(a))

# 将字符串转换为list：
l5 = map(int, '1234')
print(list(l5))

# 提出字典中的key，并将结果放在一个list中：
l6 = map(int, {1: 2, 2: 3, 3: 4, 4: 5, 5: 6})
print(list(l6))

# reduce 函数
'''
reduce(function,sequence,initial=None)
reduce有三个函数，第一个是函数function,第二个是序列sequence，第三个是initial，为初始值，默认为None
'''


# 传入自定义的函数
def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6]))

# 求积
x = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(x)

# 求和
y = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(y)
