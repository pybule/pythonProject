# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--22:14


#方法一
# def test(filepath):
#     distone = {}
#     with open(filepath,'r',encoding='utf-8') as f:
#         for line in f:
#             # line = re.sub("\w+"," ",line)
#             lineone = line.split()
#             for keyone in lineone:
#                 if not distone.get(keyone):
#                     distone[keyone] = 1
#                 else:
#                     distone[keyone] +=1
#     num_ten = sorted(distone.items(),key=lambda x:x[1],reverse=True)[:10]
#     num_ten = [x[0] for x in num_ten]
#     print(num_ten)
# if __name__ == '__main__':
#     test('31test.txt')

#第二种方法
from collections import Counter

def test2(filepath):
    with open(filepath,encoding='utf-8') as f:
        # print(list(Counter(f.read().split()).most_common(10)))
        # [('dd', 4), ('gg', 4), ('fd', 2), ('erte', 2), ('hh', 2), ('水电费', 2), ('sd', 1), ('dsfsd', 1),
        # ('fds', 1),('ffg', 1)]

        #map函数取出key
        print(list(map(lambda c: c[0], Counter(f.read().split()).most_common(10))))
test2('31test.txt')
