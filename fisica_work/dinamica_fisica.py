import pygame as py
import random, time, math
py.init() 
  
largura = 800 #x
altura = 450 #y
screen = py.display.set_mode((largura, 650)) 
py.display.set_caption("Colisões - Física")

class bolas:
    def __init__(self,coordX, coordY, speedX, speedY, raio):
        self.coordX = coordX
        self.coordY = coordY
        self.speedX = speedX
        self.speedY = speedY
        self.raio = raio
    def move(self):
        self.coordX += self.speedX
        self.coordY += self.speedY 
    def limite_wall(self):
        if self.coordX < 0 or self.coordX > largura:
            self.speedX *= -1
        elif self.coordY < 0 or self.coordY > altura:
            self.speedY *= -1 #mudei a direção da velocidade, que soma com a coordenada 
    def colisao(self, outra_bola): #colisoes

        distancia = math.sqrt((outra_bola.coordX - self.coordX)**2 + (outra_bola.coordY - self.coordY)**2)
        if distancia < (self.raio + outra_bola.raio):
            self.speedX *= -1
            self.speedY *= -1  
        return distancia 



running = True



n_bolas = 7
raio = 10
lista_bolas = []
distancia = []   
clock = py.time.Clock()
for i in range(n_bolas):
    posX = random.randint(raio,largura-raio)
    posY = random.randint(raio,altura-raio)
    lista_bolas.append(bolas(posX,posY,i*1.5,5,raio))
    posY += 30
    posX += 20
    cor = (255,45,215)

font = py.font.Font(None, 36) 
velocidade = font.render("Velocidade: ", True, (255, 255, 255))  # Text, antialias, color
coordenadas_X = font.render(f'X: {posX}', True, (255, 255, 255))
coordenadas_Y = font.render("Y:", True, (255, 255, 255))

while running: 
    clock.tick(60)
    screen.fill((0, 0, 0))

    
    screen.blit(velocidade, (50, 500))
    
    screen.blit(coordenadas_Y, (50, 600))
    for event in py.event.get(): 
        if event.type == py.QUIT: 
            running = False

    for i, ball in enumerate(lista_bolas): 
        for j in range(n_bolas):
            if i != j:  # Evitar verificar a colisão da bola consigo mesma
                ball.colisao(lista_bolas[j])
        ball.move() #move
        ball.limite_wall() #limitador de bolinhas
        screen.blit(coordenadas_X, (50, 550))
        py.draw.circle(screen, cor, (ball.coordX, ball.coordY), ball.raio)

    py.display.update()
py.quit()
