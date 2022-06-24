import primerPrograma
def dos_veces(mi_lista):
    lista=[]
    for element in mi_lista:
        lista.append(element*2)
    return lista

lista=[5,10,50,100]
print(' Antes dos veces(): {0}'.format(lista))
nlista=dos_veces(lista)
print(' despues dos veces(): {0}'.format(nlista))

primerPrograma.uno_dos_tres(4,5,6)
