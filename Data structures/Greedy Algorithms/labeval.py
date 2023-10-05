def interval_selector(interval_arr, s_arr, k, n):
    m = k + 1
    s_arr.append(interval_arr[k][1])
    while m < n and interval_arr[k][1] >= interval_arr[m][0]:
        m = m + 1
    if m < n:
        interval_selector(interval_arr, s_arr, m, n)
    else:
        return None


if __name__ == '__main__':
    n = int(input("Enter the length of the interval"))
    interval = []
    S = []
    for i in range(n):
        start_point = int(input("Enter the x coordinate"))
        end_point = int(input("Enter the y coordinate"))
        interval.append((start_point, end_point))
    interval.sort(key=lambda x: x[1])
    k = 0
    interval_selector(interval, S, k, n)
    print("The interval is : ",interval)
    print("Final Set is : ",S)
