# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/22--1:15
class Array:
    __list = []

    def __init__(self):
        print("constructor")

    def __del__(self):
        print("destruct")

    def __str__(self):
        return "thid=s self-defined array class"

    def __getitem__(self, key):
        return self.__list[key]

    def __len__(self):
        return len(self.__list)

    def Add(self,value):
        self.__list.append(value)

    def Remove(self,index):
        del self.__list[index]

    def DisplayItems(self):
        print("show all items---")
        for item in self.__list:
            print(item)
