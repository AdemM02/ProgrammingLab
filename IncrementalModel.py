# Faccio una funzione model con funzione fit e predict vuote
class Model ():

    def fit (self, data):
        raise NotImplementadError('Metodo non implementato')

    def predict (self, data):
        raise NotImplementadError('Metodo non implementato')


# Faccio una funzione per predire il valore successiovo rispetto a una serie
class IncrementalModel (Model):

    def predict(self, data):
        predizione = 0
        incremento = 0
        # Prendo la lughezza della lista
        n = len (data)

        # Sommo tutti gli incrementi fino a n (escluso)
        for i in range (1, n):
            incremento = incremento + (data [i] - data [i - 1])
        # Faccio la media degli incrementi
        incremento = incremento / (n - 1)
        # Ritorno il valore previsto
        predizione = incremento + data[n - 1]
        return predizione


# Prova di IncrementalModel
lista = [50, 52, 60]
A = IncrementalModel()
print('{}'.format(IncrementalModel.predict(A, lista)))


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


# Uso IncrementalModel sui prezzi di shampoo_sales.csv
var_A = NumericalCSVFile('shampoo_sales.csv')
lista_prezzi = var_A.get_data()
prezzo_previsto = IncrementalModel()
print('{}'.format(prezzo_previsto.predict(lista_prezzi)))