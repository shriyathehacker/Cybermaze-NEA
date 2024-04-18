import pygame
from importlib import import_module
from Character_Object import miner

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
time = 0
running = True

class building(pygame.sprite.Sprite): #The buildings, setting, vault, cave
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
        self.mask.fill()

class loadingZone(pygame.sprite.Sprite): #Loading Zones to link Files together
    def __init__(self, join, start, stretch, visible): #Initializes the loading zones
        super().__init__()
        if visible:
            self.image = pygame.Surface(stretch)
            self.image.fill((0, 255, 0))
        else:
            self.image = pygame.Surface(stretch, pygame.SRCALPHA)

        self.rect = self.image.get_rect(topleft = start)
        self.join = join

    def activate(self): #When the player collides with the loading zone, it will activate the next file
        import_module(self.join)

settingBlock = building(0, 260, 540) #Create the Buildings and Players
vaultBlock = building(1, 1660, 540)
cave = building(2, 960, 160)
playerA = miner(960, 540, 5, 1)

invisWallGroup = pygame.sprite.Group()
loadingZonesGroup = pygame.sprite.Group()

invisWallVisible = False #To show the invisible walls and loading zones (for debugging)
loadingZoneVisible = False
loadingZones = [
    ["Game.py", (860, 150), (200, 100)], #Cave Loading Zone --> Main Game
    ["Setting_Menu.py", (292, 650), (96, 96)], #Setting Loading Zone --> Setting Hub
    ["Vault_Menu.py", (1532, 650), (96, 96)] #Vault Loading Zone --> Vault Menu
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

            [(164, 444), (16, 352)], #Setting Block Left Wall
            [(180, 780), (112, 16)], #Setting Block Bottom Left Wall
            [(276, 650), (16, 130)], #Setting Block Left Wall Inside
            [(388, 650), (16, 130)], #Setting Block Right Wall Inside
            [(388, 780), (112, 16)], #Setting Block Bottom Right Wall
            [(500, 444), (16, 352)], #Setting Block Right Wall
            [(4, 284), (16, 352)], #Setting Block Left Most Wall
            [(19, 636), (16, 16)], #Setting Diagonal 1
            [(35, 652), (16, 16)], #Setting Diagonal 2
            [(52, 668), (16, 16)], #Setting Diagonal 3
            [(68, 684), (16, 16)], #Setting Diagonal 4
            [(84, 700), (16, 16)], #Setting Diagonal 5
            [(100, 716), (16, 16)], #Setting Diagonal 6
            [(116, 732), (16, 16)], #Setting Diagonal 7
            [(132, 748), (16, 16)], #Setting Diagonal 8
            [(148, 764), (16, 16)], #Setting Diagonal 9

            [(1404, 444), (16, 352)], #Vault Block Left Wall
            [(1900, 284), (16, 352)], #Vault Block Right Most Wall
            [(1420, 780), (112, 16)], #Vault Block Bottom Left Wall
            [(1516, 650), (16, 130)], #Vault Block Left Wall Inside
            [(1628, 650), (16, 130)], #Vault Block Right Wall Inside
            [(1628, 780), (128, 16)], #Vault Block Bottom Right Wall
            [(1740, 444), (16, 352)], #Vault Block Right Wall
            [(1884, 636), (16, 16)], #Vault Diagonal 1
            [(1868, 652), (16, 16)], #Vault Diagonal 2
            [(1852, 668), (16, 16)], #Vault Diagonal 3
            [(1836, 684), (16, 16)], #Vault Diagonal 4
            [(1820, 700), (16, 16)], #Vault Diagonal 5
            [(1804, 716), (16, 16)], #Vault Diagonal 6
            [(1788, 732), (16, 16)], #Vault Diagonal 7
            [(1772, 748), (16, 16)], #Vault Diagonal 8
            [(1756, 764), (16, 16)], #Vault Diagonal 9

            [(790, 310), (70, 10)], #Cave Entrance Horizontal Left
            [(780, 300), (10, 10)], #Cave Diagonal 1 1
            [(770, 290), (10, 10)], #Cave Diagonal 1 2
            [(760, 280), (10, 10)], #Cave Diagonal 1 3
            [(750, 270), (10, 10)], #Cave Diagonal 1 4
            [(740, 260), (10, 10)], #Cave Diagonal 1 5
            [(730, 250), (10, 10)], #Cave Diagonal 1 6
            [(720, 240), (10, 10)], #Cave Diagonal 1 7
            [(710, 90), (10, 150)], #Cave Vertical Left
            [(850, 90), (10, 220)], #Cave Loading Zone Left
            [(1060, 90), (10, 220)], #Cave Loading Zone Right
            [(1060, 310), (70, 10)], #Cave Entrance Horizontal Right
            [(1130, 300), (10, 10)], #Cave Diagonal 2 1
            [(1140, 290), (10, 10)], #Cave Diagonal 2 2
            [(1150, 280), (10, 10)], #Cave Diagonal 2 3
            [(1160, 270), (10, 10)], #Cave Diagonal 2 4
            [(1170, 260), (10, 10)], #Cave Diagonal 2 5
            [(1180, 250), (10, 10)], #Cave Diagonal 2 6
            [(1190, 240), (10, 10)], #Cave Diagonal 2 7
            [(1200, 90), (10, 150)], #Cave Vertical Right
]

for pos1, pos2 in blocks:
    invisWallGroup.add(invisWall(pos1, invisWallVisible, pos2))

for join, pos1, pos2 in loadingZones:
    loadingZonesGroup.add(loadingZone(join, pos1, pos2, loadingZoneVisible))

while running:
    screen.fill((50, 50, 50))

    keys = pygame.key.get_pressed() #Checks which keys are pressed and moves accordingly

    vector = [0, 0]
    moved = False
    if keys[pygame.K_w] or keys[pygame.K_UP]: #Check if key has been pressed
        playerA.update(0, 1) #Move the player in that direction
        if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask): #If they walk into a wall (ie are in the wall)
            playerA.update(0, -1) #Move them out of the wall
        else:
            vector[1] += 1 #This is so the animations know which direction we have moved
            moved = True #To tell the animations whether we are idle or moving

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

    playerA.animation(vector[0], vector[1], time, 1) #Updates Animations

    if pygame.sprite.spritecollide(playerA, invisWallGroup, False, pygame.sprite.collide_mask): #Checks if we are stuck in a wall (from changing directions)
        playerA.collide()

    loadingZonesEntered = pygame.sprite.spritecollide(playerA, loadingZonesGroup, False) #Check if we have entered a loading zone
    
    if loadingZonesEntered != []:
        loadingZonesEntered[0].activate() #Visits a loading zone

    pygame.draw.rect(screen, (35, 35, 35), ((860, 0), (200, 1080))) #Middle Path
    pygame.draw.rect(screen, (25, 25, 25), ((0, 480), (600, 600))) #Left Platform
    pygame.draw.rect(screen, (25, 25, 25), ((1320, 480), (600, 600))) #Right Platform
    pygame.draw.rect(screen, (25, 25, 25), ((600, 780), (260, 300))) #Left Connector
    pygame.draw.rect(screen, (25, 25, 25), ((1060, 780), (260, 300))) #Right Connector
    pygame.draw.rect(screen, (25, 25, 25), ((650, 100), (620, 300))) #Cave Platform

    screen.blit(settingBlock.image, settingBlock.rect) #Blit all the buildings
    screen.blit(vaultBlock.image, vaultBlock.rect)
    screen.blit(cave.image, cave.rect)
    invisWallGroup.draw(screen) #Blit the invisible walls
    loadingZonesGroup.draw(screen) #Blit the loading zones
    screen.blit(playerA.image, playerA.rect) #Blit the player

    pygame.display.flip() #Updates and controls the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Check if the game has been quitted
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: #If we have pressed the screen with the mouse we get the coordinates (For debugging)
            print(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN: #Check if we press the key
            if event.key == pygame.K_KP_ENTER: #If we press keypad enter, we exit
                running = False

            if event.key == pygame.K_KP_PLUS: #If we press keypad plus, we take a screen shot
                pygame.image.save(screen, "menuPage.png")

    pygame.time.Clock().tick(60)
    time += 1 #A timing system in order to help orchestrate the game
    if time == 60:
        time = 0

pygame.quit()