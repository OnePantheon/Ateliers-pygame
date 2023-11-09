# Les bibliothèques en python

import math

math.pi # 3.14
math.e # 2.71

math.ceil(2.1) # arrondi supérieur 3
math.floor(2.9) # arrondi inférieur 2
math.factorial(3) # 1*2*3 = 6
math.gcd(12, 18) # pgcd 6

math.sqrt(2) # 1.41
math.exp(1) # 2.71
math.log(1) # 0
math.log10(10) # 1

math.sin(math.pi/2) # 1
math.cos(math.pi) # -1
math.tan(math.pi/4) # 1

math.dist([0,0], [1,1]) # distance euclidienne 1.41

import numpy as np

np.array([1,2,3]) # liste array([1, 2, 3])
np.zeros(3) # array([0, 0, 0])
np.ones(3) # array([1, 1, 1])
np.full(3, 5) # array([5, 5, 5])
np.arange(3) # array([0, 1, 2])
np.linspace(10, 50, 10) # array([ 10. , 20. , 30. , 40. , 50. ])

np.identity(3) # array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])

np.min([1,2,3]) # 1
np.max([1,2,3]) # 3
np.mean([1,2,3]) # 2

np.sort([3,2,1]) # array([1, 2, 3])
np.sort([3,2,1])[::-1] # array([3, 2, 1])
np.squeeze([[0], [1], [2]]) # array([0, 1, 2])

import time

time.time() # secondes depuis 1970
time.ctime() # 'Tue Jun  1 10:00:00 2021'

import random

random.random() # nombre aléatoire entre 0 et 1
random.randint(1, 10) # nombre aléatoire entre 1 et 10
random.choice([1,2,3]) # choix aléatoire dans la liste

import matplotlib.pyplot as plt

plt.plot([1,2,3], [1,2,3]) # affiche le graphique
plt.ylabel('axe des y') # ajoute un titre à l'axe des y
plt.xlabel('axe des x') # ajoute un titre à l'axe des x
plt.axis([0, 4, 0, 4]) # définit les bornes des axes
plt.show() # affiche le graphique

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3)) # taille du graphique (combien de plots)

plt.subplot(131) # 1 ligne, 3 colonnes, 1er plot
plt.bar(names, values) # graphique en barres
plt.subplot(132)
plt.scatter(names, values) # graphique en points
plt.subplot(133)
plt.plot(names, values) # graphique en courbes
plt.suptitle('Categorical Plotting') # titre du graphique
plt.show()

