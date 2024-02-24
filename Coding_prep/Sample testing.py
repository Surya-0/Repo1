# # class Solution(object):
# #     def findDuplicate(self, nums):
# #         d = {}
# #         for i in nums:
# #             d[i] = nums.count(i)
# #         L = []
# #         for key, value in d.items():
# #             if value > 1:
# #                 L.append(key)
# #         return L
# #
# class Solution(object):
#     def containsDuplicate(self, nums):
#         s = set()
#         for i in nums:
#             if i not in s:
#                 s.add(i)
#             elif i in s:
#                 return True
#         return False
#
#
# #
# # # Example usage:
# solution_instance = Solution()
# nums_list = [1, 2, 3, 4, 5, 3, 2]  # Example list with a duplicate element (3)
# result = solution_instance.containsDuplicate(nums_list)
# print(result)  # This should print the duplicate element (3)
# # d = {1:'apple', 2:'banana', 3:'cherry'}
# # for key, value in d.items():
# #     print(key, value)

arr = [1,2,4,2,3,8,9,6,7]
arr.sort()
print(arr)