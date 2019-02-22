from random import randint
import time, os
from termcolor import cprint
from yeelight import *

#Declarando lampada
bulb = Bulb("192.168.1.10", effect="smooth")
bulb.turn_on()

#Funcao Cores Lampada
def luz_vermelho():
    bulb.set_rgb(255,0,0)
    time.sleep(1)
def luz_azul():
    bulb.set_rgb(0,0,255)
    time.sleep(1)
def luz_verde():
    bulb.set_rgb(0,255,0)
    time.sleep(1)
def luz_amarelo():
    bulb.set_rgb(255,255,0)
    time.sleep(1)
def luz_branca():
    bulb.set_rgb(255,255,255)
    time.sleep(1)

#Variaveis de Ambiente
comecar_jogo = 0
contador = 0
nivel = 1
soma = []
resposta = []

def gerarCor():
    global contador
    #while (contador < 4):
    resultado_random = randint(1, 4)
    time.sleep(1)

    if resultado_random == 1:
        luz_vermelho()
        time.sleep(1)
    elif resultado_random == 2:
        luz_azul()
        time.sleep(1)
    elif resultado_random == 3:
        luz_verde()
        time.sleep(1)
    elif resultado_random == 4:
        luz_amarelo()
        time.sleep(1)

    else:
        print("Erro")
    soma.append(resultado_random)
    contador += 1

def exibeCor():
    for x in soma:
        if x == 1:
            cprint('Vermelho: 1', 'red')
        elif x == 2:
            cprint("Azul....: 2", 'blue')
        elif x == 3:
            cprint("Verde...: 3", 'green')
        elif x == 4:
            cprint("Amarelo.: 4", 'yellow')
        time.sleep(.5)

comecar_jogo = input("Deseja comecar o jogo? Digite 1 para comecar: ")
while comecar_jogo == 1:
    os.system("clear")
    if contador == 0:
        print("Comecando jogo...\n")
        gerarCor()
        time.sleep(1)

    print("\nAs cores foram:")

    for x in range(contador):
        #print("contador> "+str(contador))
        #print("x: " +str(x))
        #print("soma: " +str(soma))
        #print("resposta: " +str(resposta))


    #print(resposta)
    #print(soma)
        for z in range(len(soma)):
            #print("z" + str(z))
            resposta.append(input("Valor: "))
            if resposta[z] != soma[z]:
                print("\nIncorreto")
                nivel -= 1
                comecar_jogo = 0
                print("Fim de jogo.")
                exit()

        print("Correto! Proximo nivel...\n")
        nivel += 1
        exibeCor()
        gerarCor()
        del resposta [:]

    time.sleep(1)

#print ("\nResposta: " + str(resposta))
#print ("Vetor...: " + str(soma))
print("Voce chegou ao nivel: " + str(nivel+1))
print("\nObrigado por jogar!")
