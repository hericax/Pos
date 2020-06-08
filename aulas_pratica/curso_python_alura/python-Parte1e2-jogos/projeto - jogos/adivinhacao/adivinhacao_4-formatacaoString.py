print ("****************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("****************************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

while (rodada <= total_tentativas):
        print("Tentativa {} de {}", format(rodada, total_tentativas))   # interpolação de string
        # permitir que o usuário informe um valor. Tudo o que é digita no imput é recebido como string,
        # #logo precisa ser convertido para inteiro para ser comparado com o numero_sercreto
        chute_str = input("Digite seu número: ")
        print("Você digitou: ", chute_str)
        chute   = int(chute_str)

        acertou =  chute == numero_secreto
        maior   =   chute >  numero_secreto
        menor   =  chute <   numero_secreto

        # verificar se o chute é igual ao número secreto
        if (acertou):
            print("Você acertou!")
        else:
            if (maior):
                print ("Você errou! Seu chute foi maior que o número secreto")
            elif (menor):
                print ("Você errou! Seu chute foi menor que o número secreto")

        rodada = rodada + 1
# print("Fim do jogo!")

