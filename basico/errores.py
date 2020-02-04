# -*- coding: utf-8 -*-

'''countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31,
    'venezuela': 50
}'''

'''while True:
    country = str(raw_input('Escribe el nombre de un país: ')).lower()

    try:
        print('La población de {} es: {} millones'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(country))
'''
def main():
    countries = {
        'mexico': 122,
        'colombia': 49,
        'argentina': 43,
        'chile': 18,
        'peru': 31,
        'venezuela': 50
    }
    opc = "s"

    while opc == "s":
        country = str(raw_input('Escribe el nombre de un pais:  ')).lower()

        try:
            print('La poblacion de {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            print('No tenemos el dato de la población de {}'.format(country))
        finally:
            opc = str(raw_input('Desea consultar otro pais: s/n: ')).lower()
            
            
            #opc=opc.lower
            if opc != "s":
                print('Saliendo del programa Gracias')



        
if __name__ == '__main__':
    main()

