from random import *

def main():
    premio = ['1', '2', '3']

    sair = 1

    i = int(0)

    qtd_jogadores = int(input("Quantos jogadores irão participar? "))

    
    jogador = []
    contador = []

    for x in range(qtd_jogadores):
            nome_jogadores = str(input("\nQual o nome do jogador {}? ".format(x+1)))
            jogador.append(nome_jogadores)
            contador.append(int(0))

    while sair != 0:

        embaralhar = randrange(0, len(premio))
        resultado = int(embaralhar+1)
    
        vez_de = jogador[i]
        print("\nAgora é a vez de '{}' jogar\n".format(vez_de))
      
        entrada = int(input('Onde está o bagulho? '))

        if entrada == resultado:

            print("Você achou o bagulho!!!\n")

            pontuação = int(contador[i])
            nova_pontuação = pontuação+1
            contador[i] = nova_pontuação

            print("PLACAR:\n\n")
            for x in range(qtd_jogadores):
                print("{} : {} acertos".format(jogador[x], contador[x]))

            i = i+1

            if i == qtd_jogadores:
                i = 0
            
            '''if i == 0:
                cont0 = cont0+1
            if i == 1:
                cont1 = cont1+1
            if i == 2:
                cont2 = cont2+1

            if i == 0:
                i = 1
            elif i == 1:
                i = 2
            else:
                i = 0'''

        elif entrada > 3:
            print ("\nCara... Só existem 3 locais para procurar o bagulho...")
            print("Perdeu a sua vez... Namoral.. Digite um valor razoavel da próxima vez")
            
            i = i+1

            if i == qtd_jogadores:
                i = 0

        else:
            print("O Prêmio estava na posição '{}'".format(resultado))
            print("Tente novamente...\n")

            '''if i == 0:
                i = 1
            elif i == 1:
                i = 2
            else:
                i = 0'''

            i = i+1

            if i == qtd_jogadores:
                i = 0

main()


