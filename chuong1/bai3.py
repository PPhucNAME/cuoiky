class GCD:
    @staticmethod
    def recursive_gcd(m, n):
        if n == 0:
            return m
        else:
            return GCD.recursive_gcd(n, m % n)

    @staticmethod
    def iterative_gcd(m, n):
        while n != 0:
            m, n = n, m % n
        return m

# Using the method
m = int(input("Enter a positive integer m: "))
n = int(input("Enter a positive integer n: "))

if m <= 0 or n <= 0:
    print("Please enter positive integers.")
else:
    print("The greatest common divisor (GCD) of", m, "and", n, "using recursion is:", GCD.recursive_gcd(m, n))
    print("The greatest common divisor (GCD) of", m, "and", n, "using iteration is:", GCD.iterative_gcd(m, n))
