calificaciones={}
calificaciones['matematicas']=9
calificaciones['fisica']=8
calificaciones['etica']=10
calificaciones['quimica']=7
calificaciones['lenguaje']=8
for key in calificaciones: #obtiene las llaves (keys) dentro del diccionario calificaciones
    
    print('Llaves: {}'.format(key))
    
for key in calificaciones.values(): #obtiene los valores (values) dentro del diccionario calificaciones
    
    print('Valores : {}'.format(key))
    
for key,value in calificaciones.iteritems(): #obtiene los valores y las keys dentro del diccionario calificaciones
    
    print('Llave: {}, valor {}'.format (key,value))
    
#calcular promedio de calificaciones:
suma_calificaciones=0
for calificacion in calificaciones.values(): 
    suma_calificaciones += calificacion
print(' ')
print('La suma de las calificaciones es: {}'.format(suma_calificaciones))
promedio=suma_calificaciones /len(calificaciones.values())
print('Promedio de calificaciones: {}' .format(promedio))