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

    - La coordonnée du centre de l'écran pour x
    
    - La bordure haute pour y. Soit : y = 0

Voici une manière de procéder : 

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

### Étape 4 : Mise a jour du chemin et affichage

Pour le moment, vous devriez avoir une fenêtre noir avec un chemin. Maintenant, il est temps de lui donner vie. 

On utilisera random pour cela (n'oubliez pas de l'importer).

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

Dans la boucle, penssez bien a implémenter l'update via la condition if :

```python
if current_time - last_update_time >= update_interval:
        updatePath()
        last_update_time = current_time
        update_interval = update_interval * 0.99
```

On a également besoin du temps écouler (Plutôt utile pour l'update)

```python
clock = pygame.time.Clock()

#Dans la boucle

last_update_time = pygame.time.get_ticks() #Tout début

current_time = pygame.time.get_ticks()#Avant  l'update
```

Il est désormait temps de donner vie a notre chemin. Pour cela, utiliser la commande "pygame.draw.rect()" avec en paramètre :la résolution de l'écran, la couleur souhaiter (penssez bien a la definir), les coordonée des cellules qui sont : 

```bash
(cell[0], cell[1], cell_size, cell_size), 1
```

### Étape 5 : Les touches

Maintenant, il est temps de rentrer dans le while. Vous serez d'accord avec moi pour dire que sans touche appliqué ça va être complexe de jouer. 

Le principe est simple : 

On veut définir ce que fais chaque touche. On va prendre les flèches directionnels et le classique z q s d .

Il faut utiliser le module pygame.event.get() dans une boucle for. 

La template général est basique. Soit : 

    - Une condition if
    
    - utiliser la variable définie dans la boucle for
    
    - Utiliser, pygame.touche presser
    
    - Modification de la vélocité du joueur par player.velocity[1 ou 0] = Une cellule ou moins 1 cellule.

Voici un exemple de manière de procéder : 

```python
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                player.velocity[1] = -cell_size
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.velocity[1] = cell_size
            elif event.key == pygame.K_q or event.key == pygame.K_LEFT:
                player.velocity[0] = -cell_size
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.velocity[0] = cell_size

```

### Étape 6 : Gestion des collisions

On va créer les collisions nécéssaire au jeux.

Pour faire ça, c'est assez simple. On récupère les coordonées de chaque cellule du chemin. Avec ça, on s'assure que le vaisseau reste dessus. 

```python
collision = 0
    for cell in path:
        if player.rect.colliderect(pygame.Rect(cell[0], cell[1], cell_size, cell_size)):
            collision += 1

    
    if collision <3 :
        print("You hit the wall !!")
        run = False
```

Maintenant, on va faire en sorte que le joueur ne puisse pas sortir de l'écran : 

On utilisera des min et des max. Du grand clasique !

```python
    player.rect.left = max(0, player.rect.left)
    player.rect.right = min(screen.get_width(), player.rect.right)
    player.rect.top = max(0, player.rect.top)
    player.rect.bottom = min(screen.get_height(), player.rect.bottom)

    player.update() 
```

### Étape 7 : Affichage

Donnons vie au joueur. Oui que maintenant. Où est le problème ;) . 

Pour ce faire on utilisera le .blit. 

Si vous avez bien suivi, vous savez alors que l'on utilisera screen.blit().

Pour que ça marche, il nous faut l'image du joueurs ( définie dans la classe player) et son rect (même chôse). 

```python
screen.blit(player.image, player.rect)
```

> Penssez bien à garder la mise a jour le display 
