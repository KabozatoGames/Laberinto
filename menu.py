import pygame
#Clase del raton , en ella se crea un rectangulo de 1x1 hacia donde
#apunte
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()
#Clase de los botones , aqui se dan las posiciones y imagenes
        
class Boton(pygame.sprite.Sprite):
    def __int__(self,image1,image2,x,y):
        self.imagenNormal = imagen1
        self.imagenSelecion = imagen2
        self.imagenActual = self.imagenNormal
        self.rect = self.imagenActual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    #El update se encargara de cambiar la imagen cuando el raton este encima
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagenActual = self.imagenSeleccion
        else:
            self.imagenActual = Self.imagenNormal
        pantalla.blit(self.imagenActual,self.rect)
def main():
    pygame.init()
    #"kamilo no me acordaba de cuanto era la pantalla del juego en si"
    
    pantalla = pygame.display.set_mode((500,400))
    pygame.display.set_caption("KabozatoGames")

    relog1 = pygame.time.Clock()
    #La primera imagen sera para su estado normal y la segunda para
    #cuando el raton este encima de el
    
    menu1 = pygame.image.load("imagen1.png")
    menu2 = pygame.image.load("imagen2.png")
    #aqui se crea un boton con las dos imagenes y las posiciones
    
    boton1 = Boton(menu1,menu2,200,200)
    #boton2 = Boton(nuevapartida1,nuevapartida2,200,250)
    
    cursor1 = Cursor()
    
    
    blanco=(255,255,255)
    salir = False
    while salir != True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    juego()
                #aqui se crearia lo que harian los demas botones
            if event.type == pygame.QUIT:
                salir = True
                
        relog1.tick(20)
        pantalla.fill(blanco)
        cursor1.update()
        boton1.update(pantalla,cursor1)
        pygame.display.update()
    pygame.quit()
main()

        
