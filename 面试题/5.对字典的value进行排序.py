# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--18:20
d = {'a':24,'g':52,'i':12,'k':33}
sorted(d.items(),key=lambda x:x[1])      #x[0]代表用key进行排序，x[1]代表用value进行排序
print(sorted(d.items(),key=lambda x:x[1]))