# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--20:42

#将对象私有化，通过共有方法提供一个读取数据的接口
class person:
    def __init__(self,x):
        self.__age = 10
    def age(self):
        return self.__age

t = person(22)
print(t.age())

#最好的方法
class MYClass():
    __weight = 50

    @property
    def weight(self):
        return self.__weight

# m = MYClass()
# print(m.weight())