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
        format_star_name = csv_row[2].split(' ')
        url = url_base + "_".join(format_star_name)
        print(url)

        req = requests.get(url, headers=header)

        soup = BeautifulSoup(req.text, 'html.parser')
        tables = soup.find_all('table')

        incomplete_info_stars = []
        for table in tables: 
            if 'Details' in table.text:
                rows = []
                table_rows = table.find_all('tr')
                for row in table_rows:
                    td = row.find_all('td')
                    row = [row.text for row in td]
                    if (len(row) > 0):
                        if (row[0] == 'Luminosity' or row[0] == 'Temperature'):
                            rows.append(row)
                        else:
                            incomplete_info_stars.append(row)
        df = pd.DataFrame(rows)
        if (not df.empty):
            print(df)
        
            lum_index = 0
            temp_index = 1
            if (df[0].nunique() > 1): # if there is only one temperature or luminosity, use the indexing.
                print(df.at[lum_index, 1])
                print(df.at[temp_index, 1]) # we do this because some stars don't have luminosity or temperature. those
                # will be filtered out before feeding into the graph.
            else: 
                print(df.at[0,0], df.at[0, 1]) # if there are multiple temperatures or luminosities for member stars,
                # we take the first instance of both, as I can trust that wikipedia places the A member star first.