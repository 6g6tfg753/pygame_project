import pygame
import copy
import maps


class Board:
    def __init__(self):
        self.size_field = 900
        screen = maps.Maps.map3(self, self.size_field)
        self.render(screen)

    def can_go(self, all_sprites, coords, f_down, f_up, f_right, f_left):  # check if player can go
        a = all_sprites.sprites()
        for i in range(1, len(a)):
            # print(coords, a[i].rect.x, a[i].rect.y)
            if f_down:
                if a[i].rect.x - self.Size_im < coords[0] < a[i].rect.x + self.Size_im:
                    if coords[1] + self.Size_im >= a[i].rect.y and not (coords[1] >= a[i].rect.y + self.Size_im):
                        return False
            if f_up:
                if a[i].rect.x - self.Size_im < coords[0] < a[i].rect.x + self.Size_im:
                    if coords[1] <= a[i].rect.y + self.Size_im and not (coords[1] + self.Size_im <= a[i].rect.y):
                        return False
            if f_right:
                if a[i].rect.y - self.Size_im < coords[1] < a[i].rect.y + self.Size_im:
                    if coords[0] + self.Size_im >= a[i].rect.x and not (coords[0] >= a[i].rect.x + self.Size_im):
                        return False
            if f_left:
                if a[i].rect.y - self.Size_im < coords[1] < a[i].rect.y + self.Size_im:
                    if coords[0] <= a[i].rect.x + self.Size_im and not (coords[0] + self.Size_im <= a[i].rect.x):
                        return False
        return True

    def render(self, screen):
        self.Size_im = 100  # size of the image (one cell)
        all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = pygame.image.load('player/image_front1.png')
        sprite.image.set_colorkey((151, 151, 151))
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)

        # FIELD:
        # 1 - cage; 0 - empty cell
        map_9 = [[0, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 0],
                 [1, 0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 1, 1, 1, 1, 0]]
        for a in range(9):
            for b in range(9):
                if map_9[b][a] == 1:
                    sprite1 = pygame.sprite.Sprite(all_sprites)
                    sprite1.image = pygame.image.load('maps/box1.png')
                    sprite1.image.set_colorkey((151, 151, 151))
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    all_sprites.add(sprite1)

        size = (screen.get_size())
        coords = [0, 0]
        screen.fill((90, 255, 127))  # green field
        all_sprites.draw(screen)
        pygame.display.flip()
        running = True
        flag_up = False
        flag_right = False
        flag_left = False
        flag_down = True
        while running:
            shooting_flag = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                key = pygame.key.get_pressed()
                if key[pygame.K_s] and coords[1] + self.Size_im < size[1] and self.can_go(all_sprites, coords, 1, 0, 0,
                                                                                          0):
                    flag_down = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] + 10
                    coords[1] += 10
                    sprite.image = pygame.image.load('player/image_front1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_w] and coords[1] > 0 and self.can_go(all_sprites, coords, 0, 1, 0, 0):
                    flag_up = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] - 10
                    coords[1] -= 10
                    sprite.image = pygame.image.load('player/image_back1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_down = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_d] and coords[0] < size[0] - self.Size_im and self.can_go(all_sprites, coords, 0, 0, 1,
                                                                                          0):
                    flag_right = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0] + 10
                    sprite.rect.y = coords[1]
                    coords[0] += 10
                    sprite.image = pygame.image.load('player/image_right1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_left = False

                if key[pygame.K_a] and coords[0] > 0 and self.can_go(all_sprites, coords, 0, 0, 0, 1):
                    flag_left = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0] - 10
                    sprite.rect.y = coords[1]
                    coords[0] -= 10
                    sprite.image = pygame.image.load('player/image_left1.png')
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
