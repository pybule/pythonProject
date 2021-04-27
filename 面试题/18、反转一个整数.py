# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--20:29
class Solution(object):
    def reverse(self,x):
        if -10<x<10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x=str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648<x<2147483648 else 0
if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-123)
    print(reverse_int)
