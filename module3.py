import pygame
from Character_Object import miner

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
time = 0

class building(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        if type == 0: #To save memory if type is 0 then its the setting building
            self.image = pygame.image.load("Textures/Menu/Setting_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))
        elif type == 1: #Type 1 = Vault Building
            self.image = pygame.image.load("Textures/Menu/Vault_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))

class invisWall(pygame.sprite.Sprite): #Creates an invisible Wall, this prevents the player from leaving the screen and forces them into the playing area
    def __init__(self, start, visible, stretch):
        super().__init__()
        if visible:
            self.image = pygame.Surface(stretch)
            self.image.fill((255, 0, 0))
        else:
            self.image = pygame.Surface(stretch, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = start)

settingBlock = building(0, 300, 540)
vaultBlock = building(1, 1620, 540)
playerA = miner(960, 540, 5)
invisWallGroup = pygame.sprite.Group()
blocks = [[(0, 470), 0, (600, 10)], [(600, 780), 0, (260, 10)], [(600, 470), 0, (10, 310)], [(850, 0), 0, (10, 780)], [(1320, 470), 0, (600, 10)], [(1310, 470), 0, (10, 310)], [(1060, 0), 0, (10, 780)], [(1070, 770), 0, (240, 10)]]
for pos1, visible, pos2 in blocks:
    invisWallGroup.add(invisWall(pos1, visible, pos2))

while True:
    screen.fill((50, 50, 50))

    keys = pygame.key.get_pressed() #Checks which keys are pressed and moves accordingly

    if keys[pygame.K_w]:
        playerA.update(0, 1, time, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(0, -1, time, 0)
    if keys[pygame.K_s]:
        playerA.update(0, -1, time, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(0, 1, time, 0)
    if keys[pygame.K_a]:
        playerA.update(-1, 0, time, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(1, 0, time, 0)
    if keys[pygame.K_d]:
        playerA.update(1, 0, time, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False):
            playerA.update(-1, 0, time, 0)

    pygame.draw.rect(screen, (35, 35, 35), ((860, 0), (200, 1080))) #Middle Path
    pygame.draw.rect(screen, (25, 25, 25), ((0, 480), (600, 600))) #Left Platform
    pygame.draw.rect(screen, (25, 25, 25), ((1320, 480), (600, 600))) #Right Platform
    pygame.draw.rect(screen, (25, 25, 25), ((600, 780), (260, 300))) #Left Connector
    pygame.draw.rect(screen, (25, 25, 25), ((1060, 780), (260, 300))) #Right Connector

    invisWallGroup.draw(screen)
    screen.blit(playerA.image, playerA.rect)
    screen.blit(settingBlock.image, settingBlock.rect)
    screen.blit(vaultBlock.image, vaultBlock.rect)

    pygame.display.flip() #Updates and controls the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

            if event.key == pygame.K_KP_PLUS:
                pygame.image.save(screen, "menuPage.png")
    pygame.time.Clock().tick(60)
    time += 1
    if time == 60:
        time = 0