import os
os.system('cls')

import time

brancovermelho = ('\033[1;30;41m')
branco = ("\033[1;97m")
roxo = ("\033[1;34m")
remove = ("\033[0;0m")

evilpoint = 0
goodpoint = 0
#////////////////////////////////////////////////////////////////////////////////////////////////////

print("Bem vindo ao escritório do inferno, desculpe não estou te reconhecendo.")
name = input("Deixe me conferir na lista, qual o seu nome?\n").upper()


if name == "HITLER":
    print(f"AH você demorou para chegar, entre no fogo mais quente do inferno.")
    exit()

if name == "STALIN":
    print(f"AH você demorou para chegar, entre no fogo mais quente do inferno.")
    exit()

if name == "LUCIFER":
    print(f"Ah você é o filho renegado de Deus, senhor da escuridão, pode entrar meu lorde.")
    exit()

if name == "JESUS":
    print(f"Ah você é o filho de Deus, o salvador, por favor suba para o sétimo céu e diga um olá para o criador.")
    exit()





print("Muito bem, deixe me verificar a planilha do inferno.")
time.sleep(4)

print(f"\033[1;97mEstranho, não encontro seu nome {name}.")
time.sleep(4)

print(f"Bom {name}, terei que fazer algumas perguntas para saber exatamente onde você se encaixa.")

time.sleep(4)

# Perguntas
# 1//////////////////////////////////////////////////////////////////////////
print("Primeira pergunta!")
time.sleep(2)
print(f"{brancovermelho}  Se estivesse andando no shopping, e uma velha tomando sorvete tropeçasse, e derrubasse a casquinha na cabeça de uma criança, você diria que essa situação é engraçada ou não?{remove}")
print(f"{branco}-1 SIM\n-2 NÃO{remove}")
quest = int(input(f"{roxo}Digite o número da alternativa:{remove}\n"))

if quest == 1:
    evilpoint += 1

if quest == 2:
    goodpoint += 1


# 2///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você mexe no celular enquanto o garçom pergunta o que vai beber?{remove}")
print(f"{branco}-1 SIM\n-2 NÃO{remove}")
quest2 = int(input(f"{roxo}Digite o número da alternativa:{remove}\n"))

if quest2 == 1:
    evilpoint += 1
if quest2 == 2:
    goodpoint += 1




# 3///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você coloca potes vazios de volta na geladeira?{remove}")
print(f"{branco}-1 SIM\n-2 NÃO{remove}")
quest3 = int(input(f"{roxo}Digite o número da alternativa:{remove}\n"))

if quest3 == 1:
    evilpoint += 1
if quest3 == 2:
    goodpoint += 1





# 4///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}E forminha de gelo vazia, você coloca de volta no frezeer?{remove}")
print(f"{branco}-1 SIM\n-2 NÃO{remove}")
quest4 = int(input(f"{roxo}Digite o número da alternativa:{remove}\n"))

if quest4 == 1:
    evilpoint += 1
if quest4 == 2:
    goodpoint += 1





# 5///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você avisa alguém que está com o zíper aberto?{remove}")
print(f"{branco}-1 Sim!\n-2 Não, o que eu tenho a ver com ele?{remove}")
quest5 = int(input(f"{roxo}Digite o numero da alternativa:{remove}\n"))

if quest5 == 1:
    goodpoint += 1

if quest5 == 2:
    evilpoint += 1

# 6///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você tenta paga com moedas quando tem?{remove}")
print(f"{branco}-1 Não, preguiça de contar. Dou logo uma nota\n-2 Sim, me livro das moedas e já ajudo no troco{remove}")
quest6 = int(input(f"{roxo}Digite o numero da alternativa:{remove}\n"))

if quest6 == 1:
    evilpoint += 1
if quest6 == 2:
    goodpoint += 1

#7///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você marca (vou) e depois não vai em evento no qual a pessoa fez comida?{remove}")
print(f"{branco}-1 Sei lá, acho que marco\n-2 procuro não fazer isso{remove}")
quest7 = int(input(f"{roxo}Digite o numero da alternativa{remove}\n"))

if quest7 == 1:
    evilpoint += 1
if quest7 == 2:
    goodpoint += 1


#8///////////////////////////////////////////////////////////////////////
print(f"{brancovermelho}Você para na porta do transporte se não vai descer na próxima parada?{remove}")
print(f"{branco}-1 Paro, melhor prevenir\n-2 Não, vou pro corredor{remove}")
quest8 = int(input(f"{roxo}Digite o numero da alternativa{remove}\n"))

if quest8 == 1:
    evilpoint += 1
if quest8 == 2:
    goodpoint += 1

#9///////////////////////////////////////////////////////////////////////

print(f"{brancovermelho}Você faz chifrinho na foto dos amigos sempre que possível?{remove}")
print(f"{branco}-1 Sempre kkkk\n-2 Claro que não{remove}")
quest9 = int(input(f"{roxo}Digite o numero da alternativa{remove}\n"))

if quest9 == 1:
    evilpoint += 1
if quest9 == 2:
    goodpoint += 1
#10///////////////////////////////////////////////////////////////////////

print(f"{brancovermelho}Você usa a expressão roubartilhar??{remove}")
print(f"{branco}-1 Sim\n-2 Não{remove}")
quest10 = int(input(f"{roxo}Digite o numero da alternativa{remove}\n"))

if quest10 == 1:
    evilpoint += 1
if quest10 == 2:
    goodpoint += 1
#11///////////////////////////////////////////////////////////////////////

print(f"{brancovermelho}Você dá opinião fortíssima sobre coisas que nem leu direito?{remove}")
print(f"{branco}-1 Sim\n-2 Não{remove}")
quest11 = input(f"{roxo}Digite o numero da alternativa{remove}\n")

if quest11 == 1:
    evilpoint += 1
if quest11 == 2:
    goodpoint += 1


# PLACAR///////////////////////////////////////////////////////////////////////
print("Deixe me calcular sua prova")
time.sleep(5)
print("Hmmm.")
time.sleep(3)


print("*"*80)
print(f"\033[1;92mPontos de bondade {goodpoint}\033[0;0m")
print(f"\033[1;31mPontos de maldade {evilpoint}\033[0;0m")

#Céu
if goodpoint >= 6:
    print(f"É {name} você está no lugar errado, você merece o céu, pode subir!")
if goodpoint >=10:
    print(f"Em nome de Zeus, você é perfeito, não há maldade em você, seja recebido pelas trombetas do céu e será cantado {name}.")


#Inferno
if evilpoint >= 6:
    print(f"É {name} voce está no lugar correto, você tem potencial para o inferno.")
if evilpoint >= 10:
    print(f"Eu não posso acreditar, o escolhido, só existe maldade em você, as guitarras irão soar por mil anos em seu nome {name}!")
