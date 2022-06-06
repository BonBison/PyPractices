library = set()
M = int(input("Введите число книг в домашней библиотеке: "))
task = set()
N = int(input("Введите число книг в списке на лето: "))

for i in range(M):
    book = input()
    library.add(book)
for i in range(N):
    book = input()
    task.add(book)
    if book in library:
        print('YES')
    else:
        print('NO')