# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--18:42
alist = [{'name':'a','age':20},{'name':'b','age':30}]
def sort_by_age(list):
    print(sorted(list,key=lambda x:x['age'],reverse=True))

if __name__ == '__main__':
    sort_by_age(alist)