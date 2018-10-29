#try except
a = 10
b = 5

try:
    c = a / b
except ZeroDivisionError
    print('Tengo un error en la division')
    c = a
else:
    print('Dentro de else')
finally
    print('Dentro de finally')
    pass


