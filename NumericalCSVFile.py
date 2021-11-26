# Dichiaro classe e inizializzo CSVFile
class CSVFile():
    def __init__(self, name):
        self.name = name
        
    # Dichiaro la funzione get_data
    def get_data(self):
        lista_due_elementi = []
        lista_completa = []
        # Se il file non esiste, allora ritrono 1000
        try:
            # Per ogni riga del file, separo le date dai prezzi
            file = open(self.name,'r')
            for line in file:
                elementi_lista = line.split(',')
                if elementi_lista[0] != 'Date':
                    data = elementi_lista [0]
                    valore = elementi_lista [1]
                    # Faccio una lista che comprende la data e il prezzo corrispondente
                    lista_due_elementi = [data, valore]
                    # Faccio una lista a cui aggiungo sempre lista_due_elementi
                    lista_completa.append(lista_due_elementi)
        except Exception as e:
            print('Errore: {}'.format(e))
            return 1000
        file.close()
        # Ritorno la lista di liste
        return lista_completa


# Dichiaro una classe che estende CSVFile
class NumericalCSVFile(CSVFile):
    # Dichiaro nuovo funzione get_data
    def get_data(CSVFile):
        lista_due_elementi = []
        lista_normale = []
        # Richiamo il get_data originale per ottenere lista_completa
        lista_completa = super().get_data()
        # Divido lista_completa in liste singole (che sono item di lista_completa
        for item in lista_completa:
            lista_due_elementi = item
            # Salvo il valore del prezzo e poi lo aggiungo a lista_normale
            valore = lista_due_elementi [1]
            # Se non riesco a convertire "valore" ad un numero, al posto del valore metto 'Valore non valido'
            try:
                lista_normale.append(float(valore))
            except Exception as e:
                print('Errore: {}'.format(e))
                lista_normale.append('Valore non valido')
        # Ritorno la lista con tutti i valori
        return lista_normale


# Instanzio var3 sull'oggetto/classe NumericalCSVFiles con argomento il file shampoo
var3 = NumericalCSVFile('shampoo_sales.csv')
# Eseguo e stampo la funzione get_data su var3
var4 = var3.get_data()
print(var4)