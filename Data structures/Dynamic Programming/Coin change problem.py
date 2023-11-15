def get_num_ways(val, coins):
    ways = [0] * (val + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j - coins[i]]
    return ways[val]


if __name__ == "__main__":
    coins = [1, 5, 10]
    print("The coins array is : ", coins)
    value = 15
    print("The num of ways to arrive at the solution : ", get_num_ways(value, coins))
