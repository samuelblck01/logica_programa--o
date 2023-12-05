
distancia = int(input("qual a distância em KM que irás percorrer ? "))

if distancia <= 200: 
    print(f'o preço a ser pago é: {distancia * 0.50}') 

elif distancia > 200: 
     print(f'o preço a ser pago é: {distancia * 0.45}')      
     