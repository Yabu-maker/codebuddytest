"""计算斐波那契数列前 N 项"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fib(10)
