import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

while True:
    screen.fill((200, 200, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
