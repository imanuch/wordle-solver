import os
g = open("listes mots anglais 5 lettres.txt",'r')
#g = open("C:/Users/emmanuel cardot/python vrmt cools/listes mots français sans accents.txt",'r')


mots = []
taille = 5
for mot in g:
    if len(mot)==taille+1:

        mots.append(mot)

def exa(mot,lettres,lps,alph):
    for i in range(taille):
        if (mot[i]!=lettres[i] and lettres[i]!='0') or mot[i]==lps[i] or (mot.count(lps[i])<(lps.count(lps[i])+lettres.count(lps[i])) and lps[i]!='0') or (mot[i] in alph and mot[i] not in lettres and mot[i] not in lps):

            return False
    return True

def rechercher(mot,k):
    lettres = ''
    lps = ''
    alph = ''
    for i in range(taille):

        if k[i]=='2':
            lettres+=mot[i]
            lps+='0'
        elif k[i]=='1':
            lps+=mot[i]
            lettres+='0'
        else:
            alph+=mot[i]
            lettres+='0'
            lps+='0'
    return lettres,lps,alph

def elim(mots,k,mot):
    mots2 = []
    for i in range(len(mots)):
        tmp = rechercher(mot,k)
        if exa(mots[i],tmp[0],tmp[1],tmp[2]):
            mots2.append(mots[i])
    print('ok')
    return mots2


def interaction(mot):
    k = ''
    print(mot)

    k+=input()
    return k
#ramat


#mot = 'abide'
#mot = 'tentacule'
mot = 'amies'
k = interaction(mot)
while k!='2'*taille:

    print(len(mots))
    mots = elim(mots,k,mot)
    print(mots)
    print(len(mots))
    mot = mots[0]
    k = interaction(mot)

print('c est validé')