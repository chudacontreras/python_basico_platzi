# -*- coding: utf-8 -*-

def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 175.53

    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA  DE  DIVISAS')
    print('Convierte de pesos Mexicanos a Pesos Colombianos\n')
    ammount=float(raw_input('Ingrese la cantidad de pesos que desea convertir -->  '))

    result = foreing_exchange_calculator(ammount)


    print('${} pesos mexicanos son ${} pesos colombianos\n'.format(ammount, result))


if __name__ == "__main__":
    run()