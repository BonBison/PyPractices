symbol = input("Введите один символ — строчная буква: ")
words = input("Введите предложение: ").split()
words_with_symbol = [word for word in words if symbol.lower() in word.lower()]
print(*words_with_symbol, sep='\n')