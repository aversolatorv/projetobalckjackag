import random

q=10
j=10
k=10
a=11

baralho=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k]*4
mj=[] #mão jogador
mc=[] #mão croupier
d=1000

m="carta"
print("♠♥♣♦ Bem-vindo à mesa de Blackjack! ♠♥♣♦")
while d!=0:
    mj.clear()
    mc.clear()
    print("Você tem R$ ", d)
    a=int(input('Aposte um valor inteiro: '))
    if a>d:
        print("Não aposte mais dinheiro do que tem!")
        print("Você foi penalizado em: ", 0.1*d, "por tentar trapacear!")
        d=d-(0.1*d)
        continue
    cj1=random.choice(baralho) #cj = carta do jogador
    cj2=random.choice(baralho)
    mj.append(cj1)
    mj.append(cj2)
    if sum(mj)>21:
        a=1
    if sum(mj)>21:
        print("Você estorou", "com as cartas", mj, "!")
        d=d-a
        continue
    if sum(mj)==21:
        d=d+((1.5)*a)
        print("Parabéns, você ganhou um Blackjack ", "com as cartas", mj, "!")
        continue
    print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
    m=input("Responda com 'continuar' ou 'carta': ")
    if m=="continuar":
        while m!= "continuar":
            m=input("Responda com 'continuar' ou 'carta': ")
            mj.append(random.choice(baralho))
            if sum(mj)>21:
                a=1
            if sum(mj)>21:
                print("Você estorou", "com as cartas", mj, "!")
                d=d-a
                continue
            elif sum(mj)==21:
                d=d+((1.5)*a)
                print("Parabéns, você ganhou um Blackjack!")
                continue
            print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
    cc1=random.choice(baralho) #cc = carta do croupier
    cc2=random.choice(baralho)
    mc.append(cc1)
    mc.append(cc2)
    print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    if sum(mc)>sum(mj):
        d=d-a
        print("Você perdeu.")
        continue
    elif sum(mj)>sum(mc):
        d=d+a
        print("Você ganhou!")
        continue
        
    
