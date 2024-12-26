import pygame


class Maps:
    def map1(self):
        size = width, height = 500, 500
        screen = pygame.display.set_mode(size)
        screen.fill((255, 255, 0))
        return screen

    def map2(self):
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        return screen
