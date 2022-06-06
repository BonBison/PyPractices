a = float(input("Введите первое число:\n"))
b = float(input("Введите второе число:\n"))
operation = input("Введите знак операции:\n")

value = 0
if operation == '+':
    value = a + b
elif operation == '-':
    value = a - b
elif operation == '*':
    value = a * b
elif operation == '/' and b != 0:
    value = a / b
else:
    value = 888888

print(value)