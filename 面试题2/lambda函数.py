# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/26--20:58
#lambda函数的用法

#1、将lambda函数赋值给变量
a = lambda x:x+3
print(a(5))

#2、将lambda作为其他函数的返回值
def test(n):
    return lambda x:x+n
t =test(3)      #n赋值为3
print(t(2))     #x为2

#3、将lambda函数作为其他函数的参数


#列表
l = [1,2,3,4,5]
l2 = [11,22,33,44,55,66,77,88]
print(l[1::2])
l[0]=8
# l.extend("k")      #追加字符串k
l.extend([4,88])   #追加新列表
l.extend([99])     #追加新列表
l.append(88)       #追加新元素
l.insert(0,199)    #把索引为0的位置插入为199
print(l+l2)

print(l[1])     #取索引为1的元素
print(l[1:])    #取第一个元素之后的元素
print(l[::-1])  #列表倒序显示
print(l[2::2])  #从索引为2的元素开始取，间隔为2
print(l)

d = {"a":1,"b":2,"c":3,"d":4}
dl = []
dl2 = []
for k,v in d.items():
    # dl.append(k)   #只能添加一个，要么把k，添加到列表，要么把v添加到列表
    dl2.append(v)
print(dl)
print(dl2)

for k in d.keys():
    print(k,end=',')
print()
for v in d.values():
    print(v,end=',')
print()

# ll = [3,44,3,5,6,77]
def high(ll):
    if ll > 20:
        return 1
    else:
        return 0
print(high(100))



