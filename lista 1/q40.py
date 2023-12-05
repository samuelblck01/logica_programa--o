expressao1 = 3 < 2 ** 3 and 3 == 3
print(expressao1)  # Resultado: True
expressao2 = 0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2)
print(expressao2)  # Resultado: True
#Primeiro, 0 != 4 é avaliado, o que é verdadeiro.
#Em seguida, (3/3 == 1) é avaliado, o que é verdadeiro.
#Em seguida, (5 + 1) / 3 é calculado, resultando em 2.
#Por fim, 1 and 2 == 2 é avaliado, o que é verdadeiro.
#Finalmente, a expressão lógica True or True é avaliada, resultando em True.



