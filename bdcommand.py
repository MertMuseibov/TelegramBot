import sqlite3
import requests
import parseee
import logging
from time import sleep




logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

while True:
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    for currency in parseee.currency_code:
        try:
            currency = currency.lower()
            url = 'https://yobit.net/api/2/{}_usd/ticker'.format(currency)
            response = requests.get(url).json()
            if response.get('error'):
                continue
            currency = currency.upper()
            name = parseee.currency_name[parseee.currency_code.index(currency)].lower()
            code = currency
            high = response['ticker']['high']
            low = response['ticker']['low']
            avg = response['ticker']['avg']
            last = response['ticker']['last']
            buy = response['ticker']['buy']
            sell = response['ticker']['sell']
            updated = response['ticker']['updated']
            server = response['ticker']['server_time']
            cur.execute('''
                  INSERT INTO currencyinformation(currency_name, currency_code, high_price, low_price, avg_price, last_price,
                                                  buy_price, sell_price, updated_time, server_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                                                  ,(name, code, high, low, avg, last, buy, sell, updated, server))

            query = '''SELECT * FROM currencyinformation'''
            cur.execute(query)
        #        print(cur.fetchall())
            conn.commit()
            sleep(1)
        except Exception:
            log.exception("Error!")

    conn.close()
    sleep(600)


#conn.close()