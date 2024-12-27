import pygame

import maps


class Board:
    def __init__(self):
        screen = maps.Maps.map2(self)
        self.render(screen)

    def render(self, screen):
        all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = pygame.image.load('image_front.png')
        sprite.image.set_colorkey((151, 151, 151))
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        coords = [0, 0]
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                key = pygame.key.get_pressed()
                if key[pygame.K_s]:
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] + 10
                    coords[1] += 10
                    sprite.image = pygame.image.load('image_front.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                if key[pygame.K_w]:
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] - 10
                    coords[1] -= 10
                    sprite.image = pygame.image.load('image_back.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                if key[pygame.K_d]:
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0] + 10
                    sprite.rect.y = coords[1]
                    coords[0] += 10
                    sprite.image = pygame.image.load('image_right.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                if key[pygame.K_a]:
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0] - 10
                    sprite.rect.y = coords[1]
                    coords[0] -= 10
                    sprite.image = pygame.image.load('image_left.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()


b = Board()
