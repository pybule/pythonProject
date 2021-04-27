# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/23--22:48
import re

a = 'ekjfwefkdfdmskfdsjsansdfdfnsdsfj asdf sadfdsjadffv zxl'
# str.find():正序字符串查找函数
print(a.find("j"))  # 索引为2

# str.index():正序字符串查找函数
print(a.index("j"))  # 索引为2

# str.rfind():倒序字符串查找函数
print(a.rfind("j"))  # 从后往前查41

# str.rindex():倒序字符串查找函数
print(a.rindex("j"))  # 从后往前查41

# 使用re模块进行查找和替换
#查找
print(re.match("kj", a))  # 从开头查起，开头字母不是k，所以结果为None
print(re.match("ekj", a))  # 结果为 <re.Match object; span=(0, 3), match='ekj'>

print(re.search("sdf", a))  # 可以从任意位置匹配，没有匹配上返回None
print(re.findall("sdf", a))  # 可以从任意位置匹配，没有匹配上返回[]
print(re.sub('sdf', 'aabbcc',a))    #把a中所有的sdf替换为aabbcc

#替换
print(a.replace('sa','aabbccdd'))    #把a中的sa全都替换为aabbccdd
