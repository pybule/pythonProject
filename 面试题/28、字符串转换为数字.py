# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--21:21
a = '1497323'
def atoi(a):
    num = 0
    for i in a:
        for j in range(10):
            if i==str(j):
                num = num*10 +j
    print(num)
if __name__ == '__main__':
    atoi(a)