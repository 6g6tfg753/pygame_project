import pygame
import copy
import maps



class Board:
    def __init__(self):
        self.size_field = 900
        screen = maps.Maps.map3(self, self.size_field)
        self.render(screen)

    def can_go_down(self, coords):  # check if player can go down
        a = self.boxes.sprites()
        for i in range(len(a)):
            if a[i].rect.x - self.Size_im < coords[0] < a[i].rect.x + self.Size_im:
                if coords[1] + self.Size_im >= a[i].rect.y and not (coords[1] >= a[i].rect.y + self.Size_im):
                    return False
        return True
    def can_go_up(self, coords):  # check if player can go up
        a = self.boxes.sprites()
        for i in range(len(a)):
            if a[i].rect.x - self.Size_im < coords[0] < a[i].rect.x + self.Size_im:
                if coords[1] <= a[i].rect.y + self.Size_im and not (coords[1] + self.Size_im <= a[i].rect.y):
                    return False
        return True
    def can_go_right(self, coords):  # check if player can go right
        a = self.boxes.sprites()
        for i in range(len(a)):
            if a[i].rect.y - self.Size_im < coords[1] < a[i].rect.y + self.Size_im:
                if coords[0] + self.Size_im >= a[i].rect.x and not (coords[0] >= a[i].rect.x + self.Size_im):
                    return False
        return True
    def can_go_left(self, coords):  # check if player can go left
        a = self.boxes.sprites()
        for i in range(len(a)):
            if a[i].rect.y - self.Size_im < coords[1] < a[i].rect.y + self.Size_im:
                if coords[0] <= a[i].rect.x + self.Size_im and not (coords[0] + self.Size_im <= a[i].rect.x):
                    return False
        return True

    def render(self, screen):
        self.Size_im = 100  # size of the image (one cell)
        self.all_sprites = pygame.sprite.Group()  # to draw
        self.finish = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()

        sprite = pygame.sprite.Sprite(self.all_sprites)
        sprite.image = pygame.image.load('player/image_front1.png')
        sprite.image.set_colorkey((151, 151, 151))
        sprite.rect = sprite.image.get_rect()
        self.all_sprites.add(sprite)

        maps.Maps.field_init(self, 0)

        size = (screen.get_size())
        coords = [0, 0]
        screen.fill((90, 255, 127))  # green field
        self.all_sprites.draw(screen)
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
                if key[pygame.K_s] and coords[1] + self.Size_im < size[1] and self.can_go_down(coords):
                    flag_down = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] + 10
                    coords[1] += 10
                    sprite.image = pygame.image.load('player/image_front1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_w] and coords[1] > 0 and self.can_go_up(coords):
                    flag_up = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0]
                    sprite.rect.y = coords[1] - 10
                    coords[1] -= 10
                    sprite.image = pygame.image.load('player/image_back1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_down = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_d] and coords[0] < size[0] - self.Size_im and self.can_go_right(coords):
                    flag_right = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0] + 10
                    sprite.rect.y = coords[1]
                    coords[0] += 10
                    sprite.image = pygame.image.load('player/image_right1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_left = False

                if key[pygame.K_a] and coords[0] > 0 and self.can_go_left(coords):
                    flag_left = True
                    pygame.time.wait(100)
                    screen.fill((90, 255, 127))
                    sprite.rect.x = coords[0] - 10
                    sprite.rect.y = coords[1]
                    coords[0] -= 10
                    sprite.image = pygame.image.load('player/image_left1.png')
                    sprite.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
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
                        screen.fill((90, 255, 127))
                        self.all_sprites.draw(screen)

                        pygame.draw.rect(screen, (255, 0, 0), (bullet_coords[0], bullet_coords[1], 10, 10))
                        pygame.display.flip()
                    pygame.time.wait(300)

                end_of_the_game = pygame.sprite.spritecollide(sprite, self.enemies, False)
                if end_of_the_game:
                    pygame.time.wait(1000)
                    running = False
                end_of_the_game = pygame.sprite.spritecollide(sprite, self.finish, False)
                if end_of_the_game:
                    pygame.time.wait(1000)
                    running = False


b = Board()
