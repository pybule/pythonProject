# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--19:24
#第一种方法：
# def singleton(cls):
#     instances = {}
#     def weapper(*args,**kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args,**kwargs)
#         return instances[cls]
#     return weapper()
#
# @singleton
# class Foo(object):
#     pass
#
# foo1 = Foo()
# foo2 = Foo()
# print(foo1 is foo2)

#第二中方法：使用基类
#New是真正创建实例对象的方法，所以重写基类的new方法，以此保证创建对象的时候只生成一个shil
# class Singleton():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
#         return cls._instance
#
# class Foo(Singleton):
#     pass
#
# foo1 = Foo()
# foo2 = Foo()
#
# print(foo1 is foo2)

class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)
