import requests
from bs4 import BeautifulSoup


req = 0
page = 43

with open('CBF.TXT', 'w') as f:
    f.write("Começo")


def scrapeCBF():

    with open('CBF.TXT', 'a') as f:
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('div', id='app')
        app = s.find('main', id='menu-panel')
        container = app.find('div', class_='container')
        row = container.find('div', class_='row')
        col = row.find('div', class_='col-md-12 col-lg-12')
        table = col.find('table', class_='table m-t-30')
        hlines = table.find('thead')
        blines = table.find('tbody')

        for il in hlines.find('tr'):
            f.write(il.text)
            print(il.text)
        for i in blines.find_all('tr'):
            f.write(i.text)
            print(i.text)

        f.write("fim")


while req != page:
    req = req + 1
    r = requests.get(
        f"https://www.cbf.com.br/futebol-brasileiro/atletas/campeonato-brasileiro-serie-a/2022?atleta=&page={req}")
    scrapeCBF()
    print(req)


print("Terminou")
