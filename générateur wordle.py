import os
g = open("C:/Users/emmanuel cardot/Desktop/python vrmt cools/listes mots anglais 5 lettres.txt",'r')
from random import randint

mots = []

for mot in g:
    mots.append(mot)

motatr = mots[randint(0,len(mots)-1)]
print(motatr)


def un(mot1,mot2,i):
    k = 0
    for j in range(5-i):
        if mot2[j]==mot[i]:
            k+=1
    return k


def inserer(mot,i,car):
    if i!=len(mot):
        mot=mot[0:i]+car+mot[i+1:5]
    else:
        mot=mot[0:i]+car
    return mot

def supprimer(mot,i):
    mot = mot[0:i] + mot[i+1:]
    return mot

def entree(motatr):
    motent = input('mot: ')
    motent2 = motent
    motatr2 = motatr
    motatr3 = motatr
    k = ''
    for i in range(5):
        if motent[i]==motatr[i]:
            k += '2'
            motent2 = inserer(motent2,i,'0')
            motatr2 = inserer(motatr2,i,'0')
            motatr3 = supprimer(motatr3,i)
        else:
            k+='0'
    for i in range(5):
        for j in range(5):
            if motent2[i]==motatr2[j] and motent2[i]!='0' and motatr2[j] in motatr3:
                motatr3 = supprimer(motatr3,motent2.index(motent2)+1)
                motent2 = inserer(motent2,i,'0')
                k=inserer(k,i,'1')


    return k



k = entree(motatr)
print("    ",k)
while k!='22222':
    k = entree(motatr)
    print("    "+k)

