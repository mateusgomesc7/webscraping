import requests
from bs4 import BeautifulSoup
import time, sys

url = "https://lelivros.love/book/baixar-livro-365-dias-extraordinarios-r-j-palacio-em-pdf-epub-mobi-ou-ler-online/"

def download(soup):
    tempo = 366
    while True:
        aguardando = soup.find("div", class_="download-timer")
        print(aguardando.get_text())
        tem_link = aguardando.find_all('a')
        print(tem_link)
        if not tem_link:
            sys.stdout.write(f"\rAguardando para fazer download. Faltam {str(tempo)} segundos")
            sys.stdout.flush()
            tempo = tempo - 1
            time.sleep(1)
        else:
            link_download = tem_link[0].get('href')
            print("*****************************")
            print()
            print(link_download)
            print()
            print("*****************************")
            break


while True:
    req = requests.get(url)

    if req.status_code == 200:
        content = req.content

        soup = BeautifulSoup(content, 'html.parser')

        valor = soup.find("div", class_="links-download")

        links = valor.find_all('a')
        url_download = links[2].get('href')

        req = requests.get(str(url_download))

        if req.status_code == 200:
            content = req.content

            soup = BeautifulSoup(content, 'html.parser')

            bloqueado = soup.find("ul", class_="pageErrors")

            if bloqueado:
                print("Espere mais 2 minutos...")
                print()
                time.sleep(120)
                continue
            else:
                download(soup)
                break

print("*****************************")
print()
print("PODE BAIXAR!!")
print()
print("*****************************")