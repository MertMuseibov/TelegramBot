import sqlite3
import matplotlib as plt
import pylab
import random
import time

day = 86400
month = 2592000
year = 31104000


conn = sqlite3.connect('example.db')
cur = conn.cursor()

def sql_command(currency, command_type, first_date, second_date):
    query = '''SELECT {}, updated_time
                      FROM currencyinformation
                           WHERE currency_code = '{}'
                                 AND  updated_time >= {}
                                 AND  updated_time <= {}''' .format(command_type, currency, first_date, second_date )
    cur.execute(query)
    return cur.fetchall()


def draw_plot(currency, command_type, first_date, second_date, period_time):

    data_array = sql_command(currency, command_type, first_date, second_date)

    hour = []
    for i in range(len(data_array)):
        clock = time.ctime(data_array[i][1])
        l = list(map(str, clock.split()))
        z = list(map(str, l[3].split(':')))
        hour.append(float(z[0]) + float(z[1])/60 + float(z[2])/3600)

    y = [data_array[i][0] for i in range(len(data_array))]
    x = [data_array[i][1] for i in range(len(data_array))]
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive']
    plt.plot(x, y, color=random.choice(colors))
    plt.xlabel('{}'.format(period_time), fontweight='normal', fontsize=12)
    plt.ylabel('Dollars', fontweight='normal', fontsize=12)
    plt.title('Change the {} of {}'.format(command_type, currency), fontweight='bold', fontsize=20)
    save = str(time.time())
    pylab.savefig('/home/MertAls/graphics/{}.png'.format(save))
    return save

    """
        hour = []
        for i in range(len(data_array)):
            clock = time.ctime(data_array[i][1])
            l = list(map(str, clock.split()))
            z = list(map(str, l[3].split(':')))
            hour.append(z[0])
        print(hour)
    """



def graphtype(currency, command_type, first_date, second_date):
    time_difference = second_date - first_date
    if second_date - first_date < 0:
        return "Неправильный ввод даты, пожалуйста, повторите."
    elif time_difference < day:
        return draw_plot(currency, command_type, first_date, second_date, 'hour')
    elif time_difference < month:
        return draw_plot(currency, command_type, first_date, second_date, 'day')
    elif time_difference < year:
        return draw_plot(currency, command_type, first_date, second_date, 'month')
    else:
        return draw_plot(currency, command_type, first_date, second_date, 'year')

