import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Set headers and URL
headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://myanimelist.net/topanime.php?type=bypopularity&limit=0'

# Request page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the anime ranking table
table = soup.find('table', class_='top-ranking-table')

# Extract table headers
th = table.find_all('th')
columns = [t.text.strip() for t in th]

# Prepare the CSV file
with open('Top_Anime_by_Popularity.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Title', 'Score', 'Your Score', 'Status'])  # Define headers explicitly

    # Extract table rows
    for row in table.find_all('tr')[1:]:
        data = row.find_all('td')

        # Extract relevant columns (Rank, Title, Score, Your Score, Status) if they exist
        # i added this part to fix the Row data so it can be print
        # Check if the number of data elements in the row matches the number of columns (headers).
        # # This prevents an error when trying to add a row that doesn't fit the structure of the DataFrame.
        # # If there's a mismatch, the row is skipped, and a message is printed for debugging.
        if len(data) >= 5:
            rank = data[0].text.strip()
            title = data[1].text.strip()
            score = data[2].text.strip()
            your_score = data[3].text.strip()
            status = data[4].text.strip()

            writer.writerow([rank, title, score, your_score, status])
        else:
            print(f"Row length mismatch: {[d.text.strip() for d in data]}")

print("Scraping complete. Data saved to 'Cleaner_Top_Anime_by_Popularity.csv'.")

#By Ris, diffrent as the first one by making it cleaner and the explanation of it abit
