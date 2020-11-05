import pandas as pd
import requests
from bs4 import BeautifulSoup

#Este método retorna um objeto Response que contém vários informações, das quais utilizaremos o status_code para verificar se a requisição retornou um status 200, indicando que ela foi bem sucedida, e content para acessar o código da página HTML.
req = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

table_str = str(table)
# o retorno deste método é sempre uma lista de Data Frames, e portanto devemos acessar a posição 0 dela para obter nossa tabela.
df = pd.read_html(table_str)[0]


def scrape_stats(base_url, year_start, year_end):
    years = range(year_start,year_end+1,1)

    final_df = pd.DataFrame()

    for year in years:
        print('Extraindo ano {}'.format(year))
        req_url = base_url.format(year)
        req = requests.get(req_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.find('table', {'id':'totals_stats'})
        df = pd.read_html(str(table))[0]
        df['Year'] = year
        final_df = final_df.append(df)
    return final_df
url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'
df = scrape_stats(url, 2013, 2018)

# print(df)

drop_indexes = df[df['Rk'] == 'Rk'].index # Pega indexes onde a coluna 'Rk' possui valor 'Rk'
df.drop(drop_indexes, inplace=True) # elimina os valores dos index passados da tabela

numeric_cols = df.columns.drop(['Player','Pos','Tm'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)

import matplotlib.pyplot as plt
import seaborn as sns

sns.barplot(x='Year', y='3PA', data = df)