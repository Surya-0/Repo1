def sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[i]:
                l[j - 1], l[i] = l[i], l[j - 1]
    return l


print(sort([8, 7, 6, 10, 4, 9]))
