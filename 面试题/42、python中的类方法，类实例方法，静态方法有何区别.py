# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/22--0:45
'''
类方法：是类对象的方法，在定义时需要在上方使用@classmethod进行修饰，形参为cls，表示类对象，
类对象和类实例对象都可调用

类实例方法：是类实例化对象的方法，只有实例对象可以调用，形参为self，指代对象本身

静态方法：是一个任意函数，在其上方使用@staticmethod进行装饰，可以用对象直接调用，静态方法实际上跟类没有太大关系
'''