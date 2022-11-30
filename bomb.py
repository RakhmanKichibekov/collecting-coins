import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, group1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bomb.png").convert()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 8, self.image.get_height() // 8))
        self.rect = self.image.get_rect(center=(x, y))
        self.image.set_colorkey((255, 255, 255))
        self.speed = speed
        self.add(group1)

    def update(self, *args):
        if self.rect.y < args[0] + 200:
            self.rect.y += self.speed
        else:
            self.kill()