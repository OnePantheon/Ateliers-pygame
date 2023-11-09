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

La première étape consiste à créer le main Pygame. Pour cela, il faut créer un fichier `main.py`, voici le template de base pour ce projet :

```python
# import module pygame
import pygame
import random

# initialise pygame
pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

# set game clock
clock = pygame.time.Clock()
FPS = 30

#Color definition

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

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

Il est temps de créer le vaisseau. Nous voulons ici une entitée de 3 "cellule" de long.
Pour cette étape, on créera une fonction player.

```python
cell_size = 16
# Player creation
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Donne une forme T-shape renversé au joueur
        self.image = pygame.Surface((cell_size * 3, cell_size))
        self.image.fill(WHITE)
        # on place le joueur au milieu de l'écran en bas
        self.rect = self.image.get_rect(center=(screen.get_width() / 2, screen.get_height() - cell_size/2))
        self.velocity = [0, 0]

    def update(self):
        self.rect.move_ip(*self.velocity)
        self.velocity = [0, 0]

player = Player()
```

N'oublez surtout pas d'assigner le joueur une variable ! 

### Étape 3 : Création du chemin

Notre vaisseau doit suivre un chemin. Pour ce faire, on définie les variables x et y pour avoir: 
    . La coordonnée du centre de l'écran pour x
    . La bordure basse pour y. Soit : y = 0

```python
path = []
# Path
x, y = (screen.get_width() / 2) - (cell_size * 3.5), 0
while y < screen.get_height():
    path.append([int(x), y])
    x += cell_size
    if x >= (screen.get_width() / 2) + (cell_size * 3.5):
        x = (screen.get_width() / 2) - (cell_size * 3.5)
        y += cell_size
```

### Étape 4 : Mise a jour du chemin

Pour le moment, vous devriez avoir une fenêtre noir avec un chemin. Maintenant, il est temps de lui donner vie. 

On utilisera random pour cela (importer en début de template).

```python
def updatePath(): # Moving the path, we add a line at the beginning and advance the following lines down, removing the last one
    global path
    # Shift down
    for cell in path:
        cell[1] += cell_size
        if cell[1] >= screen.get_height(): # Deleting the last line
            path.remove(cell)
    # Adding a line at the beginning
    x = random.randint(-1,1)
    new_line = [path[0][0] + (x * cell_size), 0]
    path.insert(0, new_line)
    for i in range(6):
        path.insert(i+1,[new_line[0] + ((1+i) * cell_size), 0])
```

### Étape 5 : Gestion des collisions

Maintenant, il est temps de rentrer dans le while. 
