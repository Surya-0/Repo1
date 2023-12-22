def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = [0]

    def knapsack_util(curr_value, curr_weight, index):
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
weights = [1,2,3,4,5]
values = [3, 4, 2, 10,7]
capacity =10

result = knapsack_backtracking(weights, values, capacity)
print(f"The maximum value for the 0/1 Knapsack problem is: {result}")