string = input("Введите предложение: ")
words = string.split()
print(*words, sep='\n')