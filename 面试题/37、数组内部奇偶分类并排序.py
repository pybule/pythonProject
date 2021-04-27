# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--23:13
#方法一
def func(l):
    if isinstance(l,str):
        l = [int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0,l.pop(i))
    print(''.join(str(e) for e in l))

l = [1,2,3,4,5,6,7,8,9]
func(l)

