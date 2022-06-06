a = float(input("Введите несколько действительных чисел на отдельных строках (действительное число, меньшее -300):\n"))

sum = 0
count = 0
while a > -300:
    sum += a
    count += 1
    a = float(input())

print(round(sum/count, 1))