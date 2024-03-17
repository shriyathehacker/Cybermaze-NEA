from pydoc import visiblename
import pygame

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

class building(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        if type == 0: #To save memory if type is 0 then its the setting building
            self.image = pygame.image.load("Textures/Menu/Setting_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))
        elif type == 1: #Type 1 = Vault Building
            self.image = pygame.image.load("Textures/Menu/Vault_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))

class player(pygame.sprite.Sprite): #Creates a movable player
    def __init__(self, x, y, velocity): #Initializes the player
        super().__init__()
        self.velocity = velocity
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 200, 200))
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, dx, dy): #Allows the player to move
        self.rect.x += dx * self.velocity
        self.rect.y -= dy * self.velocity

class invisWall(pygame.sprite.Sprite):
    def __init__(self, x, y, visible, xStretch, yStretch):
        super().__init__()
        self.id = (x, y)
        self.image = pygame.Surface((xStretch, yStretch))
        if visible:
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (x, y))

settingBlock = building(0, 300, 540)
vaultBlock = building(1, 1620, 540)
playerA = player(960, 540, 10)
invisWallGroup = pygame.sprite.Group()
blocks = [[320, 540, 1, 20, 100]]
for x, y, visible, xStretch, yStretch in blocks:
    invisWallGroup.add(invisWall(x, y, visible, xStretch, yStretch))

while True:
    screen.fill((50, 50, 50))

    keys = pygame.key.get_pressed() #Checks which keys are pressed and moves accordingly

    if keys[pygame.K_w]:
        playerA.update(0, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(0, -1)
    if keys[pygame.K_s]:
        playerA.update(0, -1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(0, 1)
    if keys[pygame.K_a]:
        playerA.update(-1, 0)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(1, 0)
    if keys[pygame.K_d]:
        playerA.update(1, 0)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(-1, 0)

    pygame.draw.rect(screen, (25, 25, 25), ((0, 540), (600, 1080))) #Places the buildings and player on the screen
    pygame.draw.rect(screen, (25, 25, 25), ((0, 880), (800, 1080)))
    pygame.draw.rect(screen, (25, 25, 25), ((1320, 540), (1920, 1080)))
    pygame.draw.rect(screen, (25, 25, 25), ((1120, 880), (1920, 1080)))
    screen.blit(playerA.image, playerA.rect)
    screen.blit(settingBlock.image, settingBlock.rect)
    screen.blit(vaultBlock.image, vaultBlock.rect)
    invisWallGroup.draw(screen)

    pygame.display.flip() #Updates and controls the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

            if event.key == pygame.K_KP_PLUS:
                pygame.image.save(screen, "menuPage.png")
    pygame.time.Clock().tick(60)
