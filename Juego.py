
import pygame, sys, glob, pytmx, Mapa ,random
from pygame import*
from pytmx.util_pygame import*


h = 600
w = 1200



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
            
       self.initialAnimSpeed = 5
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
   
#class coin:
  #  def __init__(self):
        
   #     self.x = 200
    #    self.y = 350
     #   self.image = pygame.image.load("coin.png")

  #  def update(self):
   #     screen.blit(self.image,(self.x,self.y))

class Enemy:
	def __init__(self):
		
               #se deben poner las imagenes del perro
	       self.x1 = 300
	       self.y2 = 400
              
	       self.initialAnimSpeed = 5
	       self.currentAnimSpeed = self.initialAnimSpeed
		#importante
               #se cambiaria las imagenes
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
	def updateIA(self,pos):
		if pos != 0:
			#faltan las raices
			xy = x*x + y*y
			xy1 = x1*x1 + y1*y1
			if(xy1 - xy == 25):
				while(x != x1):
					if(x - x1 < 0):
						x1 = x1 - 1
						if(#aqui iria si no pudiera moverse):
							#nose como sera la clase pared 3:
							
					if(x - x1 > 0):
						x1 = x1 + 1
						if(#aqui iria si no pudiera moverse):
				while(y != y1):
					if(y - y1 < 0):
						y1 = y1 - 1
						if(#aqui iria si no pudiera moverse):
					if(y - y1 > 0):
						y1 = y1 + 1
						if(#aqui iria si no pudiera moverse):

			else:
				o = random.randrange(1,4)
				#faltan las funciones para que no choque
				if(o = 1):
					x1 = x1 + 5
				if(o = 2):
					x1 = x1 - 5
				if(o = 3):
					y1 = y1 + 5
				if(o = 4):
					y1 = y1 - 5


#coin1 = coin()
player1 = player()
Enemy1 = Enemy()
position = 0

pygame.mixer.init()
pygame.mixer.music.load("ice_zone.mp3")
pygame.mixer.music.play(-1,0.0)




while 1:
    screen.fill((0,0,0))
    clock.tick(30)
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
            position = 5
            
        elif event.type == KEYUP and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
            position = 0
            player1.animPosition = 0

    Mapa.render_tiles_to_screen("Mapa1.tmx") 
    player1.update(position)
    pygame.display.flip()       
