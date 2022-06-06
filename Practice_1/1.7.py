import time

s = int(input("Введите целое число: "))

while s >= 0:
    print(f"Осталось секунд: {s}")
    time.sleep(1)
    s -= 1

print("Пуск")