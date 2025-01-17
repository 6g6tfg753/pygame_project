import pygame
import copy
import maps


class Board:
    def __init__(self):
        self.start_flag = False
        pygame.init()
        self.board_list = []
        self.size_field = 900
        screen = maps.Maps.map_init(self, self.size_field)
        start_screen = pygame.display.set_mode((900, 900))

        font1 = pygame.font.Font(None, 24)
        btn_surface = pygame.Surface((150, 50))

        text = font1.render("START", True, (0, 0, 0))
        text_rect = text.get_rect(center=(btn_surface.get_width() / 2, btn_surface.get_height() / 2))

        btn_rect = pygame.Rect(350, 100, 300, 50)

        btn_surface.blit(text, text_rect)

        start_screen.blit(btn_surface, (btn_rect.x, btn_rect.y))

        pygame.display.update()

        while not self.start_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if btn_rect.collidepoint(event.pos):
                        self.start_flag = True
            pygame.draw.rect(btn_surface, (255, 255, 0), (1, 1, 148, 48))

            btn_surface.blit(text, text_rect)
            start_screen.blit(btn_surface, (btn_rect.x, btn_rect.y))
            pygame.display.update()
        self.render(screen)

    def can_go_down(self, coords):  # check if player can go down
        self.player.rect.x = coords[0]
        self.player.rect.y = coords[1] + 5
        if not pygame.sprite.spritecollide(self.player, self.boxes, dokill=False):
            return True
        return False

    def can_go_up(self, coords):  # check if player can go up
        self.player.rect.x = coords[0]
        self.player.rect.y = coords[1] - 5
        if not pygame.sprite.spritecollide(self.player, self.boxes, dokill=False):
            return True
        return False

    def can_go_right(self, coords):  # check if player can go right
        self.player.rect.x = coords[0] + 5
        self.player.rect.y = coords[1]
        if not pygame.sprite.spritecollide(self.player, self.boxes, dokill=False):
            return True
        return False

    def can_go_left(self, coords):  # check if player can go left
        self.player.rect.x = coords[0] - 5
        self.player.rect.y = coords[1]
        if not pygame.sprite.spritecollide(self.player, self.boxes, dokill=False):
            return True
        return False

    def add_util(self, height):
        if height > 5:
            return
        utilite = pygame.sprite.Sprite()
        utilite.image = pygame.image.load('maps/mine_mini.png')
        utilite.image.set_colorkey((251, 251, 251))
        utilite.rect = utilite.image.get_rect()
        utilite.rect.x, utilite.rect.y = 0, height * 30
        self.utils.add(utilite)

    def find_object_sprite(self, player):
        for el in self.objects.sprites():
            if pygame.sprite.spritecollide(player, [el], False):
                return el

    def render_init(self, screen):
        self.Size_im = 100  # size of the image (one cell)

        # flag of the game
        self.state_of_the_game = True

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.finish = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.utils = pygame.sprite.Group()
        self.end_of_the_game = pygame.sprite.Group()
        self.move_boxes = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()


        # player sprite
        sprite = pygame.sprite.Sprite(self.all_sprites)
        sprite.image = pygame.image.load('player/image_front1.png')
        sprite.image.set_colorkey((151, 151, 151))
        sprite.rect = sprite.image.get_rect()
        self.all_sprites.add(sprite)
        self.player = sprite

        # Generate field
        maps.Maps.field_init(self, self.level)
        #print(self.level)

        #Utils
        self.artefacts = 0
        self.killed_heroes = 0
        self.utils.draw(screen)

        screen.fill((90, 255, 127))  # green field
        self.all_sprites.draw(screen)
        pygame.display.flip()

    def render(self, screen):
        self.level = 0
        self.render_init(screen)
        size = (screen.get_size())
        coords = [0, 0]
        running = True
        flag_up = False
        flag_right = False
        flag_left = False
        flag_down = True

        while running:
            if self.state_of_the_game == False:
                pygame.time.wait(100)
                screen.fill((90, 255, 127))
                self.all_sprites.draw(screen)
                self.utils.draw(screen)
                self.end_of_the_game.draw(screen)
                pygame.display.flip()
            shooting_flag = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # exit
                    running = False
                key = pygame.key.get_pressed()
                if key[pygame.K_1]:  # restart
                    self.state_of_the_game = True
                    self.render_init(screen)
                    size = (screen.get_size())
                    coords = [0, 0]
                    flag_up = False
                    flag_right = False
                    flag_left = False
                    flag_down = True
                if key[pygame.K_2]:  # lower level
                    if self.level > 0:
                        self.level -= 0.5
                        self.state_of_the_game = True
                        self.render_init(screen)
                        size = (screen.get_size())
                        coords = [0, 0]
                        flag_up = False
                        flag_right = False
                        flag_left = False
                        flag_down = True
                if key[pygame.K_3]:  # higher level
                    if self.level < 4:
                        self.level += 0.5
                        self.state_of_the_game = True
                        self.render_init(screen)
                        size = (screen.get_size())
                        coords = [0, 0]
                        flag_up = False
                        flag_right = False
                        flag_left = False
                        flag_down = True
                if key[pygame.K_s] and coords[1] + self.Size_im < size[1] and self.can_go_down(coords) and self.state_of_the_game:
                    flag_down = True
                    pygame.time.wait(1)
                    screen.fill((90, 255, 127))
                    self.player.rect.x = coords[0]
                    self.player.rect.y = coords[1] + 5
                    coords[1] += 5
                    self.player.image = pygame.image.load('player/image_front1.png')
                    self.player.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    self.utils.draw(screen)
                    self.end_of_the_game.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_w] and coords[1] > 0 and self.can_go_up(coords) and self.state_of_the_game:
                    flag_up = True
                    pygame.time.wait(1)
                    screen.fill((90, 255, 127))
                    self.player.rect.x = coords[0]
                    self.player.rect.y = coords[1] - 5
                    coords[1] -= 5
                    self.player.image = pygame.image.load('player/image_back1.png')
                    self.player.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    self.utils.draw(screen)
                    self.end_of_the_game.draw(screen)
                    pygame.display.flip()
                    flag_down = False
                    flag_right = False
                    flag_left = False

                if key[pygame.K_d] and coords[0] < size[0] - self.Size_im and self.can_go_right(coords) and self.state_of_the_game:
                    flag_right = True
                    pygame.time.wait(1)
                    screen.fill((90, 255, 127))
                    self.player.rect.x = coords[0] + 5
                    self.player.rect.y = coords[1]
                    coords[0] += 5
                    self.player.image = pygame.image.load('player/image_right1.png')
                    self.player.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    self.utils.draw(screen)
                    self.end_of_the_game.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_left = False

                if key[pygame.K_a] and coords[0] > 0 and self.can_go_left(coords) and self.state_of_the_game:
                    flag_left = True
                    pygame.time.wait(1)
                    screen.fill((90, 255, 127))
                    self.player.rect.x = coords[0] - 5
                    self.player.rect.y = coords[1]
                    coords[0] -= 5
                    self.player.image = pygame.image.load('player/image_left1.png')
                    self.player.image.set_colorkey((151, 151, 151))
                    self.all_sprites.draw(screen)
                    self.utils.draw(screen)
                    self.end_of_the_game.draw(screen)
                    pygame.display.flip()
                    flag_up = False
                    flag_down = False
                    flag_right = False

                if pygame.sprite.spritecollide(self.player, self.move_boxes, dokill=False):
                    if flag_up:
                        print(3)
                        self.sprite_box.rect.y -= 10
                    if flag_down:
                        print(43242342)
                        self.sprite_box.rect.y += 10
                    if flag_right:
                        print(54)
                        self.sprite_box.rect.x += 10
                    if flag_left:
                        print(00)
                        self.sprite_box.rect.x -= 10


                if key[pygame.K_SPACE] and not shooting_flag and self.state_of_the_game:

                    shooting_flag = True
                    bullet_coords = [0, 0]
                    bullet_coords[0] = copy.deepcopy(coords[0] + 40)
                    bullet_coords[1] = copy.deepcopy(coords[1] + 40)

                    time_of_enemy_dying = 0
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
                            bullet_sprite.image = pygame.image.load('bullet/bullet_right.png')
                        if flag_down:
                            bullet_sprite.image = pygame.image.load('bullet/bullet_down.png')
                        if flag_up:
                            bullet_sprite.image = pygame.image.load('bullet/bullet_up.png')
                        if flag_left:
                            bullet_sprite.image = pygame.image.load('bullet/bullet_left.png')
                        bullet_sprite.image.set_colorkey((255, 255, 255))
                        bullet_sprite.rect = bullet_sprite.image.get_rect()
                        bullet_sprite.rect.x = bullet_coords[0]
                        bullet_sprite.rect.y = bullet_coords[1]
                        self.all_sprites.add(bullet_sprite)
                        screen.fill((90, 255, 127))
                        self.all_sprites.draw(screen)
                        self.utils.draw(screen)
                        self.end_of_the_game.draw(screen)
                        pygame.display.flip()
                        self.all_sprites.remove(bullet_sprite)

                        if pygame.sprite.spritecollide(bullet_sprite, self.boxes, dokill=False):
                            screen.fill((90, 255, 127))
                            self.all_sprites.draw(screen)
                            self.utils.draw(screen)
                            self.end_of_the_game.draw(screen)
                            pygame.display.flip()
                            break
                        if pygame.sprite.spritecollide(bullet_sprite, self.enemies, dokill=False):
                            killed_enemy = sprite1 = pygame.sprite.Sprite()
                            for el in self.enemies.sprites():
                                if el.rect.collidepoint(bullet_coords):
                                    killed_enemy = el
                                    killed_enemy.image = pygame.image.load('player/shield.png')
                                    killed_enemy.image.set_colorkey((126, 194, 210))

                            screen.fill((90, 255, 127))
                            self.all_sprites.draw(screen)
                            self.utils.draw(screen)
                            self.end_of_the_game.draw(screen)
                            pygame.display.flip()
                            time_of_enemy_dying += 1
                            if time_of_enemy_dying > 9:
                                self.all_sprites.remove(killed_enemy)
                                self.enemies.remove(killed_enemy)
                                self.killed_heroes += 1
                                break
                    screen.fill((90, 255, 127))
                    self.all_sprites.draw(screen)
                    self.utils.draw(screen)
                    self.end_of_the_game.draw(screen)
                    pygame.display.flip()

                    pygame.time.wait(300)

                end = pygame.sprite.Sprite()
                image_lose = pygame.image.load('maps/lose.png')
                image_win = pygame.image.load('maps/win.png')

                get_objects = pygame.sprite.spritecollide(self.player, self.objects, False)
                if get_objects and self.state_of_the_game:
                    obj = self.find_object_sprite(self.player)
                    self.all_sprites.remove(obj)
                    self.objects.remove(obj)
                    self.add_util(self.artefacts)
                    self.artefacts += 1

                end_of_the_game_flag = pygame.sprite.spritecollide(self.player, self.enemies, False)
                if end_of_the_game_flag and self.state_of_the_game:
                    end.image = image_lose
                    end.rect = end.image.get_rect()
                    end.rect.x, end.rect.y = 0, 200
                    self.end_of_the_game.add(end)
                    self.state_of_the_game = False
                end_of_the_game_flag = pygame.sprite.spritecollide(self.player, self.finish, False)
                if end_of_the_game_flag and self.state_of_the_game:
                    end.image = image_win
                    end.rect = end.image.get_rect()
                    end.rect.x, end.rect.y = 0, 200
                    self.end_of_the_game.add(end)
                    if self.level < 0:
                        self.level = 0
                    elif self.level > 4:
                        self.level = 0
                    else:
                        self.level += 1
                    self.state_of_the_game = False


b = Board()
