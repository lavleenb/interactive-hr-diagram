import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


url_base = 'https://en.wikipedia.org/wiki/'
with open('stardata.csv', "r", newline='') as csvfile: 
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(spamreader, None) # skips headers
    for csv_row in spamreader:
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }

        url = url_base + csv_row[2]

        req = requests.get(url, headers=header)

        soup = BeautifulSoup(req.text, 'html.parser')
        tables = soup.find_all('table')

        for table in tables: 
            if 'Details' in table.text:
                rows = []
                table_rows = table.find_all('tr')
                for row in table_rows:
                    td = row.find_all('td')
                    row = [row.text for row in td]
                    rows.append(row)
        df = pd.DataFrame(rows)
        lum_index = df.set_index(0).index.get_loc('Luminosity')
        temp_index = df.set_index(0).index.get_loc('Temperature')
        print(df.at[lum_index, 1])
        print(df.at[temp_index, 1])