"""
convert list of row tuples to list of row dicts with field name keys
"""
import sqlite3

def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts

conn = sqlite3.connect('data/dbase1')
cursor = conn.cursor()
query  = 'select name, pay from people where pay < ?'
lowpay = makedicts(cursor, query, [70000])
for rec in lowpay: 
    print(rec)
