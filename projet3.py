"""
File : projet3.py
File created on 07/11/2023
Created by Yanis El Kadiri
"""
#Exercice 1

def boucle_1(n):
    for i in range(n):
        for j in range(n):       
            if i == 0: #First loop
                print(j, " ", end='')
            else :
                val = (i+j) % n #Add the value of the two loop and take the rest of the modulo for switch
                print(val, " ", end='')

        print()

# Exercice 1.2

def boucle_2(n):
    for i in range(n):
        for j in range(n):       
            if i == 0: #First loop
                print(j, " ", end='')
            else :
                if j < i+1: # Add 0
                    print(0, " ", end='')
                else : 
                    print(j-i, " ",end='')#Adjustment of the value j with i

        print()



#Exercice 2.1

def present (list, x):
    if x in list: #Verfication
        return True
    else : 
        return False
    


#Exercice 2.2

def compte_sup (list,x):
    sup = []
    for i in list:
        if i >= x: #Validation
            sup.append(i)
    return sup

def compte_inf (list,x):
    inf = []
    for i in list:
        if i <= x:#Validation
            inf.append(i)
    return inf

#Exercice 2.3

def mediane(list):
    n = len(list)

    for i in range(len(list)): #Sorted the list
        k = list [i] # key value
        x = i - 1 #place in the list 
        while x >= 0 and k < list[x]: # Arrangement in ascending order
            list [x+1] = list [x] #Assignment of the value x to x+1
            x -=1
            list[x+1] = k # Assignment of the key value
    print (list)

    #Median

    if n%2 == 0:#Pair list
        midle1 = n // 2
        midle2 = midle1 -1
        return list[midle1] + list[midle2] / 2
    elif n == 1:#Only one element
        return list[n]
    else : #Other case
        return list[n // 2]
    
#Exercice 3.1

def echange(chain):
    #Init
    new = ""

    #Detection
    for caractere in chain: 
        if caractere == 'a':
            new += 'q'
        elif caractere == 'q':
            new += 'a'
        else:
            new += caractere
    return new

#Exercice 3.2

def corrige_dys(chain):
    #Init
    new = ""
    i = 0

    #Process
    while i < len(chain):
        if i < len(chain) - 1 and chain[i:i+2] == "ae": #ae Detection
            new += "ea"
            i += 2
        else: #Rest of the time
            new += chain[i]
            i += 1

    return new

#Exercice 3.3

def corrige_rep(chain):
    #Init
    new = ""
    i = 0

    #Process
    while i < len(chain):
        if i == 0 or chain[i] != chain[i-1]:#Single letter
            new += chain[i]
        else:
            count = 1
            while i < len(chain) - 1 and chain[i] == chain[i+1]:#Repetition
                i += 1
                count += 1
                if count <= 2:
                    new += chain[i]
        i += 1

    return new

#Exercice 4.1

def compte(chain,char):
    #Init
    count =0

    #Process
    for i in range(len(chain)):
        if chain[i] == char :
            count +=1 

    return count

#Exercice 4.2

def frequence(chain):
    #Init
    a = 0
    b = 0
    c = 0
    d = 0
    result = []

    #Process
    for i in range(len(chain)):
        if chain[i] == 'a':
            a += 1
        elif chain[i] == 'b':
            b += 1
        elif chain[i] == 'c':
            c += 1
        elif chain[i] == 'd':
            d += 1

    #Insert
    result.append("a{0}".format(a))
    result.append("b{0}".format(b))
    result.append("c{0}".format(c))
    result.append("d{0}".format(d))

    return result

#Exercice 5.1

import random

def genere_char(L):
    #Check that the sum of the elements of L is equal to 100
    if L[0] + L[1] + L[2] + L[3] != 100:
        return "La somme des éléments de la liste doit être égale à 100."
        
    
    #Generate a random number between 0 and 99
    n = random.randrange(100)

    #Determine character based on n and elements of L
    if n < L[0]:
        return 'a'
    elif n < L[0] + L[1]:
        return 'b'
    elif n < L[0] + L[1] + L[2]:
        return 'c'
    else:
        return 'd'


#Exercice 5.2

def genere(N, L):
    #Init
    total = N
    result = ""    
    
    #Check that the sum of the elements of L is equal to 100
    if N <= 0 or type(N) != int:
        return "N doit être un entier naturel positif."
    
    #Caracter chain 
    for i in range(N):
        total -= 1
        result += genere_char(L)
    
    return result
