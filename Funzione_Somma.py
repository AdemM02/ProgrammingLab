lista_numeri = [4,5,6,7,9]

def somma(lista):
    risultato = 0
    for item in lista:
        risultato = risultato + item
    print('Risultato della somma = {}'.format(risultato))

risultato = somma(lista_numeri)