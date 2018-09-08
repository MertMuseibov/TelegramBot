import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()



cur.execute('''
        CREATE TABLE currencyinformation(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        currency_name VARCHAR(255),
        currency_code VARCHAR(255),
        high_price FLOAT,
        low_price FLOAT,
        avg_price FLOAT,
        last_price FLOAT,
        buy_price FLOAT,
        sell_price FLOAT,
        updated_time INTEGER,
        server_time INTEGER 
        )
''')

conn.commit()
conn.close()