# Paso a paso para entender el output del enumerate y qué hace
print("Esta es la prueba uno")
mi_tupla = ('Cin','Dey','Kev')
print(enumerate(mi_tupla))
nueva_tupla = tuple(enumerate(mi_tupla))
print(nueva_tupla)
print("#######")
for index, possition in nueva_tupla:
    print('Para el valor {} su índice de posición es {}'.format(possition,index))

########################################################################################
print()
print("Esta es la prueba dos")
# Como lo hizo el profe es mucho más fácil porque así simplemente se usa la lista misma sin tener que nombrarla antes
# y simplemente usando la función enumerate
print()
for index, possition in enumerate(['Ana','Deybid','Kevin']):
    print('Para el valor {} su índice de posición es {}'.format(possition,index))

########################################################################################
print()
print("Esta es la prueba tres")
# Paso a paso para entender el output del format y qué hace
for x,y in enumerate(('Jose', 'Deybid', 'Alexander','Andres')):
    print('Hola {} esperamos tenga un hermoso dia! Su posición en la lista es {}' .format(y,x))