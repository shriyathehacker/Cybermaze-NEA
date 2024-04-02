import pygame

class miner(pygame.sprite.Sprite): #Creates a movable player
    def __init__(self, x, y, velocity): #Initializes the player
        super().__init__()
        self.idleAnimations = ["Textures/Characters/Miner/miner_idle_1.png", "Textures/Characters/Miner/miner_idle_2.png"]
        self.flippedAnimations = ["Textures/Characters/Miner/miner_idle_1_flip.png", "Textures/Characters/Miner/miner_idle_2_flip.png"]
        self.animations = [self.flippedAnimations, self.idleAnimations]
        self.velocity = velocity
        self.facingDirection = 1 #1 = Facing to Right, 0 = Facing to Left
        self.currentAnimation = 0
        self.image = pygame.image.load(self.animations[self.facingDirection][self.currentAnimation]).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dx, dy): #Allows the player to move
        self.rect.x += dx * self.velocity
        self.rect.y -= dy * self.velocity
        
    def animation(self, dx, dy, time, flip): #Sorts out animations
        if dx < 0 and self.facingDirection == 1 and flip:
            self.facingDirection = 0
        if dx > 0 and self.facingDirection == 0 and flip:
            self.facingDirection = 1

        if (abs(dx) + abs(dy) == 0 and time == 30) or (abs(dx) + abs(dy) != 0 and time % 5 == 1):
            if self.currentAnimation == 0:
                self.currentAnimation = 1
            else:
                self.currentAnimation = 0

        self.image = pygame.image.load(self.animations[self.facingDirection][self.currentAnimation]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)