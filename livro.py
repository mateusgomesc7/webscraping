import requests
from bs4 import BeautifulSoup

def buscar(name, url, classes):
  req = requests.get(url)
  print()
  print(name)

  if req.status_code == 200:
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # print(soup.prettify())

    valor = soup.find("span", class_=classes)
    if not valor:
      valor = soup.find("div", class_=classes)
      if not valor:
        valor = soup.find("i", class_=classes)

    # print(valor)
    print(valor.get_text())
  else:
    print('Não foi legal')

buscar("Americanas","https://www.americanas.com.br/produto/6983188/livro-codigo-limpo-habilidades-praticas-do-agile-software?epar=ZOOM&hl=lower&opn=YSMESP&s_term=YYNKZU&sellerId=4713695000100", "price__SalesPrice-ej7lo8-2 kjGSBk TextUI-sc-12tokcy-0 bLZSPZ")

buscar("submarino" , "https://www.submarino.com.br/produto/6983188/livro-codigo-limpo-habilidades-praticas-do-agile-software?epar=zoom&hl=lower&opn=COMPARADORESSUB&s_term=COMPARADORESSUB&sellerId=4713695000100", "sales-price main-offer__SalesPrice-sc-1oo1w8r-1 kVYfBf TextUI-sc-12tokcy-0 CIZtP")

buscar("altabooks", "https://www.altabooks.com.br/produto/codigo-limpo-habilidades-praticas-do-agile-software/", "woocommerce-Price-amount amount")

buscar("livrariaflorence", "https://www.livrariaflorence.com.br/produto/livro-codigo-limpo-habilidades-praticas-do-agile-software-martin-167512", "precoPor com-precoDe")

buscar("leitura", "https://www.leitura.com.br/produto/codigo-limpo-80660", "js-money")

buscar("amazon", "https://www.amazon.com.br/s?k=codigo+limpo", "a-price-whole")

#https://www.amazon.com.br/s?k=codigo+limpo&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=D4X7IHLFMQKH&sprefix=codigo%2Caps%2C335&ref=nb_sb_ss_ac-o-p_1_6

#https://www.amazon.com.br/s?k=codigo+limpo&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=D4X7IHLFMQKH&sprefix=codigo%2Caps%2C335&ref=nb_sb_ss_ac-o-p_1_6

#https://www.amazon.com.br/s?k=codigo+limpo&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss

#https://www.amazon.com.br/s?k=codigo+limpo&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91

#https://www.amazon.com.br/s?k=codigo+limpo
