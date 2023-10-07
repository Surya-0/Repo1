def counting_sort(brr):
    count_arr = (max(brr) + 1) * [0]
    for i in brr:
        count_arr[i] += 1

    for i in range(len(count_arr) - 1):
        count_arr[i + 1] = count_arr[i] + count_arr[i + 1]
    # print(count_arr)

    sorted_arr = len(brr) * [0]
    for i in range(len(brr) - 1, -1, -1):
        count_arr[brr[i]] = count_arr[brr[i]] - 1
        ele = count_arr[brr[i]]
        sorted_arr[ele] = brr[i]
    print(sorted_arr)


if __name__ == '__main__':
    arr = [1, 4, 1, 2, 7, 5, 2]
    print(arr)
    counting_sort(arr)
