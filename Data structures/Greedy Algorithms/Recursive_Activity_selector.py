def activity_selector(activity, k, x, l):
    m = k + 1
    l.append(activity[k])
    while m <= x-1 and activity[m][0] < activity[k][1]:
        m = m + 1
    if m <= x-1:
        activity_selector(activity, m, x, l)
    else:
        return None


n = int(input("Enter the number of activities"))
time = []
for i in range(n):
    start = int(input("Enter the start time"))
    end = int(input("Enter the end time"))
    time.append((start, end))

time.sort(key=lambda x: x[1])
print(time)
arr = []
activity_selector(time, 0, n, arr)
print(arr)
# (1, 4)
# (3, 5)
# (3, 8)
# (0, 6)
# (5, 7)
# (5, 9)
# (6, 10)
# (8, 11)
