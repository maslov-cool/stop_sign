from turtle import *
from math import *


def sign(side):
    hideturtle()
    pensize(3)

    # рисуем границу
    for i in range(8):
        left(45)
        forward(side)

    # перемещаем внутрь
    penup()
    goto(-0.025 * side, 0.05 * side)
    pendown()

    # закрашиваем
    pencolor('white')
    fillcolor('red')
    begin_fill()
    for i in range(8):
        left(45)
        forward(side * 0.95)
    end_fill()

    # пишем надпись
    penup()
    goto(-0.5 * side, side)
    pendown()
    color('white')
    write('STOP', font=('Arial', side / 2, 'normal'), align='center')


sign(int(input()))
