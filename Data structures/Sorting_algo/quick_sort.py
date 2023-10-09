# def partition(array,low,high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low,high):
#         if array[j]<=pivot:
#             i = i+1
#
#
# def quick_sort(array,low,high):
#     if low<high:
#         pi = partition(array,low,high)
#         quick_sort(array,low,pi-1)
#