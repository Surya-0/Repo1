def knapsack(W, wt, val, n):
    K = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(K[i - 1][w], val[i - 1] + K[i - 1][w - wt[i - 1]])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapsack(W, weight, profit, n))
