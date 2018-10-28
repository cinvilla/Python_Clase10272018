#while ejemplo

bandera = True
colores = 0
while bandera:
    colores += 1
    print(f'Hola: El valor del tiquete es de ${colores}')
    if colores == 3:
        bandera = False

#while ejemplo

bandera = True
colores = 0
while bandera:
    colores += 1
    print(f'Hola: El valor del tiquete es de ${colores}')
    if colores == 3:
        bandera = False

else:
    print(f'El valor del tiquete subió ${colores}')
print(f'Por fuera: el valor es de: ${colores}')