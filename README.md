# Seance-Python-Pygame

## Introduction

Ce projet est un sujet de TP pour le cours de Python en Pygame. Il est destiné aux étudiants débutants en Python et en programmation orientée objet.

## Prérequis

Pour pouvoir utiliser ce projet, il faut avoir installé Python 3.7 ou supérieur. Il faut également utiliser Pip pour installer les dépendances en utilisant la commande suivante :

```bash
pip install -r requirements.txt
```

## Objectif

L'objectif de ce TP est de créer un jeu d'ésquive en utilisant le module Pygame. Le jeu doit être composé d'un vaisseau qui peut se déplacer sur l'écran et qui doit rester le plus longtemps possible sur un chemin. Ce chemin est composé de cases qui se déplacent de haut en bas de l'écran. Si le vaisseau sort du chemin, le joueur perd la partie.

> **Note** : Une proposition de solution est disponible dans le dossier `Solution`.

## Étapes

### Étape 1 : Création du template Pygame

Pour cette étape, nous nous baserons sur le tutoriel suivant : [Getting started with Pygame](https://riptutorial.com/pygame).

La première étape consiste à créer le main Pygame. Pour cela, il faut créer un fichier `main.py`, voici le template de base :

```python
# import module pygame
import pygame

# initialise pygame
pygame.init()

# set game clock
clock = pygame.time.Clock()
FPS = 30

# screen dimensions
screen_width = 900
screen_height = 600

# set screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame')

# run the main loop
run = True
while run:
    
    # if we click on the quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # refresh the screen
    clock.tick(FPS)
    pygame.display.update()

# quit pygame
pygame.quit()
```

### Étape 2 : Création du vaisseau

Pour cette étape, nous allons créer la classe `Ship` qui représente le vaisseau.
Pour cela vous devez définir **une taille pour une cellule** afin de quadriller l'écran, nous utiliserons cette mesure pour définir la taille du vaisseau.

Cette classe doit contenir les attributs suivants :
- `image` : qui représente le rectangle du vaisseau avec _pygame.Surface_
- `rect` : qui représente la position du vaisseau sur l'écran
- `velocity` : qui représente la vitesse de déplacement du vaisseau avec une liste de deux valeurs [x, y]

Il faudra aussi une fonction `update` qui permet de mettre à jour la position du vaisseau en fonction de la vitesse de déplacement.

Voici le squelette de la classe `Ship` :

```python
class Ship:
    def __init__(self, x, y, cell_size):
        # set image
        self.image = pygame.Surface(# ...
        self.image.fill(# ...
        self.rect = self.image.get_rect(#...
        self.velocity = # ...

    def update(self):
        self.rect.move_ip(*self.velocity)
        # ...
```

> **Note** : Vous pouvez créer des variables globales pour la taille des cellules ainsi que les couleurs du jeu (`BLACK = (0, 0, 0)`).

N'oublier pas de créer une instance de la classe `Ship`.

### Étape 3 : Création du chemin




