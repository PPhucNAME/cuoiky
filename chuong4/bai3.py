class Expression:
    def __init__(self):
        self.operands = []
        self.operators = []

    def is_higher_precedence(self, op1, op2):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        if op2 not in precedence:
            return False  # Không phải toán tử, nên không có ưu tiên
        return precedence[op1] >= precedence[op2]

    def evaluate(self, bt):
        for char in bt:
            if char.isdigit():
                self.operands.append(int(char))
            elif char in {'+', '-', '*', '/'}:
                while self.operators and self.is_higher_precedence(self.operators[-1], char):
                    self.evaluate_operator()
                self.operators.append(char)
            elif char == '(':
                self.operators.append(char)
            elif char == ')':
                while self.operators[-1] != '(':
                    self.evaluate_operator()
                self.operators.pop()  # Discard '('
        
        while self.operators:
            self.evaluate_operator()

        return self.operands[-1]

    def evaluate_operator(self):
        operator = self.operators.pop()
        operand2 = self.operands.pop()
        operand1 = self.operands.pop()

        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2

        self.operands.append(result)

# Test the Expression class
if __name__ == "__main__":
    bt = "3+4*5-7/2"
    expression = Expression()
    result = expression.evaluate(bt)
    print("Result of the expression '{}' is: {}".format(bt, result))
