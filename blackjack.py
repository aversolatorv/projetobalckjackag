import random

q=10
j=10
k=10
a=11

baralho=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k]*4

d=1000

m="carta"
while d!=0:
    print("Você tem R$ ", d)
    a=int(input('Aposte um valor: '))
    cj1=random.choice(baralho) #cj = carta do jogador
    cj2=random.choice(baralho)
    if cj1+cj2>21:
        a=1
    if cj1+cj2>21:
        print("Você estorou!")
        d=d-a
        continue
    if cj1+cj2==21:
        d=d+((1.5)*a)
        print("Parabéns, você ganhou um Blackjack ", "com as cartas", cj1, cj2, "!")
        continue
    print("Você tem as cartas: ", cj1, "e", cj2, "totalizando: ", cj1+cj2, ", você gostaria de mais uma carta ou quer continuar?")
    while m!= "continuar":
        m=input("Responda com continuar ou carta: ")
        cj3=random.choice(baralho)
        if cj1+cj2>21:
            a=1
        if cj1+cj2+cj3>21:
            print("Você estorou!")
        elif cj1+cj2+cj3==21:
            d=d+((1.5)*a)
            print("Parabéns, você ganhou um Blackjack!")
        break
        print("Você tem as cartas: ", cj1, cj2, "e", cj3, "totalizando: ", cj1+cj2+cj3, ", você gostaria de mais uma carta ou quer continuar?")
    cc1=random.choice(baralho) #cc = carta do croupier
    cc2=random.choice(baralho)
    print("O croupier tem as cartas: ", cc1, "e", cc2, "totalizando: ", cc1+cc2)
    if cc1+cc2>cj1+cj2:
        d=d-a
        print("Vc perdeu.")
        continue
    else:
        d=d+a
        print("Vc ganhou!")
        continue
    