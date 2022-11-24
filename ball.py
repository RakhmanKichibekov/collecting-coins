import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, speed, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))
        self.rect = self.image.get_rect(center=(x, y))
        self.image.set_colorkey((255, 255, 255))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] + 200:
            self.rect.y += self.speed
        else:
            self.kill()
