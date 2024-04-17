class Expression:
    def __init__(self):
        self.output = []  # Chuỗi kết quả biểu thức hậu tố
        self.operators = []  # Stack chứa các toán tử

    def precedence(self, op):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence.get(op, 0)

    def hau_to(self, bt):
        for char in bt:
            if char.isdigit():
                self.output.append(char)
            elif char in {'+', '-', '*', '/'}:
                while (self.operators and 
                       self.precedence(self.operators[-1]) >= self.precedence(char)):
                    self.output.append(self.operators.pop())
                self.operators.append(char)
            elif char == '(':
                self.operators.append(char)
            elif char == ')':
                while self.operators[-1] != '(':
                    self.output.append(self.operators.pop())
                self.operators.pop()  # Discard '('

        while self.operators:
            self.output.append(self.operators.pop())

        return ' '.join(self.output)

# Test the Expression class
if __name__ == "__main__":
    bt = "2 + 3 * 5"
    expression = Expression()
    result = expression.hau_to(bt)
    print("Postfix expression of '{}' is: {}".format(bt, result))
