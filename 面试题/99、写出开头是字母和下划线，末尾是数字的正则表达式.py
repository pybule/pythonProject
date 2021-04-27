# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--23:08
import re
str = '_sfsdf sdf00fds99f098'
res = re.findall('^[A-Za-z_].*?\d$',str)
print(res)