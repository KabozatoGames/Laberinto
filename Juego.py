
import pygame, sys, glob, pytmx, Mapa, random
from pygame.locals import*
from pygame import*
from pytmx.util_pygame import*

w = 1200
h = 600

posx = 0
posy = 0 


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
            
       self.x = 0
       self.y = 0
       self.dir = 0   
       
       self.initialAnimSpeed = 2
       self.currentAnimSpeed = self.initialAnimSpeed
       
       self.anim = [0,0,0,0]
       
       
       self.anim[0] = glob.glob("CaminandoAdelante/Caminando*.png")
       self.anim[1] = glob.glob("CaminandoAtras/Caminando*.png")
       self.anim[2] = glob.glob("CaminandoDerecha/Caminando*.png")
       self.anim[3] = glob.glob("CaminandoIzquierda/Caminando*.png")
            
       self.anim[0].sort()
       self.anim[1].sort()
       self.anim[2].sort()
       self.anim[3].sort()
       
       self.animPosition = 0
       self.animMax1 = len(self.anim[0]) - 1
       self.animMax2 = len(self.anim[1]) - 1
       self.animMax3 = len(self.anim[2]) - 1
       self.animMax4 = len(self.anim[3]) - 1
       
       self.image = load_image(self.anim[0][0],True)
       self.rect = self.image.get_rect()
       self.rect.centerx = 600
       self.rect.centery = 300
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
             self.image = load_image(self.anim[1][self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             self.dir = 1
             if self.animPosition == self.animMax2:
                self.animPosition = 0
             else:
                self.animPosition += 1
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_DOWN:
             self.image = load_image(self.anim[0][self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             self.dir = 0
             if self.animPosition == self.animMax1:
                self.animPosition = 0
             else:
                self.animPosition += 1 
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_RIGHT:
             self.image = load_image(self.anim[2][self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             self.dir = 2
             if self.animPosition == self.animMax3:
                self.animPosition = 0
             else:
                self.animPosition += 1    
          if self.currentAnimSpeed == 0 and event.type == KEYDOWN and event.key == K_LEFT:
             self.image = load_image(self.anim[3][self.animPosition],True)
             self.currentAnimSpeed = self.initialAnimSpeed
             self.dir = 3
             if self.animPosition == self.animMax4:
                self.animPosition = 0
             else:
                self.animPosition += 1    
       else:
           if self.animPosition != 0:
               self.animPosition = 0
           self.image = load_image(self.anim[self.dir][self.animPosition],True)
           
       screen.blit(self.image,(600,300))            

class Enemy:
	def __init__(self):

	       self.x1 = 300
	       self.y1 = 300
	       self.dir = 0              
	       self.initialAnimSpeed = 2
	       self.currentAnimSpeed = self.initialAnimSpeed
               
          
	       self.anim = [0,0,0,0]  
               
	       self.anim[0] = glob.glob("Enemy/Perro/Adelante/Perro*.png")
	       self.anim[1] = glob.glob("Enemy/Perro/Atras/Perro*.png")
	       self.anim[2] = glob.glob("Enemy/Perro/Derecha/Perro*.png")
	       self.anim[3] = glob.glob("Enemy/Perro/Izquierda/Perro*.png")
            
	       self.anim[0].sort()
	       self.anim[1].sort()
	       self.anim[2].sort()
	       self.anim[3].sort()
       
	       self.animPosition = 0
	       self.animMax1 = len(self.anim[0]) - 1
	       self.animMax2 = len(self.anim[1]) - 1
	       self.animMax3 = len(self.anim[2]) - 1
	       self.animMax4 = len(self.anim[3]) - 1
       
	       self.image = load_image(self.anim[0][0],True)
	       self.rect = self.image.get_rect()
	       self.rect.centerx = 300
	       self.rect.centery = 400
	       self.updateIA(self.x1,self.y1)
	def updateIA(self,playerx,playery):
                self.currentAnimSpeed -= 1
                distancia = ((self.x1 - (600 + playerx))**2 + (self.y1 - (300 + playery))**2)**(0.5)
		if(cont1 != 1):
			if(distancia <= 300):
                    		if((600 + playerx) != self.x1):
                        		if((600 + playerx) - self.x1 < 0):
                            			self.x1 = (self.x1 - 4)
                            			self.image = load_image(self.anim[3][self.animPosition],True)
                           			self.currentAnimSpeed = self.initialAnimSpeed
                           			if self.animPosition == self.animMax2:
                                			self.animPosition = 0
                           			else:
                                			self.animPosition += 1
                            			#if(#aqui iria si no pudiera moverse):
						#nose como sera la clase pared 3:
						
                        		if((600 + playerx) - self.x1 > 0):
                            			self.x1 = (self.x1 + 4)
                            			self.image = load_image(self.anim[2][self.animPosition],True)
                            			self.currentAnimSpeed = self.initialAnimSpeed
                            			if self.animPosition == self.animMax2:
                                			self.animPosition = 0
                            			else:
                                			self.animPosition += 1
                            			#if(#aqui iria si no pudiera moverse):            
                    		if((300 + playery) != self.y1):
                        		if((300 + playery) - self.y1 < 0):
                           			self.y1 = (self.y1 - 4)
                            			self.image = load_image(self.anim[1][self.animPosition],True)
                            			self.currentAnimSpeed = self.initialAnimSpeed
                            			if self.animPosition == self.animMax2:
                                			self.animPosition = 0
                            			else:
                                			self.animPosition += 1
                            			#if(#aqui iria si no pudiera moverse):
                        		if((300 + playery) - self.y1 > 0):
                            			self.y1 = (self.y1 + 4)
                            			self.image = load_image(self.anim[0][self.animPosition],True)
                            			self.currentAnimSpeed = self.initialAnimSpeed
                            			if self.animPosition == self.animMax2:
                                			self.animPosition = 0
                            			else:
                                			self.animPosition += 1
                                		#if(#aqui iria si no pudiera moverse):
                	else:
                    		o = random.randrange(4)
                        
                    		if(o == 0):
                        		self.x1 = self.x1 + 5
                    		if(o == 1):
                        		self.x1 = self.x1 - 5
                    		if(o == 2):
                        		self.y1 = self.y1 + 5
                    		if(o == 3):
                        		self.y1 = self.y1 - 5
					
                screen.blit(self.image,(self.x1 - playerx,self.y1 - playery)) 
#class coin:
  #  def __init__(self):
        
   #     self.x = 200
    #    self.y = 350
     #   self.image = pygame.image.load("coin.png")

  #  def update(self):
   #     screen.blit(self.image,(self.x,self.y))
class Medicina:
	def __init__(self):
		
		self.anime = glob.glob("Medicina/Medicina*.png")
		self.anime.sort()
		self.z = 0
		self.image = load_image(self.anime[self.z],True)
		self.image2 = load_image("Medicina/Frasco.png",True)
		self.rect1 = self.image.get_rect()
		self.rect2 = self.image.get_rect()
		
		#posicion final del nivel
		self.rect3 = self.image.get_rect()
		self.rect3.centerx1 = 800
		self.rect3.centery1 = 800
		
		self.cont1 = 1
		self.cont2 = 2
		self.cont3 = 3
		self.cont4 = 4
		
		self.x = 0
		self.y = 0
		#se usa la funcion random para selecionar 2 posiciones sin repetirse
		o = random.randrange(4)
		if(o == 0):
			self.x = self.cont1
			o = random.randrange(3)
			if(o == 0):
				self.y = self.cont2
			if(o == 1):
				self.y = self.cont3
			if(o == 2):
				self.y = self.cont4
		if(o == 1):
			self.x = self.cont2
			o = random.randrange(3)
			if(o == 0):
				self.y = self.cont1
			if(o == 1):
				self.y = self.cont3
			if(o == 2):
				self.y = self.cont4
		if(o == 2):
			self.x = self.cont3
			o = random.randrange(3)
			if(o == 0):
				self.y = self.cont1
			if(o == 1):
				self.y = self.cont2
			if(o == 2):
				self.y = self.cont4
		if(o == 3):
			self.x = self.cont4
			o = random.randrange(3)
			if(o == 0):
				self.y = self.cont1
			if(o == 1):
				self.y = self.cont2
			if(o == 2):
				self.y = self.cont3
		#posiciones de la medicina dependiendo del random
		#estas posiciones estan de ejemplo
		if(self.x = 1):
			self.x1 = self.rect1.centerx1 = 100
			self.y1 = self.rect1.centery1 = 400
		if(self.x = 2):
			self.x1 =self.rect1.centerx2 = 200
			self.y1 =self.rect1.centery2 = 400
		if(self.x = 3):
			self.x1 =self.rect1.centerx3 = 300
			self.y1 =self.rect1.centery3 = 400
		if(self.x = 4):
			self.x1 =self.rect1.centerx4 = 400
			self.y1 =self.rect1.centery4 = 400
			
		if(self.y = 1):
			self.x2 = self.rect2.centerx1 = 100
			self.y2 = self.rect2.centery1 = 400
		if(self.y = 2):
			self.x2 = self.rect2.centerx2 = 200
			self.y2 =self.rect2.centery2 = 400
		if(self.y = 3):
			self.x2 = self.rect2.centerx3 = 300
			self.y2 = self.rect2.centery3 = 400
		if(self.y = 4):
			self.x2 = self.rect2.centerx4 = 400
			self.y2 =self.rect2.centery4 = 400
		update()
		def update(self):
			#animacion de movimiento de la medicina
			self.connt = 0
			self.connt++
			if(self.connt = 5):
				self.connt = 0
				self.z++
				self.image = load_image(self.anime[self.z],True)
			if(self.z == 7):
				self.z = 0
			
		def TocarMedicina(self,playerx,playery,Medicinax,Medicinay,BarraCordura):
			self.Variacionx = playerx - Medicinax
			self.Variaciony = playery - Medicinay
			
			if(self.Variacionx < 3 and self.Variaciony < 3):
				
				self.z = self.z - 26
				if(z < 0):
					z = 0
			
					
			#Sprite collide con las medicinas
			#aumentar la vida en el momento que las toque(restar 28 a z de la vida)
			#borrar la imagen de la medicina
			
			#final del nivel
			
				
			
		
		
class Vida:
	def __init__(self):
		self.anime = glob.glob("BarraCordura/BarraCordura*.png")
		self.anime.sort()
		self.z = 0
		self.cont = 0
		self.image = load_image(self.anime[self.z],True)
       		self.rect = self.image.get_rect()
       		self.rect.centerx = 100
       		self.rect.centery = 500
		self.animeMax = len(self.anime) - 1
		#colores para darle "un toque" al final
		self.blanco = (255,255,255)
		self.gris1 = (180,180,180)
		self.gris2 = (100,100,100)
		self.negro = (0,0,0)
		self.updateVida(self.z,self.cont,)
	def ObjetoTexto(Mensaje,color):
		textoSurperfice1 = font.render(Mensaje,True,color)
		return textoSurperfice1 ,textoSurperfice1.get_rect()
	def MensajePantalla(Mensaje , color , cambioy = 0):
		textoSuperficie , textoRect = ObjetoTexto
		textoRect.center = (w/2),(h/2) + cambioy
		PantallaTexto = font.render(Mensaje , True , color)
		screen.blit(textoSuperficie,textoRect)
	def updateVida(self,playerx,playery,Enemyx1,Enemyy1):
		self.Variacionx = playerx - Enemyx1
		self.Variaciony = playery - Enemyy1
		self.cont++
		if(self.cont == 10):
				
			self.z = self.z + 1
			self.image = load_image(self.anime[self.z],True)
			self.cont = 0
			
		if(self.Variacionx < 3 and self.Variaciony < 3):
				
			self.z = self.z + 26
			self.cont1 = 1
			self.cont2 = 0
			if(self.x > 78):
				self.x = 78
			self.image = load_image(self.anime[self.z],True)
				
			while(self.cont1 == 1):
				self.cont2 = self.cont2 + 1
				if(self.cont2 == 5):
					self.cont1 = 0
					self.cont2 = 0
			if(self.z == 78):
				("mensaje de game over y opciones para continuar o salir")
				self.gameover = true
				self.contDie = 0
				screen.fill(self.gris2)
				pygame.display.update()
				
			while self.gameover == true:
				self.contDie++
				if(self.contDie = 1):
					screen.fill(self.negro)
				
				if(self.contDie = 4):
					screen.fill(self.gris1)
				if(self.contDie = 7):
					screen.fill(self.blanco)
				if(self.contDie = 8):
					MensajePantalla = ("Has perdido" , self.gris1,20)
				if(self.contDie = 9):
					MensajePantalla = ("Has perdido" , self.gris2,20)
				if(self.contDie = 10):
					MensajePantalla = ("Has perdido" , self.negro,20)
					MensajePantalla = ("ESPACIO para continuar y ESCAPE para salir" , self.negro , 0)
				
				
					
				pygame.display.update()
					
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
            					sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key = pygame.K_SPACE:
							gameover = false
							Juego()
						if event.key = pygame.K_ESCAPE:
							menu1()
				
					
				
		


#coin1 = coin()
def Juego():
	
	player1 = player()
	enemy1 = Enemy()
	vida1 = Vida()
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
		    position = 6

		elif event.type == KEYUP and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
		    position = 0
		    player1.animPosition = 0

	    Mapa.render_tiles_to_screen("Mapa1.tmx",player1.x,player1.y, player1.rect) 
	    enemy1.updateIA(player1.x,player1.y)
	    player1.update(position)
	    pygame.display.flip()       
Juego()
