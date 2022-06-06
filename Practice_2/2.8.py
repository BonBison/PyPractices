string_list = [input("Введите текст:\n").split(",") for _ in range(int(input("Введите число рядов таблицы:\n")))]
data_list = []
for _ in range(int(input("Введите число элементов таблицы, которые нужно будет вывести:\n"))):
    string_number, word_number = [int(i) for i in input("Введите номера строк и номера столбцов (нумерация с нуля):\n").split(",")]
    data_list.append(string_list[string_number][word_number])
print(*data_list, sep="\n")