while True:
    opcoes = ['pedra', 'papel', 'tesoura']
    
    opcao_computador = random.randint(0, 2)
    escolha_computador = opcoes[opcao_computador]

    opcao_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if opcao_jogador in opcoes:
        print(f'O computador escolheu: {escolha_computador}')
        print(f'Você escolheu: {opcao_jogador}')

        if (opcao_jogador == 'pedra' and escolha_computador == 'tesoura') or \
           (opcao_jogador == 'tesoura' and escolha_computador == 'papel') or \
           (opcao_jogador == 'papel' and escolha_computador == 'pedra'):
            print('Jogador venceu!')
        elif opcao_jogador == escolha_computador:
            print('Empate!')
        else:
            print('Computador venceu!')
    else:
        print('Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.')

    jogar_novamente = input('Quer jogar novamente? (s/n): ')
    if jogar_novamente.lower() != 's':
        break


 