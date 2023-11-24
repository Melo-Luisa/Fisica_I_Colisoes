import pygame as py
import random, time, math
py.init() 
  
largura = 800
altura = 600
screen = py.display.set_mode((largura, altura)) 

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
    # def calc_distancia(self, ball): 
    #     #calcular a distancia = {sqrt[(x2-x1)**2]+[(y2-y1)**2]}
    #     x, y = ball.coordX, ball.coordY
    #     x2, y2 = ball.coordY, ball.coordX

    #     self.distancia = math.sqrt((x2 - x)**2 + (y2 - y)**2)
    def colisao(self, outra_bola):
        distancia = math.sqrt((outra_bola.coordX - self.coordX)**2 + (outra_bola.coordY - self.coordY)**2)
        if distancia < (self.raio + outra_bola.raio):
            print('Colisão entre bolas!', self.coordX, self.coordY)   

        return distancia 

            
  #distancia era menor do que a soma dos dois raios
        #o que fazer
        #pegar posicao da bolinha [i] com posicao de[i+1] e somar
        #se a distancia < que raio[i] + raio[i+1]:
        #print('colisão')
         
running = True

n_bolas = 3
raio = 10
lista_bolas = []
distancia = []   
clock = py.time.Clock()
for i in range(n_bolas):
    posX = random.randint(0,largura - raio)
    posY = random.randint(0,altura)
    lista_bolas.append(bolas(posX,posY,i*2,5,raio))
    posY += 30
    posX += 20
    cor = (255,45,215)

#print(lista_bolas)

while running: 
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in py.event.get(): 
        if event.type == py.QUIT: 
            running = False

    for i, ball in enumerate(lista_bolas): 
        ball.move() #move
        ball.limite_wall() #limitador de bolinhas
        for j in range(n_bolas):
            #distancia_balls = ball.calc_distancia(lista_bolas[j]) #função que calcula a distancia das bolinhas
            #distancia.append(distancia_balls) # lista
            #ball.colisao(distancia_balls)
            if i != j:  # Evitar verificar a colisão da bola consigo mesma
                ball.colisao(lista_bolas[j])
        py.draw.circle(screen, cor, (ball.coordX, ball.coordY), ball.raio)
    #print(distancia_balls)

    py.display.update()
py.quit()




