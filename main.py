import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("my First Game")

x = 50
y = 50
width = 40
height = 60
speed = 5

loop = True

while loop:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_ESCAPE]:
        loop = False

    win.fill((0,0,0))
    pygame.draw.rect(win,(0,0,255),(x,y,width,height))

    pygame.display.update()

pygame.quit()