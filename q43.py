materia1 = float(input("Digite a nota da matéria 1: "))
materia2 = float(input("Digite a nota da matéria 2: "))
materia3 = float(input("Digite a nota da matéria 3: "))

faltas = int(input("Digite o número total de faltas: "))

aulas_totais = 30  # 3 matérias x 10 aulas cada
frequencia = ((aulas_totais - faltas) / aulas_totais) * 100

aprovado = materia1 > 7 and materia2 > 7 and materia3 > 7 and frequencia >= 75

print("Aluno aprovado?", aprovado)
