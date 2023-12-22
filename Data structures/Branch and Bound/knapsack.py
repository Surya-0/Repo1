from queue import Queue
class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def bound_computer(node: Node, n, knap, array):  # fractional knapsack sub problem -> gives the bound
    if node.weight > knap:
        return 0

    profitBound = node.profit
    j = node.level + 1
    totalWeight = int(node.weight)

    while j < n and totalWeight + int(array[j].weight) <= knap:
        totalWeight += int(array[j].weight)
        profitBound += array[j].value
        j += 1

    if j < n:
        profitBound += (int(W - totalWeight) / array[j].weight) * array[j].value

    return profitBound  # gets assigned to the node's profit

def knapsack_bb(n, array, W):
    # arr.sort(key=sort_cmp, reverse=True)
    q = Queue()
    root = Node(-1, 0, 0, 0)
    q.put(root)

    maxprofit = 0
    # print("I am outside")
    while not q.empty():
        # print("Just got in")
        parent = q.get()

        if parent.level == n-1:
            continue

        yes_node = Node(level=parent.level + 1, profit=parent.profit + array[parent.level + 1].value,
                        bound=0, weight=parent.weight + array[parent.level + 1].weight)

        yes_node.bound = bound_computer(yes_node, n, W, array)
        if yes_node.weight <= W and yes_node.profit > maxprofit:
            maxprofit = yes_node.profit

        if yes_node.bound > maxprofit:
            q.put(yes_node)

        no_node = Node(level=parent.level+1, profit=parent.profit, bound=0, weight=parent.weight)
        no_node.bound = bound_computer(no_node, n, W, array)

        if no_node.bound > maxprofit:
            q.put(no_node)

        # print("I'm here")

        for i in q.queue:
            print(i.weight, " ", i.profit, " ", i.bound)
        print("----")


    return maxprofit


def sort_cmp(x):
    return float(x.value)/x.weight

if __name__ == '__main__':
    W = 16
    # arr = [
    #     Item(2, 40),
    #     Item(3.14, 50),
    #     Item(1.98, 100),
    #     Item(5, 95),
    #     Item(3, 30)
    # ]

    arr = [
        Item(2, 40),
        Item(5, 30),
        Item(10, 50),
        Item(5, 10)
    ]
    # arr.sort(key=sort_cmp, reverse=True)
    # for i in arr:
    #     print((i.weight, i.value), end=" ")

    print("Max Profit: ", knapsack_bb(len(arr), arr, W))