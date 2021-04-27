# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--18:03
import datetime
def dayofyear():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    print((date1 - date2).days+1)
    return (date1-date2).days+1

if __name__ == '__main__':
    dayofyear()