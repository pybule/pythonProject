# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--21:15
#第一种方法
# a = sum([1,2,3,10248])
# print(a)

#第二种方法
from functools import reduce
a = reduce(lambda x,y :x+y,[1,2,3,10248])
print(a)
