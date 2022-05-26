import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    snake = pygame.Surface((50, 50))
    snake.fill((0,0,0))
    screen.blit(snake, (50, 50))

    pygame.display.flip()

pygame.quit()