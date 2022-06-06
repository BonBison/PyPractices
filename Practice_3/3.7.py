print("Введите матрицу в диапазоне от 0 до 99, числа которой разделёны пробелами: ")
mas = []

for i in range(10):
    mas.append(input())

print(any(['0' in i.split() for i in mas]))