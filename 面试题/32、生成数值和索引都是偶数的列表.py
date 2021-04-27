# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--22:46
def num_list(num):
    return [i for i in num if i%2==0 and num.index(i)%2==0]

num = [0,1,2,3,4,5,6,7,8,9,10]
list = num_list(num)
print(list)
