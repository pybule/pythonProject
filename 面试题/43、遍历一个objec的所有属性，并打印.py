# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/22--1:00
class Car:
    def __init__(self,name,loss):  #loss [价格，油耗，公里数]
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        #获取汽车价格
        return self.loss[0]

    def getLoss(self):
        #获取汽车损耗值
        return self.loss[1] * self.loss[2]

BMW = Car("宝马",[60,9,500])   #实例化一个宝马车对象
print(getattr(BMW,"name"))    #使用getattr()传入对象名字，属性值
print(dir(BMW))   #获取BMW所有的属性和方法