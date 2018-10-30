la_lista = ['Asus','Samsumg','HP','LG','AOC'] # Paso 1 se designan los elementos dentro de una lista, lista que será utilizada para la secuencia.
for posicion, elemento in enumerate(la_lista[::-1]): # Paso 2 el index operator combinado con el salto ordenarán los elementos de atrás hacia adelante.
    # Paso 3. El método enumerate devolverá la posición de cada elemento dentro de la lista y su valor creando así a partir de un elemento 2 elementos.
    # Paso 4. El for loop tomará cada uno de los elementos del output de enumerate method y barrerá sus subelementos nombrándolos con los nombres
    # posicion y elemento (variables names) uno por uno para así ejecutar el mandato de impresión.
    print(f'El dispositivo tipo {elemento} será evaluado en la posición {posicion}')


