import requests
from bs4 import BeautifulSoup

#requisição de site
page = requests.get('https://www.gabrielcasemiro.com.br')

#Retorna o html da pagina
if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href', " "))
else:
    print("HTTP error", page.status_code)

