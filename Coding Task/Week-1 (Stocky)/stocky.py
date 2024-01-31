import unittest
import pandas as pd

class StockAnalyzer:
    def __init__(self, filename):
        self.data = pd.read_csv(filename)

    def getMaxHighPrice(self):
        return self.data['High'].max()

    def getMinLowPrice(self):
        return self.data['Low'].min()

    def getAverageVolume(self):
        return self.data['Volume'].mean()

    def getMaxDayGain(self):
        self.data['Gain'] = self.data['Close'] - self.data['Open']
        return self.data['Gain'].max()

class TestStockAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = StockAnalyzer("./HCLTECH.NS.csv")

    def test_getMaxHighPrice(self):
        self.assertEqual(self.analyzer.getMaxHighPrice(), 1555.0)  

    def test_getMinLowPrice(self):
        self.assertEqual(self.analyzer.getMinLowPrice(), 1016.25)  

    def test_getAverageVolume(self):
        self.assertEqual(self.analyzer.getAverageVolume(), 2640535.174796748)  

    def test_getMaxDayGain(self):
        self.assertEqual(self.analyzer.getMaxDayGain(), 69.30004899999994)  

if __name__ == '__main__':
    unittest.main()