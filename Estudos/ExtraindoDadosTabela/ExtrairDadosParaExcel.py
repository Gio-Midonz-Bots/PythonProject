from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By

import pandas as pd
navegador = opcoes.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')

colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

dataFramerLista = []
linha = 1
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFramerLista.append(linhaAtual.text)
    linha += 1

arquivoExcel = pd.ExcelWriter('dadosSites.xlsx', engine='xlsxwriter')

arquivoExcel.save()

dataFrame = pd.DataFrame(dataFramerLista, columns=['Dados'])
arquivoExcel = pd.ExcelWriter('dadosSites.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1', index=True)

arquivoExcel.save()