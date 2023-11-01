
valor = int(input("Digite o valor:"))

notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = notas1 = 0


while valor > 0:
    if valor >= 100:
        valor -= 100
        notas100 += 1
    elif valor >= 50:
        valor -= 50
        notas50 += 1
    elif valor >= 20:
        valor -= 20
        notas20 += 1
    elif valor >= 10:
        valor -= 10
        notas10 += 1
    elif valor >= 5:
        valor -= 5
        notas5 += 1
    elif valor >= 2:
        valor -= 2
        notas2 += 1
    else:
        valor -= 1
        notas1 += 1


print("Valor lido:", valor)
print("Notas de R$100:", notas100)
print("Notas de R$50:", notas50)
print("Notas de R$20:", notas20)
print("Notas de R$10:", notas10)
print("Notas de R$5:", notas5)
print("Notas de R$2:", notas2)
print("Notas de R$1:", notas1)
