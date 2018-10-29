# Primer ejemplo con loops - for
for indice, elemento in enumerate (['maria', 'jose', 'pedro', 'juan']):
    print('El indice {} para el valor {}' .format(indice, elemento))

# enumerate - para obtener el índice de posición junto a su valor correspondiente.

# Primer ejemplo con loops - for
print()
for indice, elemento in enumerate(['maria', 'jose', 'pedro', 'juan']):
    print(f'El indice {indice} para el valor {elemento}')

# en reversa -1
print()
mi_lista = ['maria', 'jose', 'pedro', 'juan']
for indice, elemento in enumerate(mi_lista[::-1]):
    print(f'El indice {indice} para el varlor {elemento}')

# lista.sort ordena la lista en sí, pero con sorted es distinto
print()
mi_lista = ['maria', 'jose', 'pedro', 'juan']
for indice, elemento in enumerate(sorted(mi_lista)):
    print(f'El indice {indice} para el varlor {elemento}')

print()
mi_lista = ['maria', 'jose', 'pedro', 'juan']
for indice, elemento in enumerate(sorted(mi_lista, reverse=True)):
    print(f'El indice {indice} para el varlor {elemento}')

# Para que el loop no inicie se agrega [] a la lista
mi_lista = ['maria', 'jose', 'pedro', 'juan']
for indice, elemento in enumerate(sorted(mi_lista)):
    print(f'El indice {indice} para el varlor {elemento}')
else:
    print('El loop no empezó')
    
## Print test using list sequences
