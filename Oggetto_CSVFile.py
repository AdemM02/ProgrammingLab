class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        lista_due_elementi = []
        lista_completa = []
        file = open(self.name,'r')
        for line in file:
            elementi_lista = line.split(',')
            if elementi_lista[0] != 'Date':
                data = elementi_lista [0]
                valore = elementi_lista [1]
                lista_due_elementi = [data, valore]
                lista_completa.append(lista_due_elementi)
        return lista_completa
        
        
Var1 = CSVFile('shampoo_sales.csv')
var2 = Var1.get_data()
print(var2)
    
            
        
        