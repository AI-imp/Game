# coding=utf-8
import random
import pygame
class Player():
    def __init__(self):
        self.player_x = 400
        self.player_y = 500
        self.player_step = 0
player1 = Player()
class Enemy():
    def __init__(self):
        self.img=pygame.image.load('./resource/enemy.png')
        self.x=random.randint(200,600)
        self.y=random.randint(50,100)
        self.step=random.randint(2,4)
class Bullet():
        def __init__(self):
            self.img = pygame.image.load(
                './resource/bullet.png')
            self.x = player1.player_x
            self.y = player1.player_y + 10
            self.step = 10




