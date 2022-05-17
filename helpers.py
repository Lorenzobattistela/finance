import sqlite3
import report

# NEED TO ADD A VALIDATION OF DATA TYPE ON DATA_LIST
def insertInDb(table, data_list):
    conn = sqlite3.connect('report.db')
    c = conn.cursor()
    labels = get_investment_label(table)
    labels_query = ''
    for label in labels:
        if labels.index(label) == (len(labels) - 1):
            labels_query += f'{label}'
        else:
            labels_query += f'{label}, '
    
    data_query = ''
    for data in data_list:
        if data_list.index(data) == (len(data_list) - 1):
            data_query += f'"{data}"'
        else:
            data_query += f'"{data}", '

    query = f'INSERT INTO {table} ({labels_query}) VALUES ({data_query});'

    try:
        c.execute(query)
        conn.commit()
        conn.close()
    except:
        raise Exception('Something went wrong with insert query')

def deleteAtIndexDb(table, investment):
    conn = sqlite3.connect('report.db')
    c = conn.cursor()
    labels = get_investment_label(table)
    query = f'DELETE FROM {table} WHERE {labels[0]} = "{investment}";'
    try:
        c.execute(query)
        conn.commit()
        conn.close()
    except:     
        raise Exception('Something went wrong with delete query')

    print(f'Deleted successfully investment at {table}')
    return


def get_investment_types():
    return ['cash', 'international', 'stocks', 'fii', 'gov']

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


def calculate_balance(buy_price, actual_price, quantity):
    buy_price = float(buy_price)
    actual_price = float(actual_price)
    quantity = float(quantity)
    balance = (actual_price - buy_price) * quantity
    return round(balance, 2)
