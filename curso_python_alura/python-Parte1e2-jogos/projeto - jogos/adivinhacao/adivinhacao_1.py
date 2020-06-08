print ("****************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("****************************************")

numero_secreto = 42

# permitir que o usuário informe um valor. Tudo o que é digita no imput é recebido como string,
# #logo precisa ser convertido para inteiro para ser comparado com o numero_sercreto
chute_str = input("Digite seu número: ")

print("Você digitou: ", chute_str)   

chute = int(chute_str)

# verificar se o chute é igual ao número secreto
if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")