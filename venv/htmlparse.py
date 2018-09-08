import urllib.request

from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()



def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody', class_='row-hover')
    rows = tbody.find_all('tr')
    currency_name = []
    currency_code = []
    for crypto in rows:
        currency_name.append(crypto.find('td', class_='column-1').text)
        currency_code.append(crypto.find('td', class_='column-2').text)
    return currency_name, currency_code




def mainn():
    return parse(get_html('http://promining.su/spisok-kriptovalyut-s-algoritamami/'))

if __name__ == '__main__':
        mainn()