# Para poder entender como usar format, se me ocurrió utilizarlo en este ejemplo que había usado en la set.
# Si no utilizáramos el format method, dentro de los print ocuparíamos usar más comas:
my_set_empty = set()
print(my_set_empty, ': creará un set empty, y el data type será', type(my_set_empty))

# Con el format method podemos usar los curly braces y dentro del format method indicar los valores de las variables:
my_set_empty = set()
print('{}: creará un set empty, y el data type será'.format(my_set_empty), type(my_set_empty))
#Quizá en este ejemplo no es tan eficiente utilizar format pero al menos funciona para entender como utilizarlo

# Utilizando la f de format dentro de los curly braces podemos ingresar
my_set_empty = set()
print(f'{my_set_empty}: creará un set empty, y el data type será', type(my_set_empty))
