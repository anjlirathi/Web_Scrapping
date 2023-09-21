from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
Soup = BeautifulSoup(page.text, 'html')
print(Soup)

Soup.find('table')
Soup.find_all('table')[1]

table = Soup.find_all('table')[1]
print(table)

Soup.find('table', class_ ='wikitable sortable')
Soup.find_all('th')
world_titles = Soup.find_all('th')
world_table_titles = [title.text for title in world_titles]
print(world_table_titles)
world_table_titles1 = [title.text.strip() for title in world_titles]
print(world_table_titles1)

### Since we only need first table so use indexed variables 'table' not 'Soup' Hence
world_titles1 = table.find_all('th')
print(world_titles1)
world_table_titles2 = [ title.text.strip() for title in world_titles1]
print(world_table_titles2)

##importing pandas -- ##  python -m pip install pandas on terminal

import pandas as pd
df = pd.DataFrame(columns = world_table_titles2)
df
column_data = table.find_all('tr')

for row in column_data:
  print(row.find_all('td'))

for row in column_data[1:]:
  row_data = row.find_all('td')
  individual_row_data = [data.text.strip() for data in row_data]
  #print(individual_row_data)
  length = len(df)
  df.loc[length] = individual_row_data

df

df.to_csv(r'C:\Users\Anjli Rathi\Downloads\Softwares\Website Portfolio\Practice\Python\files.csv' , index = False)

df_verify = pd.read_csv(r'C:\Users\Anjli Rathi\Downloads\Softwares\Website Portfolio\Practice\Python\files.csv')
print(df_verify)
