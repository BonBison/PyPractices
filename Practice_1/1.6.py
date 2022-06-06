d = int(input("День: "))
m = int(input("Месяц: "))
y = int(input("Год: "))

if (m > 3):
    m = m - 2
else:
    m = m - 2
    m = 12 + m
    y = y - 1
c = y // 100
day_of_week = (7 + d + ((13*m - 1) // 5 ) + y + (y // 4 + c // 4 - 2*c + 777) - 1) % 7

print(day_of_week)