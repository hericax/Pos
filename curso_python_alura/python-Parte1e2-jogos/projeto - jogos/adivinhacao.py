def jogar():

        import random

        print ("****************************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("****************************************")

        # fazer com que o número secreto seja gerado aleatoriamente
        numero_secreto = random.randrange(1,11)
        total_tentativas = 0
        #rodada = 1
        pontos = 1000

        print("Qual o nível de dificuldade você quer?")
        print("(1)Fácil  (2)Médio  (3)Difícil ")
        nivel = int(input("Defina o nível: "))
        if (nivel == 1):
            total_tentativas = 20
        elif (nivel == 2):
            total_tentativas = 10
        else:
            total_tentativas = 5

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
                    print("Você acertou e fez {}!".format(pontos))
                    break
                else:
                    if (maior):
                        print ("Você errou! Seu chute foi maior que o número secreto")
                    elif (menor):
                        print("Você errou! Seu chute foi menor que o número secreto")
                    pontos_perdidos = abs(numero_secreto - chute) # exemplo: numero_secreto: 40 e chute: 20 => pontos_perdidos=20, se o cálculo for negativo, precisamos ignorar o sinal de menus
                    pontos = pontos - pontos_perdidos


        print ("O número secreto era {}".format(numero_secreto))
        print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()

