
import pandas as pd
import requests

from bs4 import BeautifulSoup


url = 'http://www.espn.com/nba/salaries/_/year/2016'
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
column_headers  = soup.find_all('tr', class_='colhead')


for name in column_headers:
    
    lis = name.find_all('td')
      
column = [li.getText() for li in lis]

data_row_odd = soup.find_all('tr', {'class':['oddrow','evenrow']})


player_data_02 = []  

for i in range(len(data_row_odd)):
    player_row = []  

    for td in data_row_odd[i].findAll('td'):        
        
        player_row.append(td.getText())        

    player_data_02.append(player_row)

df = pd.DataFrame(player_data_02, columns=column)

url_template = 'http://www.espn.com/nba/salaries/_/year/2016/page/{page}'
for page in range(2, 12):  
    url = url_template.format(page=page) 
    
    r = requests.get(url)

    soup = BeautifulSoup(r.text,"lxml")
    column_headers  = soup.find_all('tr', class_='colhead')


    for name in column_headers:
    
        lis = name.find_all('td')
      
    column = [li.getText() for li in lis]
    data_row_odd = soup.find_all('tr', {'class':['oddrow','evenrow']})


    player_data_02 = []  

    for i in range(len(data_row_odd)): 
        player_row = []  

    
        for td in data_row_odd[i].findAll('td'):        
        
            player_row.append(td.getText())        

    
        player_data_02.append(player_row)
    df2 = pd.DataFrame(player_data_02, columns=column)
    
    df = df.append(df2, ignore_index=True)

print df
df.rename(columns = {'NAME':'Player'}, inplace = True)
df.to_csv('nbasalaries.csv',encoding='utf-8')
