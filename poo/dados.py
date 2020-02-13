
# -*- coding: utf-8 -*-

""" Este programa es un juego de azar en el que se lanza un dado y si el valor no es ni 1 ni 6 se pierde.
Para esto creamos la clase Dice con los atributos de un dado su valor y su cantidad de lados así como su comportamiento
como lo es el lanzarlo o girarlo para que obtengamos un valor al azar"""



#Importo libreria Random

import random

class Dice:
	"""Clase  que crea un dado. Se puede lanzar el dado y obtener su valor. Darse cuenta que el array está declarado como contante
	y además como privado ya que tiene dos (_) antes de dato. Que quiere decir esto? Ques una constante privada la cual solo puede ser
	accedida dentro de su propia clase. Si tuviese un solo (_) sería una constante publica de la clase, así que cualquier pudiese
	acceder a ella en el main por ejemplo"""

	__DADO= ["""

		-----
		|   |
		| o |
		|   |
		-----
		""", """

		-----
		|o  |
		|   |
		|  o|
		-----
		""","""

		-----
		|o  |
		| o |
		|  o|
		-----
		""","""

		-----
		|o o|
		|   |
		|o o|
		-----
		""", """

		-----
		|o o|
		| o |
		|o o|
		-----
		""", """

		-----
		|o o|
		|o o|
		|o o|
		-----"""]

		#Constante que define que el dado tiene 6 lados

	__SIDES = 6

		#en el constructor de la clase no es necesario pasarle nada ya que se creará el dado con valor 1
	def __init__(self):
		self.__value=1


		#Con el metodo roll le damos un valor random de 1 a 6 a la instancia. Lo que es lo mismo que lanzar el dado
	def roll(self):
		self.__value= random.randint(0,6)
		#Aquí mostramos el dibujo que corresponde al valor de dado obtenido
		self.__display_dice()

		#este metodo es para obtener el valor del dado en el programa proncipal. De esa manera no es necesario accesar a la propia variable
		#__value ya que es una variable privada que no queremos que sea modificada por el usuario a menos que use el metodo roll()
	def get_value(self):
		return self.__value

		#En este metodo mostramos la figura del dado que corresponda al valor generado cuando lanzamos el dado. Dense cuenta que en
		# en este metodo tambien lo declaramos como un metodo privado que solo puede ser accedido dentro de la clase
	def __display_dice(self):
		if self.__value is 1:
			print(self.__DADO[0])
		elif self.__value is 2:
			print(self.__DADO[1])
		elif self.__value is 3:
			print(self.__DADO[2])
		elif self.__value is 4:
			print(self.__DADO[3])
		elif self.__value is 5:
			print(self.__DADO[4])
		else:
			print(self.__DADO[5])

def main():
	dado = Dice()


	dado.roll()

	if 1 < dado.get_value() and dado.get_value() < 6:
		print("perdiste, sacaste", dado.get_value())
	else:
		print("ganaste, sacaste", dado.get_value())

	#intenten usar esta linea de codigo y verán que les arrojará error ya que es una variable privada

	#print(dado.__SIDES)



if __name__ == '__main__':
	main()
