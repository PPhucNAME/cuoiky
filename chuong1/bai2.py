class Neper:
    @staticmethod
    def calculate_factorial(num):
        if num == 0:
            return 1
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

    @staticmethod
    def calculate_term(k):
        return 1 / Neper.calculate_factorial(k)

    @staticmethod
    def neper_sum(n):
        if n < 0:
            return "Please enter a non-negative integer."
        else:
            sum = 0
            for i in range(n + 1):
                sum += Neper.calculate_term(i)
            return sum

# Using the method
n = int(input("Enter an integer n >= 0: "))
print("The sum of terms a0 + a1 + ... + an is:", Neper.neper_sum(n))
