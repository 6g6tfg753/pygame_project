import pygame
import maps


class Board:
    def __init__(self):
        screen = maps.Maps.map2(self)
        self.render(screen)

    def render(self, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    pygame.display.flip()


b = Board()
