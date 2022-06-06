def byte(byte):
    return byte * 8

def Kbyte(kilo):
    return kilo * 1024

print(f"1 бит - минимальная единица количества информации.")
print(f"1 байт = {byte(1)} бит.")
print(f"1 Килобит = {Kbyte(1)} бита.")
print(f"1 Килобайт = {Kbyte(1)} байта.")
print(f"1 Килобайт = {byte(Kbyte(1))} бит.")