# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--13:25

#hasattr（object，name）函数：
'''
判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True
否则返回False
'''
class function_demo(object):
    name = 'demo'
    def run(self):
        return "hello function"
functiondemo = function_demo()
res1 = hasattr(functiondemo,"name")    #判断对象是否有name属性，True
res2 = hasattr(functiondemo,"run")     #判断对象是否有run方法，True
res3 = hasattr(functiondemo,"age")     #判断对象是否有age属性，False
print(res1)
print(res2)
print(res3)