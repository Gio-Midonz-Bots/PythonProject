'''
INTRODUÇÃO A BIBLIOTECA BEAUTIFUL SOUP

para instalação utilizar = pip install beautifulsoup

função .find ou .find_all = pega os elementos html

Esse é uma forma de percorrer o html e retornar a tag que você está procurando
for i in soup.find_all('a'):
    i['href']
pdb = É uma biblioteca que permite a interação com os dados.
th -> cabeçalho
tr -> linhas
td -> colunas
'''

#Importando a biblioteca
from bs4 import BeautifulSoup

#Abrindo o arquivo
html_file = open("../Material_de_Apoio/data_in_table.html", mode="r", encoding="utf-8")

#Criando objeto Soup
#Nesta linha, o BeautifulSoup entra em ação. Ele pega o conteúdo bruto do arquivo e o transforma em um objeto estruturado (a variável soup). O argumento features="html.parser" avisa ao Python para usar o analisador padrão interno para entender a estrutura do HTML.
soup = BeautifulSoup(html_file, features="html.parser")

#Localizando a table pelo id
table = soup.find(id='main_table')

#Extraindo as linhas da tabela e printando
table_rows = table.find_all('tr')
#print(table_rows)

dados_alunos = []
#Criar uma lista para pecorrer todas as linhas
for i in table_rows:
    colunas = i .find_all('td')
    if len(colunas) > 0:
        Codigo_Estudade = colunas[0].text
        Codigo_Nome = colunas[1].text
        Codigo_Notas = colunas[2].text

        dict_alunos = {
            'Codigo_Estudade': Codigo_Estudade,
            'Codigo_Nome': Codigo_Nome,
            'Codigo_Notas': Codigo_Notas
        }
        dados_alunos.append(dict_alunos)
        print(f'O ID do aluno:{Codigo_Estudade}\nNome:{Codigo_Nome} e sua nota {Codigo_Notas}')

print(dados_alunos)

