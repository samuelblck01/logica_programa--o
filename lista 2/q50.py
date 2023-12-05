
A = int(input("digite um valor : "))
B = int(input("digite um valor : "))
C = int(input("digite um valor : "))
D = int(input("digite um valor : "))


if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores não aceitos")
 