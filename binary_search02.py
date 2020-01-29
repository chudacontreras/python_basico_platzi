# -*- coding: utf-8 -*-
def ordened_list(numbers):
    numbers.sort()
    return numbers

def binary_search(lista_ordenada, number_search, low, high):

    if low > high:
        return False
    
    mid = int((low + high) / 2)

    if lista_ordenada[mid] == number_search:
        return True

    elif lista_ordenada[mid] > number_search:
        return binary_search(lista_ordenada, number_search, low, mid - 1)
    else:
        return binary_search(lista_ordenada, number_search, mid + 1, high )




if __name__ == '__main__':
    numbers = [23, 45, 21, 5, 87, 12, 34, 7, 1, 9, 2, 46, 28, 19, 73]
    #numbers = range(0,100)
    print(' ')
    print(numbers)
    print(' ')
    lista_ordenada = ordened_list(numbers)
    print(' ')
    print (lista_ordenada)
    print(' ')

    number_search = int(input('Ingrese un numero: '))
    find_number = binary_search(lista_ordenada, number_search, 0, len(lista_ordenada) -1)
    
    if find_number == False:
        print('El numero NO se encuentra en la lista')
    else:
        print('El numero SI se encuentra en la lsta')