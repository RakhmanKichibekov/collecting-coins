import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

W, H = 600, 400
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Game of the year by Rakhman")
pygame.display.set_icon(pygame.image.load("car.png"))
pygame.mixer.music.load("musicBg.mp3")
pygame.mixer.music.play(-1)
music1 = pygame.mixer.Sound("musicMoney.mp3")

PURPLE = (255, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

score = pygame.image.load("check.png").convert()
score = pygame.transform.scale(score, (score.get_width() // 2.5, score.get_height() // 2.5))
score.set_colorkey(WHITE)
f = pygame.font.SysFont('arial', 100)
# pygame.draw.rect(sc, PURPLE, (10, 10, 50, 100), 2)
#
# pygame.draw.line(sc, GREEN, (200, 20), (350, 50), 5)
# pygame.draw.line(sc, GREEN, (200, 40), (350, 70))
#
# pygame.draw.lines(sc, RED, True, [(200, 80), (250, 80), (300, 200)], 2)
# pygame.draw.aalines(sc, RED, True, [(300, 80), (350, 80), (400, 200)])
#
# pygame.draw.polygon(sc, PURPLE, [[150, 210], [180, 250], [90, 290], [30,230]], 2)

pygame.display.update()
FPS = 60
clock = pygame.time.Clock()

rocks_image = ['coin.png', 'coin2.png']
rocks_surf = [pygame.image.load(path).convert() for path in rocks_image]


def createRock(group):
    indx = randint(0, len(rocks_surf) - 1)
    x = randint(20, W * 3 - 20)
    speed = randint(8, 16)
    return Ball(x, 0, rocks_surf[indx], speed, group)

game_score = 0
game_score2 = 0
def collideBalls():
    global game_score
    global game_score2
    for rock in rocks:
        if car_rect.collidepoint(rock.rect.center):
            game_score += 1
            music1.play(1)
            rock.kill()
        if car_rect2.collidepoint(rock.rect.center):
            game_score2 += 1
            music1.play(1)
            rock.kill()

surf = pygame.Surface((200, 200))
surf.fill(RED)
# sc.blit(surf, (50, 50))
pygame.display.update()

rocks = pygame.sprite.Group()

x2 = W // 1.1
y2 = H * 1.5
speed = 12

x = W * 1.5
y = H * 1.5
speed2 = 10

speed3 = 2.3

createRock(rocks)
print("правление синей машинкой WASD\n"
      "красной стрелки")
flRun = True
while flRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRun = False
        elif event.type == pygame.USEREVENT:
            createRock(rocks)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        if (x < 0):
            x = 0
    elif keys[pygame.K_RIGHT]:
        x += speed
        if (x > W * 2.5 -30):
            x = W * 2.5 -30
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_a]:
        x2 -= speed2
        if (x2 < 100):
            x2 = 100
    if keys[pygame.K_w]:
        y2 -= speed2
    elif keys[pygame.K_s]:
        y2 += speed2
    if keys[pygame.K_d]:
        x2 += speed2
        if (x2 > W * 2.5 -30):
            x2 = W * 2.5 -30

    sc.fill(WHITE)
    car_surf = pygame.image.load("myCarNew.png").convert()
    car_surf = pygame.transform.scale(car_surf, (car_surf.get_width() // 2.5, car_surf.get_height() // 2.5))
    car_rect = car_surf.get_rect(center=(x, y))
    car_surf.set_colorkey(WHITE)

    car_surf2 = pygame.image.load("car4.png").convert()
    car_surf2 = pygame.transform.scale(car_surf2, (car_surf.get_width() // 2, car_surf.get_height()))
    car_rect2 = car_surf.get_rect(center=(x2, y2))
    car_surf2.set_colorkey(WHITE)

    bg_surf = pygame.image.load("bg.png").convert()
    bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width() * 2, bg_surf.get_height() * 1.3))

    collideBalls()

    sc.blit(bg_surf, (0, 0))
    sc.blit(score, (-40,0))
    sc_text = f.render(str(game_score), 1,(94, 138, 14))
    sc_text2 = f.render(str(game_score2), 1,(94, 138, 14))
    sc.blit(sc_text2, (20, 50))
    sc.blit(sc_text, (150, 50))
    sc.blit(car_surf2, car_rect2)
    sc.blit(car_surf, car_rect)
    rocks.draw(sc)

    # pygame.draw.rect(sc, GREEN, (x, y, 10, 20))
    pygame.display.update()
    clock.tick(FPS)

    rocks.update(H)
