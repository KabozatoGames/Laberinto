import pygame, sys, glob, tmx
from pygame import*

h = 400
w = 800

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
pygame.display.set_caption("Pruebas	Pygame")	
def load_image(filename, transparent=False):	
#	Intentamos	cargar	la	imagen,	si	no	se	puede	
#	lanzamos	un	mensaje	de	error.	
		try:	image	=	pygame.image.load(filename)	
		except pygame.error,	message:	
					raise SystemExit,	message
#	Convertimos	la	imagen	al	tipo	interno	de	
#	Pygame	que	hace	que	sea	mucho	más	eficiente.	
		image	=	image.convert()	
#	Si	la	imagen	es	transparente,	tomamos	el		
#	color	de	su	esquina	superior	izquierda	y	lo	
#	definimos	como	color	transparente	de	la	imagen.	
		if transparent:	
					color	=	image.get_at((0,0))	
					image.set_colorkey(color,	RLEACCEL)	
		return image 

   
class player:
    def __init__(self):
            
       self.x = 200
       self.y = 300
            
       self.initialAnimSpeed = 10
       self.currentAnimSpeed = self.initialAnimSpeed
            
       self.anim1 = glob.glob("CaminandoAdelante/Caminando*.png")
       self.anim2 = glob.glob("CaminandoAtras/Caminando*.png")
       self.anim3 = glob.glob("CaminandoDerecha/Caminando*.png")
       self.anim4 = glob.glob("CaminandoIzquierda/Caminando*.png")
            
       self.anim1.sort()
       self.anim2.sort()
       self.anim3.sort()
       self.anim4.sort()
       
       self.animPosition = 0
       self.animMax1 = len(self.anim1) - 1
       self.animMax2 = len(self.anim2) - 1
       self.animMax3 = len(self.anim3) - 1
       self.animMax4 = len(self.anim4) - 1
       
       self.image = load_image(self.anim1[0],True)

       self.update(0) 
                 
    def update(self,pos):
       if pos != 0:
          self.currentAnimSpeed -= 1
          if event.type == KEYDOWN and event.key == K_UP: 
              self.y -= pos
          if event.type == KEYDOWN and event.key == K_DOWN:
              self.y += pos
          if event.type == KEYDOWN and event.key == K_RIGHT:
              self.x += pos
          if event.type == KEYDOWN and event.key == K_LEFT:
              self.x -= pos
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_UP:
             self.image = load_image(self.anim2[self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             if self.animPosition == self.animMax2:
                self.animPosition = 0
             else:
                self.animPosition += 1
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_DOWN:
             self.image = load_image(self.anim1[self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             if self.animPosition == self.animMax1:
                self.animPosition = 0
             else:
                self.animPosition += 1 
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_RIGHT:
             self.image = load_image(self.anim3[self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             if self.animPosition == self.animMax3:
                self.animPosition = 0
             else:
                self.animPosition += 1    
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_LEFT:
             self.image = load_image(self.anim4[self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             if self.animPosition == self.animMax4:
                self.animPosition = 0
             else:
                self.animPosition += 1                
       screen.blit(self.image,(self.x,self.y))            

      
#Se cambiaria coin por pildora 
#Se uso coin, porque era el objeto que teniamos mas completo (Imagen y sonido)

#class coin:
  #  def __init__(self):
        
   #     self.x = 200
    #    self.y = 350
     #   self.image = pygame.image.load("coin.png")

  #  def update(self):
   #     screen.blit(self.image,(self.x,self.y))




#coin1 = coin()
player1 = player()
position = 0

pygame.mixer.init()
pygame.mixer.music.load("ice_zone.mp3")
pygame.mixer.music.play(-1,0.0)




while 1:
    screen.fill((0,0,0))
    clock.tick(60)
    
    #Ideas para las pildoras y coleccionables
    
    #if player1.y == coin1.y:
        #effect = pygame.mixer.Sound("coin.ogg")
        #effect.play()
        #if coin1.y == 350:
        #    coin1.y = 250
        #elif coin1.y == 250:
        #    coin1.y = 350
        
    #else:
    #    coin1.update()   
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
            position = 1
            
        elif event.type == KEYUP and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
            position = 0
            player1.animPosition = 0
    player1.update(position)
        
    pygame.display.flip()       

