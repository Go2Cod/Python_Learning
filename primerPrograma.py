

##def uno_dos_tres(x,y,z):
##    print('X-> {a}'.format(a=x))
##    print('Y-> {a}'.format(a=y))
##    print('Z-> {a}'.format(a=z))


##En esta version de la funcion entre corchetes ponemos 0 y eso
##hace que no haga falta poner dentro del .format(0=x)....como en la funcion de arriba
def uno_dos_tres(x,y,z):
    print('X-> {0}'.format(x))
    print('Y-> {0}'.format(y))
    print('Z-> {0}'.format(z))

    
uno_dos_tres(1,2,3)
    