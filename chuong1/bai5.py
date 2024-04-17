class Number:
    @staticmethod
    def calculate_sum_of_divisors(n):
        sum_divisors = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                sum_divisors += i
                if i != n // i:
                    sum_divisors += n // i
        return sum_divisors

    @staticmethod
    def classify_numbers(x, y):
        if x <= 0 or y <= 0:
            print("Please enter positive integers.")
            return

        for num in range(x, y + 1):
            sum_divisors = Number.calculate_sum_of_divisors(num)

            if sum_divisors < num:
                print(num, "is deficient.")
            elif sum_divisors == num:
                print(num, "is perfect.")
            else:
                print(num, "is abundant.")

# Using the method
x = int(input("Enter the lower bound x: "))
y = int(input("Enter the upper bound y: "))
Number.classify_numbers(x, y)
