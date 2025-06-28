# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/countries-that-start-with-b/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Use a generic approach to find the first table
# table = soup.find('table')
# rows = table.find('tbody').find_all('tr')
# countries_list = [] 
# for row in rows:
#     dic = {}
#     dic['Country'] = row.find_all('td')[1].text
#     dic['population 2020'] = row.find_all('td')[2].text.replace(',','')
    
#     countries_list.append(dic)
# df = pd.DataFrame(countries_list)
# df.to_excel('countries_data.xlsx', index=False)
# df.to_csv('country_data.csv',index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/countries-that-start-with-b/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Safely find the first table
table = soup.find('table')
if table is None:
    raise ValueError("Table not found on the page.")

rows = table.find('tbody').find_all('tr')
countries_list = []

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:  # Ensure columns exist
        dic = {
            'Country': cols[1].text.strip(),
            'population 2020': cols[2].text.replace(',', '').strip()
        }
        countries_list.append(dic)

df = pd.DataFrame(countries_list)
df.to_excel('countries_data.xlsx', index=False)
df.to_csv('country_data.csv', index=False)
