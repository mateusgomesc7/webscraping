# fonte: https://blog.geekhunter.com.br/como-fazer-um-web-scraping-python/

from bs4 import BeautifulSoup

import requests

#pegando todo o conteúdo de um requisição get na url do Clima tempo.
html = requests.get("https://www.climatempo.com.br/").content

#criado um objeto chamado soup que está interpretando o documento HTML.
soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

#“span “é a tag html, e “class_=” é a classe atribuída ao elemento
temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# temperatura = soup.find_all("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)

# for link in temperatura:
#   print(link.string)

# Documentação BeautifulSoup:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/