from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://kworb.net/itunes/'
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find('table', class_ = 'sortable')
th = table.find_all('th')
title = [t.text.strip() for t in th]

df = pd.DataFrame(columns= title)

tr = table.find_all('tr')
for row in tr[1:]:
    data = row.find_all('td')
    row_data = [d.text.strip() for d in data]
    print(row_data)
    length = len(df)
    df.loc[length] = row_data

df.to_csv('Top Artis.csv', index=True)