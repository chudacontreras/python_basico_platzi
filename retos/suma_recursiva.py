# -*- coding: utf-8 -*-

def run(num):
    numero = 0
    for numero in range(num):
        print(numero + 1)

if __name__ == "__main__":
    num = int(input("Ingrese entero, un numero que sera el tope de la suma: "))
    run(num)