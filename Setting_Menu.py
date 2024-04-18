import pygame
from Character_Object import miner

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
time = 0

playerA = miner(960, 540, 5)
invisWallGroup = pygame.sprite.Group()

while True:

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

    screen.blit(playerA.image, playerA.rect)
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