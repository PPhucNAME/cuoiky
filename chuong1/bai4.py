class PascalTriangle:
    @staticmethod
    def pascal(n):
        if n <= 0:
            print("Please enter a positive integer.")
            return
        triangle = []
        for i in range(n):
            row = [1] * (i + 1)
            if i > 1:
                for j in range(1, i):
                    row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        for i in range(n):
            print("n=" + str(i), end=" ")
            for j in range(i + 1):
                print(triangle[i][j], end=" ")
            print()

# Using the method
n = int(input("Enter a positive integer n: "))
PascalTriangle.pascal(n)
