from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By

navegador = opcoes.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net")
linha =1
i =1
while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    for linhaAtual in linhas:
        print(linhaAtual.text)

        linhaAtual = linha + 1
    i+=1


