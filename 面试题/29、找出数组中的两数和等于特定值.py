# _*_ encoding=utf-8 _*_
# author zdh
# date 2021/4/21--21:27

#第一种方法
# class Soluton:
#     def twosum(self,nums,target):
#         """
#
#         :type nums: list[int]
#         :type target: int
#         :retype: list[int]
#         """
#         d = {}
#         size = 0
#         while size < len(nums):
#             if target-nums[size] in d:
#                 if d[target-nums[size]] < size:
#                     return [d[target-nums[size]],size]
#                 else:
#                     d[nums[size]] = size
#                 size = size+1
#
# Soluton =Soluton()
# list = [2,3,4,56,7,8,9,88,65,33]
# target = 9
# nums = Soluton.twosum(list,target)
# print(nums)

#第二种方法
class Solution(object):
    def twosum(self,nums,target):
        for i in range(len(nums)):
            num = target -nums[i]
            if num in nums [i+1:]:
                print([i,nums.index(num,i+1)])
if __name__ == '__main__':
    s=Solution()
    a=s.twosum([2,3,4,5,67,7,8],9)