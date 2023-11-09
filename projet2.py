# A simple game where you have to fly through a path without hitting the walls.

# Specifications:
# - The ship can move left and right using the arrow keys to deplace block by block. The ship can also move up and down using the arrow keys to take some advance or keep calm.
# - The ship cannot move outside the screen.
# - The screen is like a grid, with the ship moving from one cell to another.
# - The ship is made of three cells and one another cell on top of them (like a reverse T shape).
# - The path is made of two walls and a space in between. The space is at minimum the same width as the ship.
# - The path moves left and right, starting from the top of the screen and moving down, it's random and infinite (like a flappy bird game with pipes).
# - The ship must fly through the path without hitting the walls. If it hits a wall, the game is over.
# - There is a score counter that increases by time, the longer you survive, the higher the score.
# - On screen menu, we can start a new game or quit the game, and we can see the 10 highest scores.
# - On a game over, we can enter our name and save our score to the list of highest scores. The list is saved to a file. The list is sorted by score, highest to lowest. Then we can start a new game or quit the game.

import pygame
import random

### Initialisation

successes, failures = pygame.init() # initialisation de pygame
print("{0} successes and {1} failures".format(successes, failures))
pygame.display.set_caption('Projet 2') 

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60
time = pygame.time.get_ticks() #Temps 

# FPS text
font = pygame.font.SysFont("Arial", 18)
font_color = pygame.Color("white")
dt_text = font.render("FPS: 0", True, font_color)
dt_text_rect = dt_text.get_rect()
dt_text_rect.midtop = (screen.get_width()-33, 0)

#Score text
dt_text1 = font.render("Score: 0",True, font_color)
dt_text1_rect = dt_text1.get_rect()
dt_text1_rect.midtop = (30,0)

#Time survived text

dt_text2 = font.render("Time survived : 0",True, font_color)
dt_text2_rect = dt_text2.get_rect()
dt_text2_rect.midtop = (55,30)

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

cell_size = 16
score = 0
path = []

# Création du chemin
x, y = (screen.get_width() / 2) - (cell_size * 3.5), 0
while y < screen.get_height():
    path.append([int(x), y])
    x += cell_size
    if x >= (screen.get_width() / 2) + (cell_size * 3.5):
        x = (screen.get_width() / 2) - (cell_size * 3.5)
        y += cell_size
#print(path) DEBUG

# Création du joueur
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

def updatePath(): # Déplacement du chemin, on ajoute une ligne au début et on fais avancer vers le bas les lignes suivantes en retirant la dernière
    global path
    global score
    #Augmentation du score
    score += 1
    # Décalage vers le bas
    for cell in path:
        cell[1] += cell_size
        if cell[1] >= screen.get_height(): # Suppression de la dernière ligne
            path.remove(cell)
    # Ajout d'une ligne au début
    x = random.randint(-1,1)
    new_line = [path[0][0] + (x * cell_size), 0]
    path.insert(0, new_line)
    for i in range(6):
        path.insert(i+1,[new_line[0] + ((1+i) * cell_size), 0])        


### Boucle principale
last_update_time = pygame.time.get_ticks()
update_interval = 1000
running = True
while running:
    paused = False
    dt = clock.tick(FPS) / 1000  # Deltatime en secondes

    #Timer init
    counting_time = pygame.time.get_ticks() - time
    counting_minutes = int(counting_time/60000)
    counting_seconds = int((counting_time%60000)/1000)
    counting_millisecond = int(counting_time%1000)
    counting_text = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

    #Timer

    dt_text = font.render("FPS: {0}".format(int(clock.get_fps())), True, font_color)
    dt_text1 = font.render("Score: {0}".format(int(score)),True, font_color)
    dt_text2 = font.render("Time survived: {0}".format(str(counting_text)),1,font_color)

    ### Jeu
    screen.fill(BLACK)

    # Check if it's time to update the path
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= update_interval:
        updatePath()
        last_update_time = current_time
        update_interval = update_interval * 0.99

    # Affichage du chemin
    for cell in path:
        pygame.draw.rect(screen, GREY, (cell[0], cell[1], cell_size, cell_size), 1)

    for event in pygame.event.get(): ## Vérification de pression d'une touche par l'utilisateur 
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
            elif event.key == pygame.K_ESCAPE: # Pause game
                paused = True
                while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                                paused = False
                                #modif après édition
                                pygame.event.clear()
                                break
    
    # Vérification des collisions
    collision = 0
    for cell in path:
        if player.rect.colliderect(pygame.Rect(cell[0], cell[1], cell_size, cell_size)):
            collision += 1
            #print (collision) DEBUG

    
    if collision <3 :
        print("You hit the wall !!")
        running = False
 
    player.rect.left = max(0, player.rect.left)
    player.rect.right = min(screen.get_width(), player.rect.right)
    player.rect.top = max(0, player.rect.top)
    player.rect.bottom = min(screen.get_height(), player.rect.bottom)

    player.update() 

    #Affichage  
    
    screen.blit(player.image, player.rect)
    screen.blit(dt_text, dt_text_rect)
    screen.blit(dt_text1, dt_text1_rect)
    screen.blit(dt_text2, dt_text2_rect)
    pygame.display.update()

print("Exited the game loop. Game will quit...")
print ("Your score was",score)
pygame.quit()