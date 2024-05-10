import pygame
from Character_Object import miner, Drill, slime
from random import randint, choice

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
time = 0

#Game Specific Variables
totalSlimes = 1
score = 0

def summonSlime(slimeGroup, allTilesGroup):
    spawnPos = choice(possibleSpawnLocations) #Randomly pick a possible spawn location
    for path in pathGroup:
        if spawnPos == path.id: #Find the path
            relativeSpawnPos = (path.rect.x, path.rect.y) #Get the position of the tile
            break
    slimeAlpha = slime(*relativeSpawnPos) #Spawn a slime on the position
    allTilesGroup.add(slimeAlpha) #Add the slime to the groups
    slimeGroup.add(slimeAlpha) #Summon Slime

def placeTile(x, y):
    return ((200 * x) + 960, (200 * y) + 540) #Place Tile

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, playerPos): #initalize it
        super().__init__() #Call the sprite from pygame
        self.id = (x, y) #Give it a unique identifier
        self.image = pygame.Surface((200, 200)) #Create the surface
        self.rect = self.image.get_rect(center = placeTile(x - playerPos[0], y - playerPos[1])) #Place it in its position
        self.mask = pygame.mask.from_surface(self.image) #Attach a bitmask

    def update(self, dx, dy): #Update its position
        self.rect.x -= dx * player.velocity
        self.rect.y += dy * player.velocity #Tile

class Path(Tile):
    def __init__(self, x, y, playerPos):
        super().__init__(x, y, playerPos) #Call SuperObject
        self.image = pygame.image.load("Textures\MainGame\path.png").convert_alpha() #Place the texture on top of it
        temp = randint(0, 3)
        self.image = pygame.transform.rotate(self.image, temp * 90) #Rotate it so that the board doesn't look the same

class Wall(Tile):
    def __init__(self, x, y, playerPos):
        super().__init__(x, y, playerPos) #Call SuperObject
        self.image = pygame.image.load("Textures\MainGame\wall.png").convert_alpha() #Place the texture on top of it
        temp = randint(0, 3)
        self.image = pygame.transform.rotate(self.image, temp * 90) #Rotate it so that all the tiles don't look the same

class health(pygame.sprite.Sprite):
    def __init__(self, health, x, y):
        super().__init__()
        self.health = health
        self.image = pygame.image.load("Textures\MainGame\health_wheel_full.png").convert_alpha() #Initalize the health wheel with full health
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        if self.health == 3:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_full.png").convert_alpha() #Updates the healthbar with the according health
        elif self.health == 2:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_hurt.png").convert_alpha()
        elif self.health == 1:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_dead.png").convert_alpha() #Health

#Create all the sprite groups
wallGroup = pygame.sprite.Group()
allTilesGroup = pygame.sprite.Group()
pathGroup = pygame.sprite.Group()
slimeGroup = pygame.sprite.Group()

tileMap = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
] #20x20 Premade TileMap

possibleSpawnLocations = []

for row in range(len(tileMap)):
    for colum in range(len(tileMap[row])):
        if tileMap[row][colum] == 2:
            playerTile = (colum, row) #Find the players starting position

for row in range(len(tileMap)):
    for column in range(len(tileMap[row])):
        if tileMap[row][column] == 1:
            wall = Wall(column, row, playerTile) #If its one create a wall tile
            wallGroup.add(wall)
            allTilesGroup.add(wall)
        else:
            path = Path(column, row, playerTile) #else create a path tile
            allTilesGroup.add(path)
            pathGroup.add(path)
            possibleSpawnLocations.append((column, row)) #Place it in the possible spawn locations for slime

#create all the objects
player = miner(960, 540, 10, 2)
healthBar = health(player.health, 150, 150)
drill = Drill(960, 540)
summonSlime(slimeGroup, allTilesGroup)
healthBarGroup = pygame.sprite.GroupSingle(healthBar)

while True:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed() #Get the keys

    vector = [0, 0] #Start with the initial movement vector as 0, 0
    moved = False #Initalize whether or not the character has moved
    if keys[pygame.K_w] or keys[pygame.K_UP]: #If they press W or up
        allTilesGroup.update(0, 1) #Shift the map
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask): #If they collide with a wall
            allTilesGroup.update(0, -1) #Shift the map back
        else:
            moved = True #else they would have moved
            vector[1] += 1 #Update the vector

    if keys[pygame.K_s] or keys[pygame.K_DOWN]: #Repeat
        allTilesGroup.update(0, -1)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(0, 1)
        else:
            moved = True
            vector[1] -= 1

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        allTilesGroup.update(1, 0)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(-1, 0)
        else:
            moved = True
            vector[0] += 1

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        allTilesGroup.update(-1, 0)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(1, 0)
        else:
            moved = True
            vector[0] -= 1

    direction, popUp = player.animation(vector[0], vector[1], time, 1) #Work out which direction we are facing
    if not(moved) and pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask): #If we are in a wall, we kick the player out
        if direction:
            allTilesGroup.update(1, 0)
        else:
            allTilesGroup.update(-1,0)

        if popUp:
            allTilesGroup.update(0, -1)

    healthBarGroup.update() #Update everything
    drill.update(pygame.mouse.get_pos(), time)
    player.immune(0, time)
    for slimes in slimeGroup:
        slimes.animate(time)
        slimes.move()

    slimeGroup.draw(screen) #Place everything on the screen
    allTilesGroup.draw(screen)
    screen.blit(player.image, player.rect)
    screen.blit(drill.image, drill.rect)
    healthBarGroup.draw(screen)

    if pygame.sprite.spritecollide(drill, slimeGroup, True, pygame.sprite.collide_mask): #If slime collides with the drill it dies
        totalSlimes += 1 #Add more slimes
        score += 100
        summonSlime(slimeGroup, allTilesGroup)#Summon all those slimes
        summonSlime(slimeGroup, allTilesGroup)

    if pygame.sprite.spritecollide(player, slimeGroup, False, pygame.sprite.collide_mask) and not(player.immunity): #If slime collides with player
        healthBar.health -= 1 #Player takes damage
        player.immune(1, time) #Give player invisibility frames
        if healthBar.health == 0: #if the health is 0
            pygame.quit() #End game
            exit()

    for event in pygame.event.get(): #Iterate though event handler
        if event.type == pygame.QUIT: #If they have quitted the game
            pygame.quit() #Quit
            exit()

        if event.type == pygame.KEYDOWN: #Check if they pressed a button
            if event.key == pygame.K_KP_ENTER: #If its the keypad enter
                pygame.quit() #Quit - this is for testing purposes
                exit()

            if event.key == pygame.K_KP_PLUS: #If its keypad plus
                pygame.image.save(screen, "gameImage.png") #Save the current Screen Image

    pygame.display.flip() #Update the screen
    pygame.time.Clock().tick(60) #Runs at 60fps
    time += 1 #Increments the time
    if time == 60: #If time is 60
        time = 0 #Reset it