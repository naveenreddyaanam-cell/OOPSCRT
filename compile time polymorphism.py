# Define a class Calculator.
class Calculator:
    def add(self, a, b, c = 0):
        return a + b + c

# Create an instance of class Calculator.
calc = Calculator()



result1 = calc.add(1, 2)
result2 = calc.add(1, 2, 3)


print(result1)
print(result2)
