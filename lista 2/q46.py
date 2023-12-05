
tipo  = input("qual o seu tipo? ")
quantidade = int(input('quanto foi a quantidade de kWh usado: '))
if tipo == 'residencial':
    if quantidade <= 500 : 
        print('o preço a ser pago por kWh é igual a: R$ 0, 40') 
    if quantidade > 500: 
     print('o preço a ser pago por kWh é igual a: R$ 0, 65') 

elif tipo == 'comercial' :    
    if quantidade <= 1000 : 
        print('o preço a ser pago por kWh é igual a: R$ 0, 55') 
    if quantidade > 1000: 
        print('o preço a ser pago por kWh é igual a: R$ 0, 65') 

elif tipo == 'industrial': 
    if quantidade <= 5000 : 
        print('o preço a ser pago por kWh é igual a: R$ 0, 55') 
    if quantidade > 5000: 
        print('o preço a ser pago por kWh é igual a: R$ 0, 60') 

 