import sqlite3
from dotenv import load_dotenv
import os
import requests

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


def get_investment_types():
    return ['cash', 'international', 'stocks', 'fii', 'gov']

#def insert_investment(typ, )

def retrieve_investment(typ):
    types = get_investment_types()
    if typ not in types:
        raise Exception('Type not accepted.')
    try:
        conn = sqlite3.connect('report.db')
        c = conn.cursor()

    except:
        raise Exception('Something went wrong with the database connection')
    
    data = c.execute(
        '''
        SELECT * FROM {};
    '''.format(typ))
    data = data.fetchall()

    conn.commit()
    return data

def construct_html():
    load_dotenv()
    quote_index = None
    html = '<div>'
    types = get_investment_types()
    for typ in types:
        type_data = retrieve_investment(typ)
        label = get_investment_label(typ)

        if 'quote' in label:
            quote_index = label.index('quote')

        html += f'<h2>{typ}</h2><div class="tables">'

        for i in range(len(type_data)):
            html += '<table>'

            for j in range(len(label)):
                html += f'<tr><th scope="col">{label[j]}</th></tr>'
                html += f'<tr><td>{type_data[i][j]} </td></tr>'

            if quote_index != None:
                actual_price = get_actual_price(type_data[i][quote_index])
             
                html += '<tr><th scope="col">Actual_price</th></tr>'
                html += f'<tr><td >{actual_price}</td></tr>'

                if actual_price != 'Esse símbolo não foi encontrado.':
                    price_index = label.index('buy_price')
                    quantity_index = label.index('quantity')

                    balance = calculate_balance(type_data[i][price_index], actual_price, type_data[i][quantity_index])

                    html += '<tr><th scope="col">Balance</th></tr>'
                    html += f'<tr><td >{balance}</td></tr>'
            html += '</table>'



        html += '</div>'
    html += '</div>'
    doc_html = insert_in_html_template(html)
    return doc_html

def calculate_balance(buy_price, actual_price, quantity):
    buy_price = float(buy_price)
    actual_price = float(actual_price)
    quantity = float(quantity)
    balance = (actual_price - buy_price) * quantity
    return round(balance, 2)

def get_actual_price(quote):
    lower_quote = quote.lower()
    api_key = os.getenv('API_KEY')
    response = requests.get(f'https://api.hgbrasil.com/finance/stock_price?key={api_key}&symbol={lower_quote}')
    response_json = response.json()
    quote_info = response_json['results'][quote]

    try:
        actual_price = quote_info['price']
    except:
        return 'Esse símbolo não foi encontrado.'   
    return actual_price

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
    <h1>Finance Report</h1>
    {html}
</body>
</html>'''
    return html_template

def get_investment_label(typ):
    switch = {
        'cash': ['storedAt','quantity','rentability'],
        'international': ['quote','buy_price','quantity','country'],
        'stocks': ['quote','buy_price','quantity'],
        'fii': ['quote', 'buy_price','quantity','dividend_yield'],
        'gov': ['name','quantity','rentability']
    }
    choosen = switch.get(typ, 'default')
    if choosen == 'default':
        raise Exception('Erro: insira uma opção disponível')
    return choosen

def write_html():
    html = construct_html()
    file = open('report.html', 'w')
    file.write(html)
    file.close()
    return