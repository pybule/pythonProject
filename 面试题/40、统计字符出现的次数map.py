# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/22--0:25

#方法一
# def count_str(str_data):
#     dict_str = {}
#     for i in str_data:
#         dict_str[i] = dict_str.get(i,0) + 1
#     return dict_str
# dict_str = count_str("AAABBCCAC")
# str_count_data = ""
# for k,v in dict_str.items():
#     str_count_data += k +str(v)
# print(str_count_data)

#方法二
from collections import Counter

print("".join(map(lambda x:x[0] +str(x[1]),Counter("AAABBCCAC").most_common())))