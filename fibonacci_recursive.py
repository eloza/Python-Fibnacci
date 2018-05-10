nth_num = 10
fib_list = []


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(f"Recursive Fibonacci: {nth_num}th term is {fibonacci_recursive(nth_num)}")
for i in range(nth_num + 1):
    fib_list.append(fibonacci_recursive(i))
print(str(fib_list)[1:-1])
