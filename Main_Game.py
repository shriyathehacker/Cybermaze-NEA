import pygame
from importlib import import_module
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
        elif type == 2: #Type 2 = Cave Entrance
            self.image = pygame.image.load("Textures/Menu/Cave_Entrance.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))

        self.mask = pygame.mask.from_surface(self.image)

class invisWall(pygame.sprite.Sprite): #Creates an invisible Wall, this prevents the player from leaving the screen and forces them into the playing area
    def __init__(self, start, visible, stretch):
        super().__init__()
        if visible:
            self.image = pygame.Surface(stretch)
            self.image.fill((255, 0, 0))
        else:
            self.image = pygame.Surface(stretch, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = start)
        self.mask = pygame.mask.from_surface(self.image)

class loadingZone(pygame.sprite.Sprite):
    def __init__(self, join, start, stretch, visible):
        super().__init__()
        if visible:
            self.image = pygame.Surface(stretch)
            self.image.fill((0, 255, 0))
        else:
            self.image = pygame.Surface(stretch, pygame.SRCALPHA)

        self.rect = self.image.get_rect(topleft = start)
        self.join = join
        self.mask = pygame.mask.from_surface(self.image)

    def activate(self):
        import_module(self.join)

settingBlock = building(0, 300, 540)
vaultBlock = building(1, 1620, 540)
cave = building(2, 960, 160)
playerA = miner(960, 540, 5)

invisWallGroup = pygame.sprite.Group()
loadingZonesGroup = pygame.sprite.Group()

invisWallVisible = True
loadingZoneVisible = True
loadingZones = [
    ["Game.py", (860, 150), (200, 100)], #Cave Loading Zone --> Main Game
    ["Setting_Menu.py", (332, 650), (96, 96)], #Setting Loading Zone --> Setting Hub
    ["Vault_Menu.py", (1492, 650), (96, 96)] #Vault Loading Zone --> Vault Menu
    ]
blocks = [
            [(0, 0), (1920, 10)], #Top Wall
            [(0, 0), (10, 1080)], #Left Wall
            [(1910, 0), (10, 1080)], #Right Wall
            [(0, 1070), (1920, 10)], #Bottom Wall
            [(0, 470), (600, 10)], #Left Section Top Wall
            [(600, 770), (260, 10)], #Left Section Bottom Wall
            [(600, 470), (10, 310)], #Left Section Vertical Wall
            [(850, 400), (10, 380)], #Middle Path Left Wall
            [(1320, 470), (600, 10)], #Right Section Top Wall
            [(1310, 470), (10, 310)], #Right Section Vertical Wall
            [(1060, 400), (10, 380)], #Middle Path Right Wall
            [(1070, 770), (240, 10)], #Right Section Bottom Wall
            [(640, 100), (10, 300)], #Cave Right Wall
            [(1270, 100), (10, 300)], #Cave Left Wall
            [(650, 90), (620, 10)], #Cave Top Wall
            [(650, 400), (210, 10)], #Cave Bottom Right Wall
            [(1060, 400), (210, 10)], #Cave Bottom Left Wall

            [(204, 444), (16, 352)], #Setting Block Left Wall
            [(220, 780), (112, 16)], #Setting Block Bottom Left Wall
            [(316, 650), (16, 130)], #Setting Block Left Wall Inside
            [(428, 650), (16, 130)], #Setting Block Right Wall Inside
            [(428, 780), (112, 16)], #Setting Block Bottom Right Wall
            [(540, 444), (16, 352)], #Setting Block Right Wall
            [(44, 284), (16, 352)], #Setting Block Left Most Wall
            [(60, 636), (16, 16)], #Setting Diagonal 1
            [(76, 652), (16, 16)], #Setting Diagonal 2
            [(93, 668), (16, 16)], #Setting Diagonal 3
            [(109, 684), (16, 16)], #Setting Diagonal 4
            [(125, 700), (16, 16)], #Setting Diagonal 5
            [(141, 716), (16, 16)], #Setting Diagonal 6
            [(157, 732), (16, 16)], #Setting Diagonal 7
            [(173, 748), (16, 16)], #Setting Diagonal 8
            [(189, 764), (16, 16)], #Setting Diagonal 9

            [(1364, 444), (16, 352)], #Vault Block Left Wall
            [(1860, 284), (16, 352)], #Vault Block Right Most Wall
            [(1380, 780), (112, 16)], #Vault Block Bottom Left Wall
            [(1476, 650), (16, 130)], #Vault Block Left Wall Inside
            [(1588, 650), (16, 130)], #Vault Block Right Wall Inside
            [(1588, 780), (128, 16)], #Vault Block Bottom Right Wall
            [(1700, 444), (16, 352)], #Vault Block Right Wall
            [(1844, 636), (16, 16)], #Vault Diagonal 1
            [(1828, 652), (16, 16)], #Vault Diagonal 2
            [(1812, 668), (16, 16)], #Vault Diagonal 3
            [(1796, 684), (16, 16)], #Vault Diagonal 4
            [(1780, 700), (16, 16)], #Vault Diagonal 5
            [(1764, 716), (16, 16)], #Vault Diagonal 6
            [(1748, 732), (16, 16)], #Vault Diagonal 7
            [(1732, 748), (16, 16)], #Vault Diagonal 8
            [(1716, 764), (16, 16)], #Vault Diagonal 9
]

for pos1, pos2 in blocks:
    invisWallGroup.add(invisWall(pos1, invisWallVisible, pos2))

for join, pos1, pos2 in loadingZones:
    loadingZonesGroup.add(loadingZone(join, pos1, pos2, loadingZoneVisible))

while True:
    screen.fill((50, 50, 50))

    keys = pygame.key.get_pressed() #Checks which keys are pressed and moves accordingly

    vector = [0, 0]
    moved = False
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        playerA.update(0, 1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask):
            playerA.update(0, -1)
        else:
            vector[1] += 1
            moved = True

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        playerA.update(0, -1)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask):
            playerA.update(0, 1)
        else:
            vector[1] -= 1
            moved = True

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        playerA.update(1, 0)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask):
            playerA.update(-1, 0)
        else:
            vector[0] += 1
            moved = True

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        playerA.update(-1, 0)
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask):
            playerA.update(1, 0)
        else:
            vector[0] -= 1
            moved = True

    playerA.animation(vector[0], vector[1], time, 1)

    loadingZonesEntered = pygame.sprite.spritecollide(playerA, loadingZonesGroup, False)
    
    if loadingZonesEntered != []:
        loadingZonesEntered[0].activate()

    pygame.draw.rect(screen, (35, 35, 35), ((860, 0), (200, 1080))) #Middle Path
    pygame.draw.rect(screen, (25, 25, 25), ((0, 480), (600, 600))) #Left Platform
    pygame.draw.rect(screen, (25, 25, 25), ((1320, 480), (600, 600))) #Right Platform
    pygame.draw.rect(screen, (25, 25, 25), ((600, 780), (260, 300))) #Left Connector
    pygame.draw.rect(screen, (25, 25, 25), ((1060, 780), (260, 300))) #Right Connector
    pygame.draw.rect(screen, (25, 25, 25), ((650, 100), (620, 300))) #Cave Platform

    screen.blit(settingBlock.image, settingBlock.rect)
    screen.blit(vaultBlock.image, vaultBlock.rect)
    screen.blit(cave.image, cave.rect)
    invisWallGroup.draw(screen)
    loadingZonesGroup.draw(screen)
    screen.blit(playerA.image, playerA.rect)

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