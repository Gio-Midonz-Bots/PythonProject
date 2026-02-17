from bs4 import BeautifulSoup
from pyexpat import features

html_file = open("../Material_de_Apoio/data_in_table_2.html", mode="r", encoding="utf-8")

soup = BeautifulSoup(html_file, features="html.parser")

table = soup.find_all('table')[1]
table_rows = table.find_all('tr')
#print(table)
Dados_Cursos =[]

for i in table_rows:
    colunas = i.find_all('td')
    if len(colunas) > 0:
        nome_curso = colunas[0].text
        intersse = colunas[1].text
        dict_curso = {
            'Curso': nome_curso,
            'Interesse': intersse
        }
        Dados_Cursos.append(dict_curso)
print(Dados_Cursos)