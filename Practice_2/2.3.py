result = input("Введите результат бросков монетки: ")
count = 1
n = 1

for i in range(1, len(result)):
  if result[i] == result[i-1] == 'о':
    count += 1
  else:
    n = max(n, count)
    count = 1

print(max(n, count))