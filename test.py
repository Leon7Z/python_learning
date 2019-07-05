# class Student(object):
#
#     @property
#     def get_score(self):
#         return self._score
#
#     @get_score.setter
#     def get_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# s = Student()
# s.score = 900
# # print(s.score)
# print(s.score)
import time

start = time.clock()
class Solution:
    def twoSum(self, nums, target):
        count = 1

        for i in range(0,len(nums), 1):
            cursor1 = i
            cursor2 = (len(nums) + i)//2
            cursor3 = len(nums)
            todo = True
            while todo:
                if nums[i] + nums[cursor2] == target:
                    count += 1
                    return i, cursor2, count
                elif cursor1 == cursor2 or abs(cursor2 - cursor1) == 1:
                    count += 1
                    break
                elif nums[i] + nums[cursor2] > target:
                    count += 1
                    cursor3 = cursor2
                    cursor2 = (cursor3 + cursor1) // 2
                    continue
                elif nums[i] + nums[cursor2] < target:
                    count += 1
                    cursor1 = cursor2
                    cursor2 = (cursor3 + cursor1) // 2
                    continue


class Solution:
    def twoSum(self, nums, target):
        _dict = {}
        for i, element in enumerate(nums):
            j = _dict.get(target - element)
            if j is not None and j != i:
                return i, j


class Solution:
    def twoSum(self,nums,target):
        _dict = {}
        for i, element in enumerate(nums):
            if _dict.get(target-element) is not None:
                return _dict.get(target-element), i
            _dict[element] = i

# class Solution:
#     def twoSum(self, nums, target):
#         count = 1
#         for i in range(0,len(nums),1):
#
#             for j in range(i+1,len(nums),1):
#                 count += 1
#                 if(nums[i] + nums[j] == target):
#                     return i, j, count
a = Solution()
# b = a.twoSum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], 45)
b = a.twoSum([2,5,5,11], 10)
print(b)
elapsed = (time.clock() - start)
print("Time used:",elapsed)
# a = [11,22,33,44,55]
# for i in range(1,len(a),2):
#     print(a[i])