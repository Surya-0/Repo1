def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = [0]

    def knapsack_util(curr_value, curr_weight, index):
        print(f"Debug: index={index}, curr_value={curr_value}, curr_weight={curr_weight}")
        if index == n:
            max_value[0] = max(max_value[0], curr_value)
            return

        # Include the current item if it doesn't exceed the capacity
        if curr_weight + weights[index] <= capacity:
            knapsack_util(curr_value + values[index], curr_weight + weights[index], index + 1)

        # Exclude the current item and move to the next one
        knapsack_util(curr_value, curr_weight, index + 1)

    knapsack_util(0, 0, 0)
    return max_value[0]

# Example usage
weights = [5, 10, 12, 13, 15, 18]
values = [3, 4, 2, 10, 7]
capacity = 30

result = knapsack_backtracking(weights, values, capacity)
print(f"The maximum value for the 0/1 Knapsack problem is: {result}")



# def is_safe(sum_val, it, target, weights):
#     if (sum_val + weights[it]) > target:
#         return False
#     return True
#
#
# #
# # def subset_problem(Mat, sum_val, it, length, target, weights):
# #     print("iterator is : ", it)
# #     # print(Mat)
# #     print(sum_val)
# #     if sum_val == 30:
# #         print("The solution is", Mat)
# #         print()
# #         return
# #     for i in range(it,length):
# #         if is_safe(sum_val, it, target, weights):
# #             Mat[it] = 1
# #             print("   ",sum_val)
# #             sum_val += weights[it]
# #             subset_problem(Mat, sum_val, it + 1, length, target, weights)
# #
#
#
# if __name__ == '__main__':
#     weights = [5, 10, 12, 13, 15, 18]
#     result = 30
#     sum_val = 0
#     n = len(weights)
#     mat = [0] * len(weights)
#     # print(mat)
#     subset_problem(mat, sum_val, 0, n, result, weights)

# Print all subsets if there is at least one subset of set[]
# with a sum equal to the given sum
# flag = False

#
# def print_subset_sum(i, n, _set, target_sum, subset):
#     global flag
#     # If targetSum is zero, then there exists a subset
#     if target_sum == 0:
#         # Prints valid subset
#         flag = True
#         print("[", end=" ")
#         for element in subset:
#             print(element, end=" ")
#         print("]", end=" ")
#         return
#
#     if i == n:
#         # Return if we have reached the end of the array
#         return
#
#     # Not considering the current element
#     print_subset_sum(i + 1, n, _set, target_sum, subset)
#
#     # Consider the current element if it is less than or equal to targetSum
#     if _set[i] <= target_sum:
#         # Push the current element into the subset
#         subset.append(_set[i])
#
#         # Recursive call for considering the current element
#         print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)
#
#         # Remove the last element after recursive call to restore subset's original configuration
#         subset.pop()
#
#
# # Driver code
# if __name__ == "__main__":
#     # Test case 1
#     set_1 = [5, 10,12,13,15,18]
#     sum_1 = 30
#     n_1 = len(set_1)
#     subset_1 = []
#     print("Output 1:")
#     print_subset_sum(0, n_1, set_1, sum_1, subset_1)
#     print()
#     flag = False
#
#     # Test case 2
#     set_2 = [3, 34, 4, 12, 5, 2]
#     sum_2 = 30
#     n_2 = len(set_2)
#     subset_2 = []
#     print("Output 2:")
#     print_subset_sum(0, n_2, set_2, sum_2, subset_2)
#     if not flag:
#         print("There is no such subset")
