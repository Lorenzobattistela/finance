import unittest
import helpers
import report

class TestHelpers(unittest.TestCase):
    def testInvestmentTypes(self):
        investTypes = ['cash', 'international', 'stocks', 'fii', 'gov']
        types = helpers.get_investment_types()
        self.assertEqual(types, investTypes, 'Should have cash, international, stocks, fii and gov.')
        self.assertCountEqual(types, investTypes)

    def testInvestmentLabel(self):
        investTypes = ['cash', 'international', 'stocks', 'fii', 'gov']
        investLabels = [['storedAt','quantity','rentability'], ['quote','buy_price','quantity','country'], ['quote','buy_price','quantity'],['quote', 'buy_price','quantity','dividend_yield'], ['name','quantity','rentability']]

        for i in range(len(investTypes)):
            labels = helpers.get_investment_label(investTypes[i])
            self.assertEqual(labels, investLabels[i])

        with self.assertRaises(Exception):
            helpers.get_investment_label('saasdasd')

    def testCalculateBalance(self):
        buy_price = 100
        actual_price = 150
        quantity = 10
        true_balance = round(float(((actual_price - buy_price) * quantity)), 2)
        balance = helpers.calculate_balance(buy_price, actual_price, quantity)
        self.assertEqual(balance, true_balance)

    def testCalculateNextBalance(self):
        rentability = 10 #percent
        value = 100 # reais
        true_nxt_balance = round((100 + (10 / 12)), 2)
        nxt_balance = helpers.calculate_next_balance(rentability, value)
        self.assertEqual(nxt_balance, true_nxt_balance)

    def testQuoteIndex(self):
        withQuoteLabels = [['quote','buy_price','quantity','country'], ['quote','buy_price','quantity'],['quote', 'buy_price','quantity','dividend_yield']]

        for label in withQuoteLabels:
            true_index = label.index('quote')
            index = helpers.getQuoteIndex(label)
            self.assertEqual(index, true_index)
        
        noQuoteLabels = [['storedAt','quantity','rentability'], ['name','quantity','rentability']]

        for label in noQuoteLabels:
            index = helpers.getQuoteIndex(label)
            self.assertEqual(index, None)

    def testRentabilityIndex(self):
        withRentabilityLabels = [['storedAt','quantity','rentability'], ['name','quantity','rentability']]
        for label in withRentabilityLabels:
            true_index = label.index('rentability')
            index = helpers.getRentabilityIndex(label)
            self.assertEqual(index, true_index)
        
        noRentabilityLabels = [['quote','buy_price','quantity','country'], ['quote','buy_price','quantity'],['quote', 'buy_price','quantity','dividend_yield']]

        for label in noRentabilityLabels:
            index = helpers.getRentabilityIndex(label)
            self.assertEqual(index, None)

    def testInsertHtmlColumn(self):
        true_html = '<tr><td>someData</td></tr>'
        html = helpers.insertHtmlTableColumn('someLabel')
        self.assertEqual(html, true_html)
        self.assertIn('someLabel', html)

    def testInsertHtmlColumn(self):
        true_html = '<tr><td>someData</td></tr>'
        html = helpers.insertHtmlDataColumn('someData')
        self.assertEqual(html, true_html)
        self.assertIn('someData', html)
    

class TestReport(unittest.TestCase):
    def testHtmlInsertInTemplate(self):
        toInsertHtml = '<div>abcdefg</div>'
        html = report.insert_in_html_template(toInsertHtml)
        self.assertIn(toInsertHtml, html)
    
    def testHtmlWriting(self):
        html = report.write_html()
        with open ('report.html', 'r') as html_file:
            self.assertIsNotNone(html_file)
            firstLine = html_file.readline()
            true_firstLine = '<!DOCTYPE html>\n'
            self.assertEqual(firstLine, true_firstLine)
        html_file.close()


if __name__ == '__main__':
    unittest.main()
