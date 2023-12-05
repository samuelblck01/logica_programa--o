
salario = int(input("qual seu salário? "))

if salario <= 1250: 
    print( f'seu novo salario é igual a : {salario * 15/100 + salario}' )
    
elif salario > 1250: 
    print( f'seu novo salario é igual a : {salario * 10/100 + salario}' )       
  