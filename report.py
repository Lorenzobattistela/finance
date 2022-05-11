import sqlite3

def defaultConfig():
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


#file = open('report.html', 'w')

