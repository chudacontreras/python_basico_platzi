# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    tortuga =turtle.Turtle()


    make_square(tortuga)
    turtle.mainloop()


def make_square(tortuga):
    length = int(raw_input('tamanio de cuadrado: '))

    for i in range(4):
        make_line_and_turn(tortuga, length)


def make_line_and_turn(tortuga, length):
    tortuga.forward(length)
    tortuga.left(90)


if __name__ == '__main__':
    main()