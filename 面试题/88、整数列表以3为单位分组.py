# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--18:47

#先生成1-100的数组，再通过索引每3个的取出 [0:3]



print([[x for x in range(1,100)] [i:i+3] for i in range(0,99,3)])


print([x for x in range(1,100)])
# print([[i:i+3] for i in range(1,100,3)])
print([i for i in range(0,100,3)])

l = [1,2,3,4,5,6]
print(l[0:1])