a = float(input("Количество столбцов в таблице: "))
b = float(input("Количество строк в таблице: "))

for i in range(1, int(b) + 1):
    print()
    for j in range(1, int(a) + 1):
        print(j / i, end=' ')
print()