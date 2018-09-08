from flask import Flask
from flask import request
from flask import jsonify
from parseee import parse_text
from parseee import get_price
import matplotlib as plt
import telebot
import description
import config
import requests
import json
import re

from flask_sslify import SSLify




app = Flask(__name__)
sslify = SSLify(app)

token = config.token
bot = telebot.TeleBot(token)
URL = 'https://api.telegram.org/bot' + str(token) + '/'


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


"""
def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()
"""



def send_message(chat_id, text='Молодой человек, Вы плохо себя ведете...'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
#            photo_command = list(map(str, parse_text(message).split('_')))
            if parse_text(message) == 'start':
                send_message(chat_id, text=description.greeting)
            elif parse_text(message) == 'help':
                send_message(chat_id, text=description.help)
            elif parse_text(message) == 'photo':
                x = [x for x in range(5)]
                y = [y for y in range(5)]
                plt.plot(x, y)
                bot.send_chat_action(chat_id, 'upload_photo')
                bot.send_photo(chat_id, plt)

            else:
                price = get_price(parse_text(message))
                send_message(chat_id, text=price)
        else:
            send_message(chat_id, text='Молодой человек, Вы плохо себя ведете...')


        # write_json(r)
        return jsonify(r)
    return '<h1> Bot welcomes you </h1>'




if __name__ == '__main__':
    app.run()