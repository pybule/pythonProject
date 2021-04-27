# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/22--0:21
def multi():
    return [lambda x:i*x for i in range(4)]
print([m(3) for m in multi()])