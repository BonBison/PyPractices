password = 'admin123'

def ask_password():
    global password
    for i in range(0, 3):
        s = input("Введите пароль:\n")
        if s == password:
            print('Пароль принят!')
            return
        if i == 2:
            print("В доступе отказано >:(")
            return

ask_password()