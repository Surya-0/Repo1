import random
import time
import matplotlib.pyplot as plt


def kadane(arr):
    m = len(arr)
    local_max = 0
    global_max = -float('inf')
    for i in range(0, m):
        local_max = max(arr[i], arr[i] + local_max)
        if local_max > global_max:
            global_max = local_max
    return global_max


if __name__ == '__main__':
    # n = int(input("Enter the size"))
    # L = []
    # for i in range(n):
    #     L.append(int(input("Enter the element")))
    # print(L)
    time_arr = []
    for j in range(10):
        start_time = time.time()
        M = [random.randint(-1000, 1000) for i in range(1000)]
        # print(M)
        max_subarray_large = kadane(M)
        end_time = time.time()
        time_arr.append(end_time - start_time)
    print(time_arr)
    plt.plot(time_arr)
    plt.show()
    # max_subarray = kadane(L)
    # print(max_subarray)
    # print(max_subarray_large)

# %%
