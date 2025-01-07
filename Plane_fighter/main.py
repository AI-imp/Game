# coding=utf-8
import pygame
import Role
import Operate
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Plane_fighter')
icon = pygame.image.load('./resource/ufo.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('./resourcebg.png')
player = pygame.image.load(
    './resource/player.png')
s=Operate.Operate()
font=pygame.font.Font('freesansbold.ttf',32)
def show_time():
    text=f'Time:{pygame.time.get_ticks()//1000}'
    Time_render=font.render(text,True,(0,255,0))
    screen.blit(Time_render,(20,40))
def show_score():
    text=f'Score:{s.score}'
    score_render=font.render(text,True,(0,255,0))
    screen.blit(score_render,(10,10))
def game_over():
    if pygame.time.get_ticks()>=10000:
        if s.score<60:
            text='Game Over'
            render=font.render(text,True,(255,0,0))
            screen.blit(render,(400,300))
            enemies.clear()
enemy_num=6
enemies=[]
for i in range(enemy_num):
    enemies.append(Role.Enemy())
def show_enemy():
    for j in enemies:
        screen.blit(j.img,(j.x,j.y))
        j.x+=j.step
        if(j.x>736 or j.x<0):
            j.step*=-1
            j.y += 10
bullets=[]
def show_bullet():
    #子弹及射中检测、效果
    for k in bullets:
        screen.blit(k.img,(k.x,k.y))
        k.y-=k.step
        if k.y<0:
            bullets.remove(k)
        for e in enemies:
            if (k.x-e.x)**2+(k.y-e.y)**2<900:
                bullets.remove(k)
                enemies.remove(e)
                s.score+=10
flag=True
while flag:
    screen.blit(bg, (0, 0))
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                Role.player1.player_step = 5
            elif event.key == pygame.K_LEFT:
                Role.player1.player_step = -5
            elif event.key == pygame.K_SPACE:
                bullets.append(Role.Bullet())
        if event.type == pygame.KEYUP:
            Role.player1.player_step = 0
            Role.player1.player_x += Role.player1.player_step
        if Role.player1.player_x > 736:
            Role.player1.player_x = 736
        if Role.player1.player_x < 0:
            Role.player1.player_x = 0
    screen.blit(player, (Role.player1.player_x, Role.player1.player_y))
    Role.player1.player_x += Role.player1.player_step
    show_enemy()
    show_bullet()
    show_time()
    game_over()
    pygame.display.update()



