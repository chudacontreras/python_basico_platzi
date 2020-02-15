# -*- coding: utf-8 -*-


def protected(func):#funcion que recibe como parametros otra funcion

    def wrapper(password):#funcion creada dentro de otra funcion

        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@protected #Decorador
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))

    protected_func(password)
