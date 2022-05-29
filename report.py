import sqlite3
from dotenv import load_dotenv
import helpers
import api

def defaultConfig():
    try:
        conn = sqlite3.connect('report.db')
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS cash ([storedAt] TEXT, [quantity] REAL, [rentability] REAL)
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS international ([quote] TEXT, [buy_price] REAL, [quantity] REAL, [country] TEXT)
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS stocks ([quote] TEXT, [buy_price] REAL, [quantity] REAL) 
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS fii ([quote] TEXT, [buy_price] REAL, [quantity] REAL, [dividend_yield] REAL)
        ''')
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS gov ([name] TEXT, [quantity] REAL, [rentability] REAL)
        ''')
        
        conn.commit()
    except:
        raise Exception('Something went wrong with the database connection.')

def construct_html():
    load_dotenv()
    html = '<div>'
    types = helpers.get_investment_types()
    for typ in types:
        type_data = helpers.retrieve_investment(typ)
        label = helpers.get_investment_label(typ)

        quote_index = helpers.getQuoteIndex(label)
        rentability_index = helpers.getRentabilityIndex(label)
        if rentability_index == None:
            quantity_index = None
        else:
            quantity_index = helpers.getQuantityIndex(label)
        
        html += f'<h2>{typ}</h2><div class="tables">'

        for i in range(len(type_data)):
            html += '<table>'

            for j in range(len(label)):
                html += helpers.insertHtmlTableColumn(label[j])
                html += helpers.insertHtmlDataColumn(type_data[i][j])

            if rentability_index != None:
                next_month = helpers.calculate_next_balance(type_data[i][rentability_index], type_data[i][quantity_index])

                html += helpers.insertHtmlTableColumn("Expected Balance Next Month")
                html += helpers.insertHtmlDataColumn(next_month)

            if quote_index != None:
                actual_price = api.get_actual_price(type_data[i][quote_index])

                html += helpers.insertHtmlTableColumn("Actual Price")
                html += helpers.insertHtmlDataColumn(actual_price)

                if actual_price != 'Esse símbolo não foi encontrado.':
                    price_index = label.index('buy_price')
                    quantity_index = label.index('quantity')

                    balance = helpers.calculate_balance(type_data[i][price_index], actual_price, type_data[i][quantity_index])

                    html += helpers.insertHtmlTableColumn("Balance")
                    html += helpers.insertHtmlDataColumn(balance)

            totalBalance = helpers.getTotalBalance()   
            html += '</table>'
        html += '</div>'
    html += f'<h1 class="title">Total Balance: {totalBalance}</h1>'
    html += f'<small class="title">Essa quantidade não conta prejuízos não retirados nos investimento. Para o valor real, diminua ou aumente os Balances de cada ação.</small>'
    html += '</div>'
    doc_html = insert_in_html_template(html)
    return doc_html




def insert_in_html_template(html):
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="report.css" />
    <title>Finance Report</title>
</head>
<body>
    <h1 class="title">Finance Report</h1>
    {html}
</body>
</html>'''
    return html_template


def write_html():
    html = construct_html()
    file = open('report.html', 'w')
    file.write(html)
    file.close()
    return