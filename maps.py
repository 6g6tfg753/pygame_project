import pygame


class Maps:
    def map_init(self, w, h=0):
        if h == 0:
            h = w
        size = width, height = w, h
        screen = pygame.display.set_mode(size)
        return screen

    def field_init(self, level):
        level = int(level)
        map_9 = []
        # 1 - cage; 0 - empty cell; -1 - finish; 2 -weapon; 3 - enemy, 4 - move_box, 5 - button
        if level == 1:
            file = open('maps/levels/level1.txt', 'r').readlines()
        elif level == 2:
            file = open('maps/levels/level2.txt', 'r').readlines()
        elif level == 3:
            file = open('maps/levels/level3.txt', 'r').readlines()
        elif level == 4:
            file = open('maps/levels/level4.txt', 'r').readlines()
        else:
            file = open('maps/levels/level0.txt', 'r').readlines()
        for el in file:
            mas = [int(x) for x in el[1:-3].split(", ")]
            map_9.append(mas)

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
                if map_9[b][a] == 3:
                    sprite1 = pygame.sprite.Sprite(self.enemies)
                    sprite1.image = pygame.image.load('maps/enemy.png')
                    sprite1.image.set_colorkey((151, 151, 151))
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    self.enemies.add(sprite1)
                    self.all_sprites.add(sprite1)
                if map_9[b][a] == 4:
                    sprite_box = pygame.sprite.Sprite(self.all_sprites)
                    sprite_box.image = pygame.image.load('maps/box_move.png')
                    sprite1.image.set_colorkey((221, 221, 221))
                    sprite_box.rect = sprite_box.image.get_rect()
                    sprite_box.rect.x = a * 100
                    sprite_box.rect.y = b * 100
                    self.move_boxes.add(sprite_box)
                    self.sprite_box = sprite_box


                if map_9[b][a] == 5:
                    sprite1 = pygame.sprite.Sprite(self.all_sprites)
                    sprite1.image = pygame.image.load('maps/button.png')
                    sprite1.rect = sprite1.image.get_rect()
                    sprite1.rect.x = self.Size_im * a
                    sprite1.rect.y = self.Size_im * b
                    self.buttons.add(sprite1)
                    self.all_sprites.add(sprite1)
