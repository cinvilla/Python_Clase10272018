# Para crear un dictionario utilizamos {}
my_empty_dict = {}
dict_data = {'juan' : 88, 'pedro' : 11, 'jose' : 56}
print("This is my empty dict", my_empty_dict,
      "And this is the dictionary that contains data", dict_data)

# Para consultar los valores dentro de los keys en el diccionario usamos []
dict_data['pedro']
print()
print(dict_data['pedro'], 'is Pedros phone number.',
      'The [] brackets are used to display value assigned to keys',
      'and to edit a value of a key I can simply set the key to another value using '
      'the assignment operator =')

# Para agregar keys dentro del diccionario usamos []
dict_data['miguel'] = 48
print()
print('This shows a dictionary update', dict_data)
