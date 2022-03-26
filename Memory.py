from random import *
from turtle import *

from freegames import path

cont = {'cero' : 0, 'uno': 0}
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        cont['cero'] = cont['cero']+1 # Agrega 1 al contador de taps por cada tap
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        cont['uno'] = cont['uno'] + 1 # Agrega 1 al contador para saber si el juego ya está terminado


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x +11, y+8) # Esto hará que los números queden centrados en el cuadro. 
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    up()
    goto(-340,190)
    down()
    write("Taps: = " + str(cont['cero']), font=('Arial', 10, 'normal'))
    up()
    if cont['uno'] > 31:
            goto(220,190)
            down()
            write("YOU WIN", font=('Arial', 30, 'normal'))
            up()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
