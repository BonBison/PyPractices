n = int(input("Введите количество строк:\n"))
data = []

for i in range(n):
    data.append(input())

for string in data:
    if "Кот" in string or "кот" in string:
        print("МЯУ!")
        exit(0)

print("НЕТ!")