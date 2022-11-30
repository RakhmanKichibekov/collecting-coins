import pygame

from ball import Ball
from random import randint
from bomb import Bomb

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 4000)
W, H = 600, 400
sc = pygame.display.set_mode((W, H), pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("Game of the year by Rakhman")
pygame.display.set_icon(pygame.image.load("pictures/car.png"))
pygame.mixer.music.load("musics/musicBg.mp3")
pygame.mixer.music.play(-1)
music1 = pygame.mixer.Sound("musics/musicMoney.mp3")

PURPLE = (255, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

score = pygame.image.load("pictures/check.png").convert()
score = pygame.transform.scale(score, (score.get_width() // 2.5, score.get_height() // 2.5))
score.set_colorkey(WHITE)
f = pygame.font.SysFont('arial', 100)

win = pygame.image.load("pictures/win2.png").convert()
win = pygame.transform.scale(win, (win.get_width(), win.get_height()))
win.set_colorkey(WHITE)
w = pygame.font.SysFont('arial', 70)

pygame.display.update()
FPS = 60  # Кадров в секунду
clock = pygame.time.Clock()

rocks_image = ['coin.png', 'coin2.png']
rocks_surf = [pygame.image.load('pictures/' + path).convert() for path in rocks_image]


def createRock(group):
    indx = randint(0, len(rocks_surf) - 1)
    x = randint(20, W * 3 - 20)
    speed = randint(5, 12)
    return Ball(x, 0, rocks_surf[indx], speed, group)


def createBomb(group1):
    x = randint(20, W * 3 - 20)
    speed = randint(3, 5)
    return Bomb(x, 0, speed, group1)


game_score = 0  # счёт синей машинки
game_score2 = 0  # счёт красной машинки
general_score = 10 #счёт для победы


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
pygame.display.update()

rocks = pygame.sprite.Group()
bombs = pygame.sprite.Group()

x2 = W // 1.1
y2 = H * 1.5
speed = 12

x = W * 1.5
y = H * 1.5
speed2 = 10

speed3 = 2.3
bush = 0
createRock(rocks)
createBomb(bombs)
print("правление синей машинкой WASD\n"
      "красной стрелки")

flRun = True
while flRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRun = False
        elif event.type == pygame.USEREVENT and (game_score < general_score and game_score2 < general_score) \
                and bush == 0:
            createRock(rocks)
            createBomb(bombs)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
        if (x < 0):
            x = 0
    if keys[pygame.K_RIGHT]:
        x += speed
        if (x > W * 2.5 - 30):
            x = W * 2.5 - 30
    if keys[pygame.K_UP]:
        y -= speed
        if (y <= 100):
            y = 100
    if keys[pygame.K_DOWN]:
        y += speed
        if (y >= 650):
            y = 650
    if keys[pygame.K_a]:
        x2 -= speed2
        if (x2 < 100):
            x2 = 100
    if keys[pygame.K_w]:
        y2 -= speed2
        if (y2 <= 100):
            y2 = 100
    if keys[pygame.K_s]:
        y2 += speed2
        if (y2 >= 650):
            y2 = 650
    if keys[pygame.K_d]:
        x2 += speed2
        if (x2 > W * 2.5 - 30):
            x2 = W * 2.5 - 30

    car_surf = pygame.image.load("pictures/myCarNew.png").convert()
    car_surf = pygame.transform.scale(car_surf, (car_surf.get_width() // 2.5, car_surf.get_height() // 2.5))
    car_rect = car_surf.get_rect(center=(x, y))
    car_surf.set_colorkey(WHITE)

    car_surf2 = pygame.image.load("pictures/car4.png").convert()
    car_surf2 = pygame.transform.scale(car_surf2, (car_surf.get_width()*1.3, car_surf.get_height()))
    car_rect2 = car_surf.get_rect(center=(x2, y2))
    car_surf2.set_colorkey(WHITE)

    bg_surf = pygame.image.load("pictures/bg.png").convert()
    bg_surf = pygame.transform.scale(bg_surf, (bg_surf.get_width() * 2, bg_surf.get_height() * 1.3))

    collideBalls()

    sc.blit(bg_surf, (0, 0))
    sc.blit(score, (-40, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc_text2 = f.render(str(game_score2), 1, (94, 138, 14))
    sc.blit(sc_text2, (20, 50))
    sc.blit(sc_text, (150, 50))
    sc.blit(car_surf2, car_rect2)
    sc.blit(car_surf, car_rect)
    rocks.draw(sc)
    bombs.draw(sc)
    if (game_score >= general_score):
        sc.blit(win, (350, 20))
        sc_text3 = w.render("Победил красный", 1, (94, 138, 14))
        sc.blit(sc_text3, (520, 350))
        for rock in rocks:
            rock.kill()
        for bomb in bombs:
            bomb.kill()

    elif (game_score2 == general_score):
        sc.blit(win, (350, 20))
        sc_text3 = w.render(str('Победил синий'), 1, (94, 138, 14))
        sc.blit(sc_text3, (520, 350))
        for rock in rocks:
            rock.kill()
        for bomb in bombs:
            bomb.kill()
    for bomb in bombs:
        if car_rect.collidepoint(bomb.rect.center):
            sc.blit(win, (350, 20))
            sc_text3 = w.render(str('Красный взорвался'), 1, (94, 138, 14))
            sc.blit(sc_text3, (520, 350))
            bush = 1
        elif car_rect2.collidepoint(bomb.rect.center):
            sc.blit(win, (350, 20))
            sc_text3 = w.render(str('Синий взорвался'), 1, (94, 138, 14))
            sc.blit(sc_text3, (520, 350))
            bush = 1
    pygame.display.update()
    clock.tick(FPS)

    rocks.update(H)
    bombs.update(H)
