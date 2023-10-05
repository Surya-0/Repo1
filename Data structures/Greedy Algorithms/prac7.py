# knapsack problem

def knapsack(items,capacity):
    items.sort(key=lambda x:x[1]/x[0],reverse=True)
    cur_weight = 0
    cur_value = 0
    for item_weights,item_values in items:
        if cur_weight+item_weights < capacity:
            cur_weight += item_weights
            cur_value += item_values
        # elif cur_weight+item_weights > capacity:
        #     fraction = (capacity - cur_weight)/item_weights
        #     cur_value += item_values*fraction
        #     cur_weight += item_weights*fraction
        #     break
    return cur_value

if __name__ == '__main__':
    items = [(10, 60), (20, 100), (30, 120)]  # (weight, value) pairs
    knapsack_capacity = 50
    value = knapsack(items, knapsack_capacity)
    print(value)
