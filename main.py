import pygame
import copy
import maps


class Enemy(pygame.sprite.Sprite):
    image = pygame.image.load('maps/enemy.png')
    image_dead = pygame.image.load('shield.png')
    image_dead.set_colorkey((126, 194, 210))

    def __init__(self, group, coords):
        super().__init__(group)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.group = group

    def update(self, point):
        if self.rect.collidepoint(point):
            self.image = self.image_dead


class Board:
    def __init__(self):
        self.board_list = []
        self.size_field = 900
        screen = maps.Maps.map3(self, self.size_field)
        self.render(screen)

    def can_go_down(self, coords):  # check if player can go down
        self.sprite.rect.x = coords[0]
        self.sprite.rect.y = coords[1] + 5
        if not pygame.sprite.spritecollide(self.sprite, self.boxes, dokill=False):
            return True
        return False

    def can_go_up(self, coords):  # check if player can go up
        self.sprite.rect.x = coords[0]
        self.sprite.rect.y = coords[1] - 5
        if not pygame.sprite.spritecollide(self.sprite, self.boxes, dokill=False):
            return True
        return False

    def can_go_right(self, coords):  # check if player can go right
        self.sprite.rect.x = coords[0] + 5
        self.sprite.rect.y = coords[1]
        if not pygame.sprite.spritecollide(self.sprite, self.boxes, dokill=False):
            return True
        return False

    def can_go_left(self, coords):  # check if player can go left
        self.sprite.rect.x = coords[0] - 5
        self.sprite.rect.y = coords[1]
        if not pygame.sprite.spritecollide(self.sprite, self.boxes, dokill=False):
            return True
        return False

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
        self.sprite = sprite

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
        for i in range(9):
            for k in range(9):
                if self.board_list[i][k] == 3:
                    a = Enemy(self.all_sprites, (i * 100, k * 100))

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
                    sprite.rect.y = coords[1] + 5
                    coords[1] += 5
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
                    sprite.rect.y = coords[1] - 5
                    coords[1] -= 5
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
                    sprite.rect.x = coords[0] + 5
                    sprite.rect.y = coords[1]
                    coords[0] += 5
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
                    sprite.rect.x = coords[0] - 5
                    sprite.rect.y = coords[1]
                    coords[0] -= 5
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
                    bullet_coords[0] = copy.deepcopy(coords[0] + 40)
                    bullet_coords[1] = copy.deepcopy(coords[1] + 40)

                    while -1 < bullet_coords[0] < size[1] and -1 < bullet_coords[1] < size[0]:

                        self.all_sprites.update(bullet_coords)

                        if flag_up:
                            bullet_coords[1] -= 10
                        if flag_down:
                            bullet_coords[1] += 10
                        if flag_right:
                            bullet_coords[0] += 10
                        if flag_left:
                            bullet_coords[0] -= 10
                        pygame.time.wait(20)
                        screen.fill((90, 255, 127))

                        bullet_sprite = pygame.sprite.Sprite(self.all_sprites)
                        if flag_right:
                            bullet_sprite.image = pygame.image.load('bullet_right.png')
                        if flag_down:
                            bullet_sprite.image = pygame.image.load('bullet_down.png')
                        if flag_up:
                            bullet_sprite.image = pygame.image.load('bullet_up.png')
                        if flag_left:
                            bullet_sprite.image = pygame.image.load('bullet_left.png')
                        bullet_sprite.image.set_colorkey((255, 255, 255))
                        bullet_sprite.rect = bullet_sprite.image.get_rect()
                        bullet_sprite.rect.x = bullet_coords[0]
                        bullet_sprite.rect.y = bullet_coords[1]
                        self.all_sprites.add(bullet_sprite)
                        screen.fill((90, 255, 127))
                        self.all_sprites.draw(screen)
                        pygame.display.flip()
                        self.all_sprites.remove(bullet_sprite)

                        if pygame.sprite.spritecollide(bullet_sprite, self.boxes, dokill=False):
                            screen.fill((90, 255, 127))
                            self.all_sprites.draw(screen)
                            pygame.display.flip()
                            break
                    screen.fill((90, 255, 127))
                    self.all_sprites.draw(screen)
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
