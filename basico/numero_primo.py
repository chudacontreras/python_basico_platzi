# -*- coding: utf-8 -*-

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
    
    return True

def run():
    #pass
    number = int(raw_input('Escribe un numero:  '))

    result = is_prime(number)

    if result is  True:
        print ('Tu Numero es primo')
    else:
        print(' tu nuemro NO es primo')



if __name__ == "__main__":
    run()