# This will be the original code
import time


def Counting_sort(A,B,k):
    C = [0]*(k+1)
    # print(C)
    for j in range(0,len(A)):
        C[A[j]] += 1
    print(C)
    
    for i in range(1,k+1):
        C[i]= C[i]+C[i-1]
    print(C)
    
    for j in range(len(A)-1,-1,-1):
        C[A[j]] = C[A[j]]-1
        B[C[A[j]]] = A[j]
        
    
A = [4, 2, 2, 8, 3, 3, 0]
# A = [1,4,1,2,7,5,2]
B = [0] * len(A)
k = max(A)  # Assuming k is the maximum value in A

Counting_sort(A, B, k)
print("Sorted Array : ",B)



# This will be the modified code 

def counting_sort(A, B, k):
    C = [0] * (k + 1)

    for i in range(0, len(A)):
        C[A[i]] += 1
    print(C)

    CU = 0
    for i in range(0, k + 1):
        temp = C[i]
        C[i] = CU
        CU += temp
    
    print(C)
    for j in range(1, len(A) + 1):
        B[C[A[j - 1]]] = A[j - 1]
        C[A[j - 1]] += 1
    print(C)

# Example usage
A = [4, 2, 2, 8, 3, 3, 0]
B = [0] * len(A)
k = max(A)  # Assuming k is the maximum value in A

counting_sort(A, B, k)
print("Sorted array B:", B)
