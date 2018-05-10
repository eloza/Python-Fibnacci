nth_num = 10
fib_list = []

def fibonacci_iterative(n):
    if n == 0:
        return n
    a, b = 1, 1
    for num in range(n - 1):
        a, b = b, a + b
    return a


print(f"Iterative Fibonacci: {nth_num}th term is {fibonacci_iterative(nth_num)}")
for i in range(nth_num + 1):
    fib_list.append(fibonacci_iterative(i))
print(str(fib_list)[1:-1])
