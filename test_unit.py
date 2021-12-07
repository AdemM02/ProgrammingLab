# DA FINIRE
import unittest from NumericalCSVFile import CSVFile


class TestNumericalCSVFile (unittest.TestCase):
    def test_init (self):
        try:
            csv_file = CSVFile('shampoo_sales.csv')
            self.assertEqual(csv_file.name, 'shampoo_sales.csv')
        except: