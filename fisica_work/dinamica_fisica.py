import pygame as py
import random, time
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
    def distancia(self, lista_bolas): 
        #distancia era menor do que a soma dos dois raios
        #o que fazer
        #pegar posicao da bolinha [i] com posicao de[i+1] e somar
        #se a distancia < que raio[i] + raio[i+1]:
        #print('colisão')
        pass
        
            

         
running = True


n_bolas = 6

raio = 10
lista_bolas = []   
clock = py.time.Clock()
for i in range(n_bolas):
    posX = random.randint(0,largura - raio)
    posY = random.randint(0,altura)
    lista_bolas.append(bolas(posX,posY,i*2,5,raio))
    posY += 30
    posX += 20
    cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#print(lista_bolas)

while running: 
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in py.event.get(): 
        if event.type == py.QUIT: 
            running = False
    #screen.fill(0,0,0)

    for ball in lista_bolas: 
        ball.move()
        ball.limite_wall()
        py.draw.circle(screen, cor, (ball.coordX, ball.coordY), ball.raio)
        

    py.display.update()
py.quit()




