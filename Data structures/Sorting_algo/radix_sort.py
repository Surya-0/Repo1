def radix_sort(brr):
    m = max(brr)
    digit = 1
    while (m//digit)>0:
        bucket = [[] for i in range(10)]
        for i in range(len(brr)):
            index = brr[i]//digit
            bucket[index%10].append(brr[i])
        digit = digit*10
        brr = []
        for container in bucket:
            for element in container:
                brr.append(element)
    print(brr)


if __name__ == '__main__':
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)