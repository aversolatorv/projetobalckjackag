'''
Andre Versolatto - andrerv@al.insper.edu.br
Gabriel Tkacz - gabrielmt2@al.insper.edu.br
1A
2019/2
'''
import random
import os

q=10 #figuradas valem 10
j=10
k=10
A=11 #ás vale 11 se uma mão não estourar
baralho=[A, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k]*4 #um baralho tem 4 conjuntos desses
letras=['A','J','Q','K']
letrasv=[11,10,10,10]
mj=[] #mão jogador
ms=[] #mao split
mc=[] #mão croupier
ls=["Sim","sim","s","S"] #lista com variacoes de sim
ln=["Não","não","nao","Nao","n","N"] #lista com variacoes de nao
lcar=["carta", "cartas", "car", "Carta", "Cartas", "Car", "c","C"] #lista com variacoes de carta
lcon=["continuar", "con", "Continuar", "Con","s","S"] #lista com variacoes de continuar
lfun=["funcionamento","Funcionamento","fun","Fun","regra","Regra","regras","Regras","reg","Reg",] #lista com variacoes de funcionamento
d=1000 #dinheiro
ldes=["desisto","fim"]
m="carta" #para entrar no loop
abc="n" #para entrar no loop
limpa = lambda: os.system('cls') #para limpar console
ayuda="Inicialmente, você apostará um valor. Após isso, você receberá duas cartas. Estas cartas terão um valor somado; se tal soma passar de 21, você estourou e perdeu. (Cartas numéricas valem seu próprio número, cartas figuradas valem 10, e o Ás vale 11. Entretanto, se sua mão valer mais de 21, mas você tem um Ás, o Ás passa a valer 1). Ganha quem tiver o número mais alto perto de 21, sem ultrapassa-lo. Se suas cartas iniciais tiverem um valor baixo, você pode pedir mais cartas quanto quiser." #texto para iniciantes
def funcionamento():
    print("Regras e funcionamento adicionais:")
    print("1: Não aposte mais dinheiro do que tem!")
    print("2: Aposte valores inteiros!")
    print("3: Se suas cartas iniciais somarem 21 pontos, você automaticamente ganha 1,5x o que apostou.")
    print("4: Se você ganhar/perder de outra forma você ganha/perde exatamente o que apostou.")
    print("5: Se você inicialmente ganhar duas cartas iguais, terá direito a jogar um split (separar as duas cartas e jogar jogo simultâneos)")
    print("6: Enquanto a mão do croupier for menor que a sua, ele vai puxar cartas até atingir no mínimo 17 pontos.")
    print("7: Se quiser lembrar como jogar Blackjack, digite 'ajuda'")
    print("8: Se quiser lembrar as regras do nosso Blackjack, digite 'funcionamento' ou 'regras'")
    print("9: Se quiser lembrar com quantos baralhos está jogando, digite 'baralho(s)'")
    print("10: Se quiser que o jogo pare, digite 'desisto' ou 'fim'.")
    print("Se divirta!")

print("♠ ♥ ♣ ♦ Bem-vindo à mesa de Blackjack do Cassino Insper! ♦ ♣ ♥ ♠")
perg=input("Você sabe jogar Blackjack? ")
while perg in ln:
    print("Sem problemas!")
    print(ayuda)
    abc=input("Entendeu? ")
    if abc in ls:
        limpa()
        break
    else:
        continue
    
funcionamento()
print(" ")

q=0 #para entrar no loop
inp="s" #para entrar no loop
while q<1 or q>10 or inp in ln:
    inp='s'
    des=input("Com quantos baralhos quer jogar? ")
    if des in ldes:
        d=0
        break
    q=int(des)
    if q>10:
        print("O máximo são 10 baralhos!")
        continue
    elif q<1:
        print("Você não digitou um valor válido.")
        continue
    elif q>3:
        inp=input("O jogo funciona optimamente com menos baralhos, tem certeza de que quer continuar? ")
    if inp in ln:
        continue
    elif inp in ls:
        break  

baralho=baralho*q #multiplos baralhos
while d>0:
    mj.clear()
    ms.clear()
    mc.clear()
    print("Você tem: R$", d)
    b=(input('Aposte um valor inteiro: '))
    if b=="ajuda" or b=="Ajuda":
        print(ayuda)
        continue
    if b=="baralho" or b=="baralhos" or b=="Baralho" or b=="Baralhos":
        print("Você está jogando com", q, "baralho(s).")
        continue
    if b in ldes:
        limpa()
        print("Que pena!")
        break
    if b in lfun:
        funcionamento()
        continue
    a=int(b)
    if a<1:
      print("Você apostou um valor inválido!")
      continue
    if a>d:
        print("Não aposte mais dinheiro do que tem!")
        print("Você foi penalizado em: R$", 0.1*d, "por tentar trapacear!")
        d=d-(0.1*d)
        continue
    mj.append(random.choice(baralho))
    mj.append(random.choice(baralho))
    if mj[0]==mj[1]:
        print("Você recebeu duas cartas", mj[0], ", gostaria de jogar um split?")
        resposta=input()
        if resposta in ls:
            ms.append(mj[1])
            mj.remove(mj[1])
            ms.append(random.choice(baralho))
            mj.append(random.choice(baralho))
            if sum(ms)>21 and A in ms:
                subst=ms.index(A)
                ms[subst]=1
            if sum(ms)>21:
                print("Você estourou seu split com as cartas", ms, "!")
                d=d-a
            if sum(ms)==21:
                d=d+((1.5)*a)
                print("Parabéns, você ganhou seu split com um Blackjack com as cartas", ms, "!")
            print("No seu split, você tem as cartas: ", ms, "totalizando: ", sum(ms), ", você gostaria de mais uma carta ou quer continuar?")
            ms=input("Responda com 'continuar' ou 'carta': ")
            while ms not in lcon:
                ms.append(random.choice(baralho))
                if sum(ms)>21 and A in ms:
                  subst=ms.index(A)
                  ms[subst]=1
                if sum(ms)>21:
                    print("Você estourou seu split com as cartas", ms, "totalizando:", sum(ms), "!")
                    d=d-a
                    break
                elif sum(ms)==21:
                    d=d+((1.5)*a)
                    print("Parabéns, você ganhou seu split com um Blackjack com as cartas", ms, "!")
                    break
                print("Você tem as cartas: ", ms, "no seu split, totalizando: ", sum(ms), ", você gostaria de mais uma carta ou quer continuar?")
                m=input("Responda com 'continuar' ou 'carta': ")
    if sum(mj)>21 and A in mj:
        subs=mj.index(A)
        mj[subs]=1
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
    if m in lcar:
        while m not in lcon:
            mj.append(random.choice(baralho))
            if sum(mj)>21 and A in mj:
              subs=mj.index(A)
              mj[subs]=1
            if sum(mj)>21:
                print("Você estourou com as cartas", mj, "totalizando:", sum(mj), "!")
                d=d-a
                break
            elif sum(mj)==21:
                d=d+((1.5)*a)
                print("Parabéns, você ganhou um Blackjack com as cartas", mj, "!")
                break
            print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
            m=input("Responda com 'continuar' ou 'carta': ")
    if sum(mj)>21:
      continue
    if sum(mj)==21:
      continue
    mc.append(random.choice(baralho))
    mc.append(random.choice(baralho))
    print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    while sum(mc)<17 and (sum(mc)<sum(mj) or sum(mc)<sum(ms)):
        mc.append(random.choice(baralho))
        print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    if sum(mc)>21 and A in mc:
        subs=mc.index(A)
        mc[subs]=1
    if sum(mc)>21:
        print("O croupier estourou!")
        d=d+a
        print("Você ganhou!")
        continue
    if len(ms)>0:
        if sum(mc)>sum(ms):
            d=d-a
            print("Você perdeu seu split.")
            continue
        if sum(mj)>sum(ms):
            d=d+a
            print("Você ganhou seu split!")
            continue
        if sum(mj)==sum(ms):
            print("Seu split é um empate!")
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
if d==0 and des not in ldes:
    print("Seu dinheiro acabou!")
print("Obrigado por jogar nosso jogo!")
print("Volte sempre!")
