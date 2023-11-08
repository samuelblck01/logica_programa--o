valor = float(input("Digite o valor monetário: "))

notas_e_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

contagem = {}

for nota_moeda in notas_e_moedas:
    qtd_notas_moedas = int(valor // nota_moeda)
    valor = round(valor % nota_moeda, 2)
    contagem[nota_moeda] = qtd_notas_moedas

print("Notas e moedas necessárias:")
for nota_moeda, quantidade in contagem.items():
    if nota_moeda >= 1:
        print(f"{quantidade} nota(s) de R${nota_moeda:.2f}")
    else:
        centavos = int(nota_moeda * 100)
        print(f"{quantidade} moeda(s) de R${centavos / 100:.2f}")
