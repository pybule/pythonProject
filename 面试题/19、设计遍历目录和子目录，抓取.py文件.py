# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--20:42
#第一种方法：
# import os
#
# def get_files(dir,suffix):
#     res = []
#     for root,dirs,files in os.walk(dir):
#         for filename in files:
#             name,suf = os.path.splitext(filename)
#             if suf == suffix:
#                 res.append(os.path.join(root,filename))
#     print(res)
#
# get_files("./",".py")

#第二种方法
from glob import iglob

def func(fp,postfix):
    for i in iglob(f"{fp}/**/*{postfix}",recursive=True):
        print(i)
if __name__ == '__main__':
    func("./",".py")