def merge_sort(brr):
    if len(brr) > 1:
        mid = len(brr) // 2

        L = brr[:mid]
        R = brr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                brr[k] = L[i]
                i += 1

            else:
                brr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            brr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            brr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    arr = [1, 7, 3, 2]
    print("Given array is", end="\n")
    print(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
