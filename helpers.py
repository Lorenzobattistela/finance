import sqlite3
import report

# NEED TO ADD A VALIDATION OF DATA TYPE ON DATA_LIST
def insertInDb(table, data_list):
    conn = sqlite3.connect('report.db')
    c = conn.cursor()
    labels = report.get_investment_label(table)
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

