from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as time
import pyautogui as funcoesTeclado

navegador = opcoes.Chrome()
navegador.get("https://www.magazineluiza.com.br")
time.sleep(2)
navegador.find_element(By.ID, "suggestion-input").send_keys("geledeiras")
time.sleep(2)
funcoesTeclado.press("enter")
time.sleep(2)

listaProdutos = navegador.find_elements(By.CLASS_NAME,"BCSuy" )

for item in listaProdutos:
    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME,"BCSuy").text

        except Exception:
            pass
    elif precoProduto == "":
        try:
            nomeProduto = item.find_element(By.CLASS_NAME,"sc-kOjCZu" ).text
        except Exception:
            pass
            print(nomeProduto)