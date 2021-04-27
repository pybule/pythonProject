# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--21:01

def get_missing_letter(a):
    s1 = set("abcdefghigklmnopqrstuvwxyz")
    s2 = set(a.lower())
    ret = "".join(sorted(s1-s2))     #"".join()转换为字符串
    return ret
print(get_missing_letter("python"))