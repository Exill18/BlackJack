#this is a BlakcJack game made in python, console only.
import random

def main():
    #inicializa as variaveis
    dealer = 0
    jogador = 0
    #inicializa as listas
    cartas = []
    cartasDealer = []
    cartasJogador = []
    #cria as cartas
    for i in range(1, 11):
        cartas.append(i)
    #cria as cartas do dealer
    for i in range(2):
        cartasDealer.append(random.choice(cartas))
    #cria as cartas do jogador
    for i in range(2):
        cartasJogador.append(random.choice(cartas))
    #conta as cartas do dealer
    for i in cartasDealer:
        dealer += i
    #conta as cartas do jogador
    for i in cartasJogador:
        jogador += i
    #mostra as cartas do dealer
    print("Cartas do dealer: ", cartasDealer)
    #mostra as cartas do jogador
    print("Cartas do jogador: ", cartasJogador)
    #mostra a soma das cartas do dealer
    print("Soma das cartas do dealer: ", dealer)
    #mostra a soma das cartas do jogador
    print("Soma das cartas do jogador: ", jogador)

    if dealer == 21:
        print("O dealer ganhou, com BlackJack!")
    elif jogador == 21:
        print("O jogador ganhou, com BlackJack!")

    if dealer < 21 and jogador < 21:
        #pergunta se o jogador quer mais uma carta
        resposta = input("Deseja mais uma carta? (s/n): ")
        #se o jogador quiser mais uma carta
        while resposta == "s":
            #cria mais uma carta para o jogador
            cartasJogador.append(random.choice(cartas))
            #conta as cartas do jogador
            jogador = 0
            for i in cartasJogador:
                jogador += i
            #mostra as cartas do jogador
            print("Cartas do jogador: ", cartasJogador)
            #mostra a soma das cartas do jogador
            print("Soma das cartas do jogador: ", jogador)
            #se o jogador passar de 21
            if jogador > 21:
                print("O dealer ganhou!")
                break
            #se o jogador tiver 21
            elif jogador == 21:
                print("O jogador ganhou, com BlackJack!")
                break
            #pergunta se o jogador quer mais uma carta
            resposta = input("Deseja mais uma carta? (s/n): ")
        #se o jogador nao quiser mais uma carta
        else:
            #cria mais uma carta para o dealer
            while dealer < 17:
                cartasDealer.append(random.choice(cartas))
            #conta as cartas do dealer
                dealer = 0
                for i in cartasDealer:
                    dealer += i
            #mostra as cartas do dealer
            print("Cartas do dealer: ", cartasDealer)
            #mostra a soma das cartas do dealer
            print("Soma das cartas do dealer: ", dealer)
            #se o dealer passar de 21
            if dealer > 21:
                print("O jogador ganhou!")
            #se o dealer tiver 21
            elif dealer == 21:
                print("O dealer ganhou, com BlackJack!")
            #se o dealer tiver menos de 21
            else:
                #verifica quem ganhou
                if dealer > jogador:
                    print("O dealer ganhou!")
                elif jogador > dealer:
                    print("O jogador ganhou!")
                else:
                    print("Empate!")

main()

