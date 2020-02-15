# -*- coding: utf-8 -*-

import random

from dados import Dice

def run():
	dados = Dice()


	dados.roll()

	if 1 < dados.get_value() and dados.get_value() < 6:
		print("perdiste, sacaste", dados.get_value())
	else:
		print("ganaste, sacaste", dados.get_value())

	#intenten usar esta linea de codigo y verán que les arrojará error ya que es una variable privada

	#print(dado.__SIDES)



if __name__ == '__main__':
	run()