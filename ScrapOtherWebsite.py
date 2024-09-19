from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://myanimelist.net/topanime.php?type=bypopularity&limit=0'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find('table', class_='top-ranking-table')
th = table.find_all('th')
title = [t.text.strip() for t in th]

df = pd.DataFrame(columns=title)
tr = table.find_all('tr')

for row in tr[1:]:
    data = row.find_all('td')
    row_data = [d.text.strip() for d in data]
    if len(row_data) == len(title):
        # i added this part to fix the Row data so it can be print
        # Check if the number of data elements in the row matches the number of columns (headers).
        # # This prevents an error when trying to add a row that doesn't fit the structure of the DataFrame.
        # # If there's a mismatch, the row is skipped, and a message is printed for debugging.
        length = len(df)
        df.loc[length] = row_data
    else:
        print(f"Row length mismatch: {row_data}")

df.to_csv('Top Anime by Popularity.csv', index=True)
