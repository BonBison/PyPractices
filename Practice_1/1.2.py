login = input("Введите логин: ")
mail = input("Введите резервный адрес электронной почты: ")

if '@' in login:
    print("Некорректный логин!")
else:
    if '@' in mail:
        print("OK! 👍")
    else:
        print("Некорректный адрес!")