from pandas import ExcelWriter
from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as timeEspera
import pandas as pd

navegador = opcoes.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net")
listaDataFramer = []
linha =1
i =1
while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFramer.append(linhaAtual.text)
        linhaAtual = linha + 1
    i+=1
    timeEspera.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    timeEspera.sleep(2)
else:
    print('Dados salvos com sucesso!')
    navegador.quit()

arquivoExcel = pd.ExcelWriter('dadosAbasSites.xlsx', engine='xlsxwriter')

dataFrame = pd.DataFrame(listaDataFramer, columns=['#;ID;Due Data'])

arquivoExcel: ExcelWriter = pd.ExcelWriter('dadosAbasSites.xlsx', engine='xlsxwriter')
dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

