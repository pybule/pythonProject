# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--22:57
#第一种方法
# def loop_merge_sort(l1,l2):
#     tmp = []
#     while len(l1)>0 and len(l2)>0:
#         if l1[0] <l2[0]:
#             tmp.append(l1[0])
#             del l1[0]
#         else:
#             tmp.append(l2[0])
#             del l2[0]
#     while len(l1)>0:
#         tmp.append(l1[0])
#         del l1[0]
#     while len(l2)>0:
#         tmp.append(l2[0])
#         del l2[0]
#     return tmp
# if __name__ == '__main__':
#     l1 = [1,2,3,4,5]
#     l2 = [3,4,5,6,7,8,9]
#     print(loop_merge_sort(l1,l2))

#第二种方法
# l1 = [1,2,3,4,5]
# l2 = [3,4,5,6,7,8,9]
#
# l1.extend(l2)
# print(l1)    #只能输出l1，不能再重新命名

#第三种方法
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7,8,9]
l3 = l1+l2
print(l3)