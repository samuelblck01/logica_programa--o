valor =int(input("qual valor ?"))

nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_1 = 0

nota_100 = valor // 100 
valor %= 100 
nota_50 = valor // 50 
valor %= 50
nota_20 = valor // 20 
valor %= 20 
nota_10 = valor// 10 
valor %= 10 
nota_5 = valor// 5
valor %= 5 
nota_2 = valor// 2 
valor %= 2 
nota_1 = valor // 1 
valor %= 1 

print("quantidade de notas 100 = " ,nota_100)
print("quantidade de notas 50 = " ,nota_50)
print("quantidade de notas 20 = " ,nota_20)
print("quantidade de notas 10 = " ,nota_10)
print("quantidade de notas 5 = " ,nota_5)
print("quantidade de notas 2 = " ,nota_2)
print("quantidade de notas 1 = " ,nota_1)

