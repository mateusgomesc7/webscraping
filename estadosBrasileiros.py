# Fonte: https://goomore.com/blog/web-scraping-python/

from bs4 import BeautifulSoup

import requests

wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea"

html = requests.get(wiki).content

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', class_='wikitable sortable')

#Separe o HTML do texto com o código abaixo
# print(list_item.text.strip())

# print(table)

#gerando a lista em colunas
A=[]
B=[]
C=[]
D=[]
E=[]

for row in table.findAll("tr"): #para tudo que estiver em <tr>
    cells = row.findAll('td') #variável para encontrar <td>
    if len(cells)==5: #número de colunas
        A.append(cells[0].find(text=True)) #iterando sobre cada linha
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find('a').text)
        E.append(cells[4].find(text=True))

#importe o pandas para converter a lista em uma planilha
import pandas as pd

df = pd.DataFrame(index=A, columns=['Posição'])

df['Posição']=A
df['Estado']=B
df['Código/IBGE']=C
df['Capital']=D
df['Área']=E

print(df)