# Para crear los set se utiliza la función set() y {}
my_set_empty = set()
print('{}: creará un set empty, y el data type será'.format(my_set_empty, type(my_set_empty)))

# Si se utiliza {} para crear un set resultará en un diccionario
print()
set_empty = {}
print('set_empty = {} esto creará un diccionario no un set:',type(set_empty))
set_empty = set()
print('Si utilizamos set_empty = set() esto assignará el data type set al dict:',type(set_empty))
print()

# Para crear set con contenido se usan las curly braces {}
my_set = {1,2,3}
your_set = {'test',3,3.14,2,4}
print('Los sets pueden ser de mixed data:', your_set,'o del mismo tipo:', my_set)
# sus elementos son inmutables por lo que los elementos no deberían ser de tipo list or dict

# Aún cuando inicialmente creemos un set con duplicados, él mismo nos lo reducirá a los valores únicos
print()
set_no_dup = {2,3,3,2,4,'Hello',5,6,'Hello'}
print(set_no_dup, 'Aún cuando se utilizó el comando **set_no_dup = {2,3,3,2,4,Hello,5,6,Hello}**',
                  'no duplicados fueron impresos o guardados dentro de la variable')

## Print test to understand set