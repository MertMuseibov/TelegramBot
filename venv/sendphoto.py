import telebot
import config
import datetime
from graphics import draw_plot

token = config.token

bot = telebot.TeleBot(token)


def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()



#time1 = 1526826071
#time2 = 1526883180

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if 'show' in message.text:
        command = list(map(str, message.text.split('_')))
        currency_name = command[1]
        command_type = command[2] + '_' + command[3]
        first = []
        second = []
        for i in range(3):
            first.append(int(command[6 - i]))
            second.append(int(command[9-i]))
        first = datetime.datetime(first[0], first[1], first[2], 0, 0, 0)
        second = datetime.datetime(second[0], second[1], second[2], 0, 0, 0)
        time1 = unix_time(first)
        time2 = unix_time(second)
        directory = '/home/mert/Рабочий стол/botproject/graphics'
        file = draw_plot(currency_name, command_type, time1, time2, 'second')
        img = open(directory + '/' + file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()



bot.polling(none_stop=True)