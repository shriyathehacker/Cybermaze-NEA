import pygame
from Character_Object import miner

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
time = 0

def placeTile(x, y):
    return ((100 * x) + 960, (100 * y) + 540)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, playerPos):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center = placeTile(x - playerPos[0], y - playerPos[1]))

    def update(self, dx, dy):
        self.rect.x -= dx * player.velocity
        self.rect.y += dy * player.velocity

tileGroup = pygame.sprite.Group()

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
            tileGroup.add(Tile(column, row, playerTile))

player = miner(960, 540, 10)
while True:
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    vector = [0, 0]
    moved = False
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        tileGroup.update(0, 1)
        if pygame.sprite.spritecollide(player, tileGroup, False):
            tileGroup.update(0, -1)
        else:
            vector[1] += 1

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        tileGroup.update(0, -1)
        if pygame.sprite.spritecollide(player, tileGroup, False):
            tileGroup.update(0, 1)
        else:
            vector[1] -= 1

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        tileGroup.update(1, 0)
        if pygame.sprite.spritecollide(player, tileGroup, False):
            tileGroup.update(-1, 0)
        else:
            vector[0] += 1

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        tileGroup.update(-1, 0)
        if pygame.sprite.spritecollide(player, tileGroup, False):
            tileGroup.update(1, 0)
        else:
            vector[0] -= 1

    player.animation(vector[0], vector[1], time, 1)

    tileGroup.draw(screen)

    screen.blit(player.image, player.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    time += 1
    if time == 60:
        time = 0