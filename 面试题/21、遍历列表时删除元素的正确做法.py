# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--20:54
#第一种方法
# a = [1,2,3,4,5,6,7,8,9]
# print(id(a))
# print(id(a[:]))
# for i in a[:]:
#     if i>5:
#         pass
#     else:
#         a.remove(i)
#     print(a)
#
# print("*"*20)
# print(id(a))

#第二种方法 filter
# a = [1,2,3,4,5,6,7,8,9]
# b = filter(lambda x:x>5 ,a)
# print(list(b))

#第三种方法 列表解析
a = [1,2,3,4,5,6,7,8,9]
b = [i for i in a if i>5]
print(b)
