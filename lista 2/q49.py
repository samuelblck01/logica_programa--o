A = int(input("digite um valor: "))
B = int(input("digite um valor: "))
C = int(input("digite um valor: ")) 

if A >= B + C  :
    print("NAO FORMA TRIANGULO")    
elif A**2 == B**2 + C**2 : 
    print(" TRIANGULO RETANGULO") 

elif A**2 > B**2 + C**2: 
    print("TRIANGULO OBTUSANGULO ") 

elif    A**2 < B**2 + C**2 : 
    print("TRIANGULO ACUTANGULO ") 

elif (A == B) and (B==C): 
    print("TRIANGULO EQUILATERO") 

elif A == B or B == C or C == A :
    print("TRIANGULO ISOSCELES")

 