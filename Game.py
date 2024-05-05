import pygame
from Character_Object import miner, Drill, slime

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
time = 0

def placeTile(x, y):
    return ((200 * x) + 960, (200 * y) + 540) #Place Tile

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, playerPos):
        super().__init__()
        self.image = pygame.Surface((200, 200))     
        self.rect = self.image.get_rect(center = placeTile(x - playerPos[0], y - playerPos[1]))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx, dy):
        self.rect.x -= dx * player.velocity
        self.rect.y += dy * player.velocity #Tile

class Path(Tile):
    def __init__(self, x, y, playerPos):
        super().__init__(x, y, playerPos) #Call SuperObject
        self.image = pygame.image.load("Textures\MainGame\path.png").convert_alpha() #Path

class Wall(Tile):
    def __init__(self, x, y, playerPos):
        super().__init__(x, y, playerPos) #Call SuperObject
        self.image = pygame.image.load("Textures\MainGame\wall.png").convert_alpha() #Wall

class health(pygame.sprite.Sprite):
    def __init__(self, health, x, y):
        super().__init__()
        self.health = health
        self.image = pygame.image.load("Textures\MainGame\health_wheel_full.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        if self.health == 3:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_full.png").convert_alpha()
        elif self.health == 2:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_hurt.png").convert_alpha()
        elif self.health == 1:
            self.image = pygame.image.load("Textures\MainGame\health_wheel_dead.png").convert_alpha() #Health

wallGroup = pygame.sprite.Group()
allTilesGroup = pygame.sprite.Group()

tileMap = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 2, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

for row in range(len(tileMap)):
    for colum in range(len(tileMap[row])):
        if tileMap[row][colum] == 2:
            playerTile = (colum, row)

for row in range(len(tileMap)):
    for column in range(len(tileMap[row])):
        if tileMap[row][column] == 1:
            wall = Wall(column, row, playerTile)
            wallGroup.add(wall)
            allTilesGroup.add(wall)
        else:
            allTilesGroup.add(Path(column, row, playerTile))

player = miner(960, 540, 10, 2)
healthBar = health(player.health, 150, 150)
drill = Drill(960, 540)
slimeAlpha = slime(500, 500)
healthBarGroup = pygame.sprite.GroupSingle(healthBar)

while True:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    vector = [0, 0]
    moved = False
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        allTilesGroup.update(0, 1)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(0, -1)
        else:
            vector[1] += 1

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        allTilesGroup.update(0, -1)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(0, 1)
        else:
            vector[1] -= 1

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        allTilesGroup.update(1, 0)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(-1, 0)
        else:
            vector[0] += 1

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        allTilesGroup.update(-1, 0)
        if pygame.sprite.spritecollide(player, wallGroup, False, pygame.sprite.collide_mask):
            allTilesGroup.update(1, 0)
        else:
            vector[0] -= 1

    player.animation(vector[0], vector[1], time, 1)
    healthBarGroup.update()
    slimeAlpha.update(time)
    drill.update(pygame.mouse.get_pos(), time)

    allTilesGroup.draw(screen)
    screen.blit(player.image, player.rect)
    screen.blit(drill.image, drill.rect)
    screen.blit(slimeAlpha.image, slimeAlpha.rect)
    healthBarGroup.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

            if event.key == pygame.K_KP_PLUS:
                pygame.image.save(screen, "gameImage.png")

            if event.key == pygame.K_KP_MINUS:
                healthBar.health -= 1

            if event.key == pygame.K_KP_MULTIPLY:
                healthBar.health += 1

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    time += 1
    if time == 60:
        time = 0