print ("****************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("****************************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas+1):  # como o valor maximo do range é exclusivo, preciso fazê-lo "+1"
        print ("Tentativa ", rodada," de " , total_tentativas)
        # permitir que o usuário informe um valor. Tudo o que é digita no imput é recebido como string,
        # #logo precisa ser convertido para inteiro para ser comparado com o numero_sercreto
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)

        chute   = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue # mantem dentro do laça, indo para a próxima iteração

        acertou =  chute == numero_secreto
        maior   =   chute >  numero_secreto
        menor   =  chute <   numero_secreto

        # verificar se o chute é igual ao número secreto
        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print ("Você errou! Seu chute foi maior que o número secreto")
            elif (menor):
                print ("Você errou! Seu chute foi menor que o número secreto")



print("Fim do jogo!")

