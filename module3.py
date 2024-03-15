import pygame

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

class building(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        if type == 0: #To save memory if type is 0 then its the setting building
            self.image = pygame.image.load("Textures/Menu/Setting_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))
        elif type == 1:
            self.image = pygame.image.load("Textures/Menu/Vault_Building.png").convert_alpha()
            self.rect = self.image.get_rect(center = (x, y))

class player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        self.velocity = velocity
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 200, 200))
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, dx, dy):
        self.rect.x += dx * self.velocity
        self.rect.y -= dy * self.velocity

settingBlock = building(0, 300, 540)
vaultBlock = building(1, 1600, 540)
playerA = player(960, 540, 3)

while True:
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

    keys = pygame.key.get_keys()

    if keys[pygame.K_w]:
        playerA.update(0, -1)
    if keys[pygame.K_s]:
        playerA.update(0, 1)
    if keys[pygame.K_a]:
        playerA.update(-1, 0)
    if keys[pygame.K_d]:
        playerA.update(1, 0)

    pygame.draw.rect(screen, (25, 25, 25), ((0, 540), (1920, 1080)))
    screen.blit(playerA.image, playerA.rect)
    screen.blit(settingBlock.image, settingBlock.rect)
    screen.blit(vaultBlock.image, vaultBlock.rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
