# activity selection
def activity_selection(activity, k, n, arr):
    m = k + 1
    arr.append(activity[k])
    while  m <= n - 1 and activity[m][0] < activity[k][1]:
        m = m + 1
    if m <= n - 1:
        activity_selection(activity, m, n, arr)
    else:
        return None


if __name__ == '__main__':
    n = int(input("Enter the number of activities"))
    activity_list = []
    brr = []
    for i in range(n):
        start_time = int(input("Enter the start time"))
        end_time = int(input("Enter the end time"))
        activity_list.append((start_time, end_time))
    k = 0
    activity_list.sort(key=lambda x: x[1])
    activity_selection(activity_list, k, n, brr)
    print(brr)
