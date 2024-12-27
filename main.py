import pygame
import copy
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
        size = (screen.get_size())
        coords = [0, 0]
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        running = True
        while running:
            shooting_flag = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                key = pygame.key.get_pressed()
                if key[pygame.K_s] and coords[1] + 185 < size[1]:
                    flag_down = True
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] + 10
                    coords[1] += 10
                    sprite.image = pygame.image.load('image_front.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_w] and coords[1] > 0:
                    flag_up = True
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] - 10
                    coords[1] -= 10
                    sprite.image = pygame.image.load('image_back.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_down = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_d] and coords[0] < size[0] - 185:
                    flag_right = True
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0] + 10
                    sprite.rect.y = coords[1]
                    coords[0] += 10
                    sprite.image = pygame.image.load('image_right.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_left = False

                if key[pygame.K_a] and coords[0] > 0:
                    flag_left = True
                    pygame.time.wait(100)
                    screen.fill((255, 255, 255))
                    sprite.rect.x = coords[0] - 10
                    sprite.rect.y = coords[1]
                    coords[0] -= 10
                    sprite.image = pygame.image.load('image_left.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_right = False

                if key[pygame.K_SPACE] and not shooting_flag:
                    shooting_flag = True
                    bullet_coords = [0, 0]
                    bullet_coords[0] = copy.deepcopy(coords[0] + 90)
                    bullet_coords[1] = copy.deepcopy(coords[1] + 90)

                    while -1 < bullet_coords[0] < size[1] and -1 < bullet_coords[1] < size[0]:
                        if flag_up:
                            bullet_coords[1] -= 10
                        if flag_down:
                            bullet_coords[1] += 10
                        if flag_right:
                            bullet_coords[0] += 10
                        if flag_left:
                            bullet_coords[0] -= 10
                        pygame.time.wait(1)
                        screen.fill((255, 255, 255))
                        all_sprites.draw(screen)

                        pygame.draw.rect(screen, (255, 0, 0), (bullet_coords[0], bullet_coords[1], 10, 10))
                        pygame.display.flip()
                    pygame.time.wait(300)


b = Board()
