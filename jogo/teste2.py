import pygame
import pyautogui
from sys import exit
vel=9
i=0
i2=0
pygame.init()
foi=False
foi2=False
x,y=(0,0)
x1,y1=(0,0)
x2,y2=(0,0)
tela = pygame.display.set_mode((800,400),pygame.RESIZABLE)
clock=pygame.time.Clock()
pygame.display.set_caption('animação procedural')
bola=pygame.image.load('bola.png')
"""bola1=pygame.image.load('bola.png')
bola2=pygame.image.load('bola.png')"""
fundo=pygame.Surface((8000,8000))
fundo.fill('black')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #desenhar os elementos
        

    #atualizar os eventos
    tela.blit(fundo,(0,0))
    tela.blit(bola,(x,y-24))
    tela.blit(bola,(x1,y1-24))
    tela.blit(bola,(x2,y2-24))
    
    x_mouse,y_mouse=pyautogui.position()
    if x>x_mouse:x-=vel
    if x<x_mouse:x+=vel
    if y>y_mouse:y-=vel
    if y<y_mouse:y+=vel
    print(i)
    if i>=16/vel*1.5:
        posx=x
        posy=y
        i=0
        foi=True
        print('chegou aqui')
    if foi:
        if x1!=posx or y1!=posy:
            print('chegou aqui1')
            if x1>posx:x1-=vel
            if x1<posx:x1+=vel
            if y1>posy:y1-=vel
            if y1<posy:y1+=vel
        if i2>=16/vel*1.5:
            pos1x=x1
            pos1y=y1
            i2=0
            foi2=True
            print('chegou aqui')
        if foi2:
            if x2!=pos1x or y2!=pos1y:
                print('chegou aqui1')
                if x2>pos1x:x2-=vel
                if x2<pos1x:x2+=vel
                if y2>pos1y:y2-=vel
                if y2<pos1y:y2+=vel
        i2+=1
    
    pygame.display.set_caption("x="+str(x)+", y="+str(y))
    
    #atualizar a tela
    pygame.display.update()
    i+=1
    clock.tick(60)
    