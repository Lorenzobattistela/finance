import sqlite3

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
    html = '<div>'
    types = get_investment_types()
    for typ in types:
        type_data = retrieve_investment(typ)
        label = get_investment_label(typ)
        for i in range(len(type_data)):
            html += f'<p>Label: {label[i]}</p><br>'
            html += f'<p>Data: {type_data[i]}</p><br>'
    html += '</div>'
    return html

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
#file = open('report.html', 'w')

