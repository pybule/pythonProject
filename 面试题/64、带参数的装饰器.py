# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--11:29

#带定长参数的装饰器
# def new_func(func):
#     def warppedfun(username,passwd):
#         if username == 'root' and passwd == '123456789':
#             print("通过认证")
#             print("开始执行附加功能")
#             return func()
#         else:
#             print("用户名或密码错误")
#             return
#     return warppedfun
#
# @new_func
# def origin():
#     print("开始执行函数")
# origin('root','123456789')

#带不定长参数的装饰器
def new_func(func):
    def wrappedfun(*parts):
        if parts:
            counts = len(parts)
            print("本系统包含 ",end="")
            for part in parts:
                print(part,' ',end='')
            print('等',counts,'部分')
            return func()
        else:
            print('用户名或密码错误')
            return func()
    return wrappedfun
@new_func
def origin():
    print("开始执行函数")
origin('root','123456789')