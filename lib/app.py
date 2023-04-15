import random
import pygame
import curses
from curses import wrapper

pygame.init()

window_x = 800
window_y = 600


game_window = pygame.display.set_mode((window_x, window_y))

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    game_window.fill((0,0,0))

    pygame.draw.rect(game_window, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

# def main(stdscr):
#     stdscr.clear()
#     stdscr.addstr('hello world')
#     stdscr.refresh()
#     stdscr.getch()

# wrapper(main)
