
lower_cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]

upper_cyrillic = [chr(i) for i in range(ord('А'), ord('Я') + 1)]

lower_cyrillic = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
upper_cyrillic = ''.join(map(chr, range(ord('А'), ord('Я') + 1)))


def alphabet(shift):
    shift = shift % len(lower_cyrillic)
    return lower_cyrillic[shift:] + \
           lower_cyrillic[:shift] + \
           upper_cyrillic[shift:] + \
           upper_cyrillic[:shift]


def encrypt_caesar(msg, shift):
    a1 = lower_cyrillic + upper_cyrillic
    a2 = alphabet(shift)
    return msg.translate(str.maketrans(a1, a2))


def decrypt_caesar(msg, shift):
    a1 = lower_cyrillic + upper_cyrillic
    a2 = alphabet(shift)
    return msg.translate(str.maketrans(a2, a1))

msg = "Да здравствует салат Цезарь!"
shift = 15
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)