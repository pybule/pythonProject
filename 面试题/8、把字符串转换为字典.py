# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--18:32
str1 = "k:1|k1:2|k2:3|k3:4"
# def str2dict(str1):
#     dict1 = {}
#     for i in str1.split('|'):
#         key,value = i.split(':')
#         dict1[key] = int(value)
#     print(dict1)
# if __name__ == '__main__':
#     str2dict(str1)

#字典推导式
d = {k:int(v) for t in str1.split('|') for k,v in (t.split(':'),)}
print(d)