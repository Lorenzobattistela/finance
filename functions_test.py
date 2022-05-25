import unittest
import helpers

class TestHelpers(unittest.TestCase):
    def testInvestmentTypes(self):
        investTypes = ['cash', 'international', 'stocks', 'fii', 'gov']
        self.assertEqual(helpers.get_investment_types(), investTypes, 'Should have cash, international, stocks, fii and gov.')

    def testInvestmentLabel(self):
        investTypes = ['cash', 'international', 'stocks', 'fii', 'gov']
        investLabels = [['storedAt','quantity','rentability'], ['quote','buy_price','quantity','country'], ['quote','buy_price','quantity'],['quote', 'buy_price','quantity','dividend_yield'], ['name','quantity','rentability']]

        for i in range(len(investTypes)):
            labels = helpers.get_investment_label(investTypes[i])
            self.assertEqual(labels, investLabels[i])

    def testCalculateBalance(self):
        buy_price = 100
        actual_price = 150
        quantity = 10
        true_balance = round(float(((actual_price - buy_price) * quantity)), 2)
        balance = helpers.calculate_balance(buy_price, actual_price, quantity)
        self.assertEqual(balance, true_balance)

    def calculate_next_balance(self):
        rentability = 10 #percent
        value = 100 # reais
        true_nxt_balance = round((100 + (10 / 12)), 2)
        nxt_balance = helpers.calculate_next_balance(rentability, value)
        self.assertEqual(nxt_balance, true_nxt_balance)

if __name__ == '__main__':
    unittest.main()
