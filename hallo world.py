print("hallo world")

import requests
from bs4 import BeautifulSoup

def get_rhine_water_level():
    url = 'https://www.pegelonline.wsv.de/gast/start'
    response = requests.get(url)

    if response.status_code != 200:
        print("Fehler beim Abrufen der Seite.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Suche nach dem Wasserpegel für Bonn
    pegels = soup.find_all('div', class_='pegel')

    for pegel in pegels:
        name = pegel.find('h3').text
        if "Bonn" in name:
            level = pegel.find('span', class_='pegelstand').text
            print(f"Wasserpegel in {name}: {level}")
            return

    print("Wasserpegel für Bonn nicht gefunden.")

if __name__ == '__main__':
    get_rhine_water_level()
