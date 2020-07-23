import pynput
import time

from pynput.mouse import Button, Controller

mouse = Controller()

# O topo y é 145
# O fim  y é 660

#distância de 10 no eixo x (presumo) e y (certeza)
tempo = 0.0005
temp2 = 0.3
x = 420
y = 150
xFinal = 955
yFinal = 655

#=================================================
# Corte do meio

mouse.position = (400, 400)
time.sleep(temp2)
i = 400

while i <= 950:
    time.sleep(tempo)
    mouse.move(5,0)
    i += 5

print(i)

#=================================================
# Corte do 1/4

mouse.position = (400, 275)
time.sleep(temp2)
i = 400

while i <= 950:
    time.sleep(tempo)
    mouse.move(5,0)
    i += 5

print(i)
    
#=================================================
# Corte do 3/4

mouse.position = (950, 530)
time.sleep(temp2)

while i >= 400:
    time.sleep(tempo)
    mouse.move(-5,0)
    i -= 5

print(i)

#=================================================
# Corte do 1/8

mouse.position = (400, 210)
time.sleep(temp2)
j = 210

while j <= 660:

    if i <= 950:
        while i <= 950:
            time.sleep(tempo)
            mouse.move (5,0)
            i += 5

    else:
        while i >= 400:
            time.sleep(tempo)
            mouse.move(-5,0)
            i -= 5

    j += 125
    mouse.position = (i, j)

#=================================================
# Aqui, está tudo preparado, isto é, temos uma
# grade de 8x8 círculos.

j = 175
i = 400
mouse.position = (i, j)
time.sleep(temp2)

while j <= 630:
    if i <= 950:
        while i <= 950:
            time.sleep(tempo)
            mouse.move (5,0)
            i += 5

    else:
        while i >= 400:
            time.sleep(tempo)
            mouse.move(-5,0)
            i -= 5 

    j += 65
    mouse.position = (i, j)


#=================================================
# Aqui, está tudo preparado, isto é, temos uma
# grade de 16x16 círculos.

j = 160
i = 400
mouse.position = (i, j)
time.sleep(temp2)

while j <= 655:
    if i <= 950:
        while i <= 950:
            time.sleep(tempo)
            mouse.move (5,0)
            i += 5

    else:
        while i >= 400:
            time.sleep(tempo)
            mouse.move(-5,0)
            i -= 5 

    j += 32.5
    mouse.position = (i, j)



#'''
tempo = 0.025
temp2 = 0.025
aux = 0
    
mouse.position = (x, y)

while y <= yFinal:
    time.sleep(temp2)
    while x <= xFinal:
        time.sleep(tempo)
        mouse.move (5, 0)
        x += 5
        print(x)

    if aux == 0:
        time.sleep(temp2)
        while x >= 420:
            time.sleep(tempo)
            mouse.move(-5, 0)
            x -= 5
            print(x)

    if aux == 0:
        aux = 1
    else:
        aux = 0
    x = 420
    mouse.position = (x, y)
    time.sleep(tempo)
    mouse.move (0, 8)
    y += 8.01

#'''
