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

    def map3(self, w, h=0):
        if h == 0:
            h = w
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        return screen

    def field_init(self, level):
        if level == 1:
        # 1 - cage; 0 - empty cell; -1 - finish; 2 -weapon; 3 - enemy, 4 - dead enemy
            map_9 = [[0, 0, 1, 0, 0, 0, 1, 0, 1],
                     [1, 0, 0, 0, 1, 0, 0, 0, 0],
                     [1, 0, 1, 0, 1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0, 1, 1, 0, 0],
                     [1, 0, 1, 1, 0, 0, 1, 0, 1],
                     [0, 0, 1, 1, 1, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 0, 1, 0, 0],
                     [1, 0, 1, 1, 1, 1, 1, 1, -1]]
        elif level == 2:
            map_9 = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 1, 1, 1, 1, 0],
                     [0, 1, 1, 0, 1, 1, 1, 1, 0],
                     [0, 0, 1, 0, 0, 0, 0, 1, 0],
                     [0, 1, 1, 0, 1, 1, 0, 1, 0],
                     [0, 0, 1, 0, 1, 0, 0, 1, 0],
                     [0, 1, 1, 0, 1, 0, 0, 1, 0],
                     [0, 1, 0, 0, 1, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 1, 1, 1, -1]]
        else:
            map_9 = [[0, 0, 1, 2, 0, 0, 0, 0, 3],
                     [0, 0, 0, 1, 1, 1, 0, 1, 0],
                     [0, 1, 0, 0, 1, 1, 0, 1, 0],
                     [0, 1, 1, 0, 0, 1, 0, 1, 0],
                     [0, 1, 2, 1, 0, 0, 0, 1, 0],
                     [0, 1, 0, 1, 0, 1, 0, 1, 2],
                     [0, 1, 0, 1, 0, 1, 0, 0, 1],
                     [0, 1, 0, 1, 0, 1, 1, 0, 0],
                     [3, 0, 0, 0, 0, 1, 1, 1, -1]]

        for a in range(9):
            for b in range(9):
                if map_9[b][a] == 1:
                    sprite1 = pygame.sprite.Sprite(self.all_sprites)
                    sprite1.image = pygame.image.load('maps/box1.png')
                    sprite1.image.set_colorkey((151, 151, 151))
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    self.all_sprites.add(sprite1)
                    self.boxes.add(sprite1)
                if map_9[b][a] == -1:
                    sprite1 = pygame.sprite.Sprite(self.all_sprites)
                    sprite1.image = pygame.image.load('maps/finish.png')
                    sprite1.image.set_colorkey((151, 151, 151))
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    self.all_sprites.add(sprite1)
                    self.finish.add(sprite1)
                if map_9[b][a] == 2:
                    sprite1 = pygame.sprite.Sprite(self.all_sprites)
                    sprite1.image = pygame.image.load('maps/mine.png')
                    sprite1.image.set_colorkey((151, 151, 151))
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    self.all_sprites.add(sprite1)
                    self.objects.add(sprite1)


        if self.board_list:
            map_9 = self.board_list
        self.board_list = map_9
