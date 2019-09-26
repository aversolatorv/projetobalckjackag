import random

q=10 #figuradas valem 10
j=10
k=10
a=11 #ás vale 11 se uma mão não estourar
binicial=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k]*4 #um baralho tem 4 conjuntos desses
#bpaus=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k] ♣
#bcopas=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k] ♥
#bespadas=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k] ♠
#bouros=[a, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k] ♦
baralho=(binicial)
#baralho=bpaus+bcopas+bespadas+bouros
mj=[] #mão jogador
mc=[] #mão croupier
ls=["Sim","sim","s","S"] #lista com sim
ln=["Não","não","nao","Nao","n","N"] #lista com nao
d=1000 #dinheiro
m="carta" #para entrar no loop
ayuda="Inicialmente, você apostará um valor. Após isso, você receberá duas cartas. Estas cartas terão um valor somado; se tal soma passar de 21, você estourou e perdeu. (Cartas numéricas valem seu próprio número, cartas figuradas valem 10, e o Ás vale 11. Entretanto, se sua mão valer mais de 21, mas você tem um Ás, o Ás passa a valer 1). Ganha quem tiver o número mais alto perto de 21, sem ultrapassa-lo. Se suas cartas iniciais tiverem um valor baixo, você pode pedir mais cartas quanto quiser."
print("♠♥♣♦ Bem-vindo à mesa de Blackjack! ♠♥♣♦")
perg=input("Você sabe jogar Blackjack? ")
while perg in ln:
    print("Sem problemas!")
    print(ayuda)
    abc=input("Entendeu? ")
    if abc in ls:
        break
    else:
        continue
'''
if abc in ls:
  abcd=input("Você gostaria de jogar uma partida teste com tutorial?")
  if abcd in ln:
'''
print("Regras e funcionamento:")
print("1: Não aposte mais dinheiro do que tem!")
print("2: Aposte valores inteiros!")
print("3: Se suas cartas iniciais somarem 21 pontos, você automaticamente ganha 1,5x o que apostou.")
print("4: Se você ganhar/perder de outra forma você ganha/perde exatamente o que apostou.")
print("5: Enquanto a mão do croupier for menor que a sua, ele vai puxar cartas até atingir no mínimo 17 pontos.")
print("6: Para razões de desempate: ♣ > ♡ > ♠ > ♢") #Feature livre implementada por nós
print("7: Se quiser lembrar como jogar Blackjack, digite 'ajuda'")
print("8: Se quiser lembrar com quantos baralhos está jogando, digite 'baralho(s)'")
print("9: Se quiser que o jogo pare, digite 'desisto' ou 'fim'.")

print("Se divirta!")
q=0 #para entrar no loop
inp="s" #para entrar no loop
while q<1 or q>10 or inp=="Não" or inp=="não" or inp=="nao" or inp=="Nao" or inp=="n" or inp=="N":
    inp='s'
    q=int(input("Com quantos baralhos quer jogar? "))
    if q>10:
        print("O máximo são 10 baralhos!")
        continue
    elif q<1:
        print("Você não digitou um valor válido.")
        continue
    elif q>3:
        inp=input("O jogo pode ficar muito fácil, tem certeza de que quer continuar? ")
    if inp=="Não" or inp=="não" or inp=="nao" or inp=="Nao" or inp=="n" or inp=="N":
        continue
    elif inp=="Sim" or inp=="sim" or inp=="s" or inp=="S":
        break
#Utilizamos varias versoes de 'Sim' e 'Nao' para facilitar para o usuario    

baralho=baralho*q
#print(baralho)
while d!=0:
    mj.clear()
    mc.clear()
    print("Você tem: R$", d)
    b=(input('Aposte um valor inteiro: '))
    if b=="ajuda" or b=="Ajuda":
        print(ayuda)
        continue
    if b=="baralho" or b=="baralhos" or b=="Baralho" or b=="Baralhos":
        print("Você está jogando com", q, "baralho(s).")
        continue
    if b=="desisto" or b=="fim":
        print("Que pena!")
        break
    a=int(b)
    if a>d:
        print("Não aposte mais dinheiro do que tem!")
        print("Você foi penalizado em: R$", 0.1*d, "por tentar trapacear!")
        d=d-(0.1*d)
        continue
    mj.append(random.choice(baralho))
    mj.append(random.choice(baralho))
    if sum(mj)>21:
        a=1
    if sum(mj)>21:
        print("Você estourou com as cartas", mj, "!")
        d=d-a
        continue
    if sum(mj)==21:
        d=d+((1.5)*a)
        print("Parabéns, você ganhou um Blackjack com as cartas", mj, "!")
        continue
    print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
    m=input("Responda com 'continuar' ou 'carta': ")
    if m=="carta":
        while m!= "continuar":
            m=input("Responda com 'continuar' ou 'carta': ")
            mj.append(random.choice(baralho))
            if sum(mj)>21:
                a=1
            if sum(mj)>21:
                print("Você estourou com as cartas", mj, "totalizando:", sum(mj), "!")
                d=d-a
                break
            elif sum(mj)==21:
                d=d+((1.5)*a)
                print("Parabéns, você ganhou um Blackjack!")
                continue
            print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
    mc.append(random.choice(baralho))
    mc.append(random.choice(baralho))
    print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    while sum(mc)<17 and sum(mc)<sum(mj):
        mc.append(random.choice(baralho))
        print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    if sum(mc)>21:
        print("O croupier estourou!")
        d=d+a
        print("Você ganhou!")
        continue
    if sum(mc)>sum(mj):
        d=d-a
        print("Você perdeu.")
        continue
    elif sum(mj)>sum(mc):
        d=d+a
        print("Você ganhou!")
        continue
    elif sum(mj)==sum(mc):
        print("É um empate!")
        continue
if d==0:    
    print("Seu dinheiro acabou!")
print("Obrigado por jogar nosso jogo!")
print("Volte sempre!")
