# -*- coding: utf-8 -*-
import sys, textwrap


KEYS = {
    'a': '01110111',
    'b': '01000101',
    'c': '01111000',
    'd': '00110001',
    'e': '01100001',
    'f': '01110100',
    'g': '00110000',
    'h': '01000011',
    'i': '01100010',
    'j': '00100001',
    'k': '01111010',
    'l': '00111000',
    'm': '01001101',
    'n': '01001001',
    'o': '01100100',
    'p': '00101110',
    'q': '01010101',
    'r': '01011001',
    's': '01101001',
    't': '00110011',
    'u': '00101100',
    'v': '01001010',
    'w': '01001110',
    'x': '01100110',
    'y': '01101101',
    'z': '01010111',
    'A': '01000111',
    'B': '01010011',
    'C': '01101010',
    'D': '01101110',
    'E': '01110011',
    'F': '01010001',
    'G': '01101111',
    'H': '01100101',
    'I': '01110101',
    'J': '01100111',
    'K': '00110010',
    'L': '00111001',
    'M': '01000001',
    'N': '00110101',
    'O': '00110100',
    'P': '00111111',
    'Q': '01100011',
    'R': '01110010',
    'S': '01001111',
    'T': '01010000',
    'U': '01101000',
    'V': '00110110',
    'W': '01110001',
    'X': '01001000',
    'Y': '01010010',
    'Z': '01101100',
    '0': '01101011',
    '1': '00110111',
    '2': '01011000',
    '3': '01001100',
    '4': '01110000',
    '5': '01110110',
    '6': '01010100',
    '7': '01010110',
    '8': '01111001',
    '9': '01001011',
    '.': '01011010',
    ',': '01000100',
    '?': '01000110',
    '!': '01000010',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        word = textwrap.wrap(word, 8)
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.iteritems():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():

    while True:

        command = str(raw_input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(raw_input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(raw_input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('saliendo')
            sys.exit()
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()