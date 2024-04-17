class Fibonacci:
    @staticmethod
    def recursive_fibonacci(n):
        if n <= 1:
            return n
        else:
            return Fibonacci.recursive_fibonacci(n-1) + Fibonacci.recursive_fibonacci(n-2)

    @staticmethod
    def iterative_fibonacci(n):
        if n <= 1:
            return n
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                c = a + b
                a, b = b, c
            return b

# Using the methods
n = int(input("Enter an integer n >= 0: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    print("The", n, "th Fibonacci number using recursion is:", Fibonacci.recursive_fibonacci(n))
    print("The", n, "th Fibonacci number using iteration is:", Fibonacci.iterative_fibonacci(n))
