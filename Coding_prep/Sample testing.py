class Solution(object):
    def findDuplicate(self, nums):
        d = {}
        for i in nums:
            d[i] = nums.count(i)
        L = []
        for key, value in d.items():
            if value > 1:
                L.append(key)
        return L


# Example usage:
solution_instance = Solution()
nums_list = [1, 2, 3, 4, 5, 3, 2]  # Example list with a duplicate element (3)
result = solution_instance.findDuplicate(nums_list)
print(result)  # This should print the duplicate element (3)
