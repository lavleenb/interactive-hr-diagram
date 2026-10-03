import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Mirach'

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

req = requests.get(url, headers=header)

soup = BeautifulSoup(req.text, 'html.parser')
tables = soup.find_all('table')

for table in tables: 
    if 'Details' in table.text:
        #col_headers = [col_header.text.strip() for col_header in table.find_all('th')]
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