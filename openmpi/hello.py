def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list

# Example usage
n = 10
fib_sequence = fibonacci(n)
print(fib_sequence)