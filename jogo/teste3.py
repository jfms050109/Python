import pygame
import random
from sys import exit
re =False
n=0
while True:
    #declaração de classes:

    class enty():
        def __init__(self,img_i,vel=1,x=0,y=0):
            self.x=x
            self.y=y
            self.img_b=pygame.image.load(img_i)
            self.vel=vel
        def desenhar(self):
            if self.x-int(self.img_b.get_size()[0]) < 0-int(self.img_b.get_size()[0]): self.x+=self.vel

            if self.y-int(self.img_b.get_size()[1]) < 0-int(self.img_b.get_size()[1]): self.y+=self.vel

            if self.x+int(self.img_b.get_size()[0]) > int(pygame.display.Info().current_w): self.x-=self.vel

            if self.y +int(self.img_b.get_size()[0]) > int(pygame.display.Info().current_h): self.y-=self.vel

            tela.blit(self.img_b,(self.x,self.y))
        def vk(self): #verify key

            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                self.y+=self.vel
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                self.y-=self.vel
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                self.x-=self.vel
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.x+=self.vel
            if pygame.key.get_pressed()[pygame.K_DELETE] or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()
            if pygame.key.get_pressed()[pygame.K_F1]:
                self.vel=int(input())
        def checar_colisão(self,obj):
                    if obj.x + int(obj.img_b.get_size()[0])> self.x and obj.x - int(obj.img_b.get_size()[0])< self.x and obj.y + int(obj.img_b.get_size()[1])> self.y and obj.y - int(obj.img_b.get_size()[1])< self.y:
                        global re
                        re=True
        def movimentar(self,obj):
            if self.x>obj.x:self.x-=self.vel
            if self.x<obj.x:self.x+=self.vel
            if self.y>obj.y:self.y-=self.vel
            if self.y<obj.y:self.y+=self.vel
            







    pygame.init()

    tela = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h),pygame.RESIZABLE)

    clock=pygame.time.Clock()

    pygame.display.set_caption('animação procedural')



    fundo=pygame.Surface((8000,8000))
    fundo.fill('black')

    #Entidades e componentes:
    b1=enty('bola.png',4)
    i1=[]
    for i in range(random.randrange(2,5)):
        obj=enty('bola.png',1,random.randrange(0,pygame.display.Info().current_w),random.randrange(0,pygame.display.Info().current_h))
        i1.append(obj)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        #desenhar os elementos
            

        #atualizar os eventos
        tela.blit(fundo,(0,0))
        b1.vk()
        b1.desenhar()
        n+=1
        for i in i1:
            i.desenhar()
            i.checar_colisão(b1)
            if n>120:
                for e in range(2):
                    obj=enty('bola.png',random.randrange(1,b1.vel-1),random.randrange(0,pygame.display.Info().current_w),random.randrange(0,pygame.display.Info().current_h))
                    i1.append(obj)
                    n=0
                
            i.movimentar(b1)
        
        #pygame.display.set_caption("x="+str(x)+", y="+str(y))
        
        #atualizar a tela
        pygame.display.update()
        if re:break
        clock.tick(60)
    if re: re=False
    else:exit()
        