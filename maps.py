import pygame


class Maps:
    def map1(self):
        size = width, height = 1000, 1000
        screen = pygame.display.set_mode(size)
        screen.fill((255, 255, 0))
        return screen

    def map2(self):
        size = width, height = 900, 900
        screen = pygame.display.set_mode(size)
        return screen

