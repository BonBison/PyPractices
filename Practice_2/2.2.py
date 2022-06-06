string = input("Введите сообщение: ")
number = int(input("Введите номер буквы: "))

if number >= 1 and number <= len(string):
    print(string[number - 1])
else:
    print("ОШИБКА")