import pygame
import time

pygame.init()
screen =  pygame.display.set_mode((1200, 675))

pygame.display.set_caption("White Samurai game")
icon = pygame.image.load('image/samurai_IMG.png')
pygame.display.set_icon(icon)


player = pygame.image.load('heroe/нач.png')

background_image = pygame.image.load('image/background.jpg')
walk_heroe = [
    pygame.image.load('heroe/нач.png'),
    pygame.image.load('heroe/прямая.png'),
    pygame.image.load('heroe/чуть согнута.png'),
    pygame.image.load('heroe/наступает.png'),
    pygame.image.load('heroe/наступил.png')
]

player_anim_count = 0
animate_bg = 0

runing = True
while runing:
    
    screen.blit(background_image, (animate_bg, 0))
    screen.blit(background_image, (animate_bg + 1200, 0))
    screen.blit(walk_heroe[player_anim_count], (0, 110))
    pygame.display.update()

    if player_anim_count == 4:
        player_anim_count = 0 
    else:
        player_anim_count += 1
        time.sleep(0.1)

    animate_bg -= 5
    if animate_bg == -1200:
        animate_bg = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
        



