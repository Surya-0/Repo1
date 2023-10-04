def activity_selector(activity, k, l, list_activity):
    m = k + 1
    list_activity.append(activity[k])
    while m <= l - 1 and activity[m][0] < activity[k][1]:
        m = m + 1
    if m <= l - 1:
        activity_selector(activity, m, l,list_activity)
    else:
        return None


if __name__ == '__main__':
    n = int(input("Enter the number of activities"))
    L = []
    for i in range(n):
        start_time = int(input("Enter the start time"))
        end_time = int(input("Enter the end time"))
        L.append((start_time, end_time))
    k = 0
    arr = []
    L.sort(key=lambda x: x[1])
    activity_selector(L, k, n, arr)
    print(arr)
