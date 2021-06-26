def decimal(num, a):
    "Convierte un número (primer parámetro 'num') de sistema en base 2 a 16 (segundo parámetro 'a')."
    global dec
    num = list(num)
    num = list(reversed(num))
    for i in range(len(num)):
        if num[i] == "A":
            num[i] = 10
        elif num[i] == "B":
            num[i] = 11
        elif num[i] == "C":
            num[i] = 12
        elif num[i] == "D":
            num[i] = 13
        elif num[i] == "E":
            num[i] = 14
        elif num[i] == "F":
            num[i] =15
        else:
            pass
    dec = 0
    for i in range(len(num)):
        dec = dec + ((a**i) * int(num[i]))
    return dec

def undec(num, a):
    "Convierte un número decimal, primer parámetro 'num' a sistema en base de 2 a 16, definido como segundo parámetro 'a'"
    hexs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E" , "F"]
    global hex
    hex = []
    num = int(num)
    while num//a not in range(a):
        hex.append(hexs[num%a])
        num = num//a
    hex.append(hexs[int(num)%a])
    hex.append(hexs[int(num)//a])
    hex = "".join(reversed(hex))
    return hex

def conversor(num, a, b):
    try:
        if a != 10 and b != 10:
            decimal(num, a)
            undec(dec, b)
            return hex
        elif a!= 10 and b == 10:
            decimal(num, a)
            return dec
        elif a == 10 and b != 10:
            undec(num, b)
            return hex
        else:
            return num
    except:
        exit()

num = input("Ingrese número a convertir: ")
a = 0
b = 0
while a not in range(2, 17):
    a = int(input("Indique en qué base está expresado el número anterior (2 a 16):"))
while b not in range(2, 17):
    b = int(input("Indique a qué base desea convertir (2 a 16): "))

print(conversor(num, a, b))
    