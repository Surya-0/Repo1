def knapsack(products,capacity):
    products.sort(key=lambda x: x[1]/x[0], reverse=True)
    cur_weight = 0
    cur_value = 0
    for item in products:
        item_weight,item_value = item
        if cur_weight+item_weight < capacity:
            cur_weight += item_weight
            cur_value += item_value
    return cur_value



if __name__ == '__main__':
    items = [(10, 60), (20, 100), (30, 120)]  # (weight, value) pairs
    knapsack_capacity = 50
    max_value = knapsack(items, knapsack_capacity)
    print("Maximum Value:", max_value)