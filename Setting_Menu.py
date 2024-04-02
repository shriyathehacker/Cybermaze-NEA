import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                exit()
                
    pygame.draw.rect(screen, (255, 200, 200), ((200, 200), (100, 200)))

    pygame.display.flip()
    pygame.time.Clock().tick(60)