# Faccio la funzione
def totale_vendite (file):

    # Apro il file 
    file = open('shampoo_sales.csv', 'r')

    # Faccio una lista dove salvare i singoli valori
    elementi_lista = []
    valore_vendite = []

    # Per ogni linea, separo la data dal valore e aggiungo il valore convertito in float alla lista
    for line in file:
        elementi_lista = line.split(',')
        data = elementi_lista [0]
        valore = elementi_lista [1]
        if valore != 'Sales\n':
            valore_vendite.append(float(valore))

    # Somma tutti i valori della lista e returno la loro somma
    somma = 0
    for item in valore_vendite:
        somma = somma + item
    return somma


# Dichiarazioni
file = 0
totale = 0

# Richiamo la funzione
totale = totale_vendite(file)

# Stampo il risultato
print('{}'.format(totale))

            
         
            