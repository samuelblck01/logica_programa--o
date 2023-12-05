hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))


tempo_inicial_em_minutos = hora_inicial * 60 + minuto_inicial
tempo_final_em_minutos = hora_final * 60 + minuto_final


duracao_em_minutos = tempo_final_em_minutos - tempo_inicial_em_minutos


if duracao_em_minutos < 1:
    duracao_em_minutos += 24 * 60  
elif duracao_em_minutos > 24 * 60:
    duracao_em_minutos %= 24 * 60  


duracao_horas = duracao_em_minutos // 60
duracao_minutos = duracao_em_minutos % 60


print(f"Duração do jogo: {duracao_horas} hora(s) e {duracao_minutos} minuto(s)")
 