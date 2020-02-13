# -*- coding: utf-8 -*-


class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):#metodo de instancia __init__ es el contuctor de la clase
        self._is_turned_on = is_turned_on

    def turn_on(self):#metodos publicos
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):#metodos publicos
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):#metodo privado
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
