import random #para escolher uma palavra aleatória

def jogar():

      abertura() #imprime a mensagem de abertura que está dentro de um 'modulo'
      palavra_secreta = carrega_palavra_sevrete() # escolhe a palabra secreta

      letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # preenche a palavra_secreta com "-"
      print(letras_acertadas)

      #inicialização das variáveis
      enforcou = False
      acertou = False
      erros = 0


      # enquanto não enforcou e não acertou, vamos jogar
      while (not enforcou and not acertou):
            chute = pede_chute() # estou pedindo o chute do jogador

            # Ao acertar a letra, colocar a letra no lugar correspondente na palavra_acertada
            if (chute in palavra_secreta):
                  marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            else:
                  erros += 1 # é a mesma coisa que erros = erros + 1
                  print("Ops, você errou! Faltam {} tentativas.\n".format(6 - erros))
                  desenha_forca(erros)

            enforcou = erros == 7  # se ele já tentou 6 vezes, a variável enforcou = True
            acertou = "_" not in letras_acertadas  # enquanto tiver o "-" dentro das letras_acertadas, ele não acertou a palavra logo acertou = False
            print(letras_acertadas)

      # Exibe a menssagem se o jogador acertou ou perdeu
      if (acertou):
            imprime_messagem_vencedor()
      else:
            imprime_messagem_perdedor(palavra_secreta)



# define a mensagem de abertura do joto
def abertura():
      print ("****************************************")
      print ("***********Jogo da forca****!*************")
      print ("****************************************")
      print("\n")


# lê o arquivo com as palavras e escolhe uma aleatóriamente
def carrega_palavra_sevrete():
      arquivo = open("palavras.txt", "r")
      palavras = []

      for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

      arquivo.close()

      numero = random.randrange(0, len(palavras))  #escolhe um palavra aleatóriamente,
      palavra_secreta = palavras[numero].upper()  #inicializa a palabra secreta
      return palavra_secreta

#inicializa a palavra_acertada com "_"
def inicializa_letras_acertadas(palavra):
      return["_" for letra in palavra]  #list comprehensions - com o for dentro da inicialização (redução de linhas de código)

# solicita o chute do jogador
def pede_chute():
      chute = input("Informe um letra: ")
      chute = chute.strip().upper()  #retira todos os spaces e caracterees especiais antes e depois da palavra. Coloca  a palabra em letras maiúsculas
      return chute

# Se o jogador acertar, ele coloca a letra acertada na posição onde a letra esta na palavra
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
      index = 0
      for letra in palavra_secreta: # procurar a letra digitada na palavra, até que a palavra termine
            if (chute == letra):
                  letras_acertadas[index] = letra  # lista que guardas as letras acertadas na posição correta
            index += 1  #é a mesma coisa que index = index + 1
      print("Letra correta!\n")


# Se o jogador acertou a palavra, exibe uma mensagem
def imprime_messagem_vencedor():
      print("Parabéns, você ganhou!")
      print("       ___________      ")
      print("      '._==_==_=_.'     ")
      print("      .-\\:      /-.    ")
      print("     | (|:.     |) |    ")
      print("      '-|:.     |-'     ")
      print("        \\::.    /      ")
      print("         '::. .'        ")
      print("           ) (          ")
      print("         _.' '._        ")
      print("        '-------'       ")

# Se o jogador errou a palavra, exibe uma mensagem
def imprime_messagem_perdedor(palavra_secreta):
      print("Puxa, você foi enforcado!")
      print("A palavra era {}".format(palavra_secreta))
      print("    _______________         ")
      print("   /               \       ")
      print("  /                 \      ")
      print("//                   \/\  ")
      print("\|   XXXX     XXXX   | /   ")
      print(" |   XXXX     XXXX   |/     ")
      print(" |   XXX       XXX   |      ")
      print(" |                   |      ")
      print(" \__      XXX      __/     ")
      print("   |\     XXX     /|       ")
      print("   | |           | |        ")
      print("   | I I I I I I I |        ")
      print("   |  I I I I I I  |        ")
      print("   \_             _/       ")
      print("     \_         _/         ")
      print("       \_______/           ")


# Desenha a forca a cada erro
def desenha_forca(erros):
      print("  _______     ")
      print(" |/      |    ")

      if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

      if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

      if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

      if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

      if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

      if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

      if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

      print(" |            ")
      print("_|___         ")
      print()

# permite que este código seja executado independete de outro principal (jogos.py)
if (__name__ == "__main__"):
      jogar()
