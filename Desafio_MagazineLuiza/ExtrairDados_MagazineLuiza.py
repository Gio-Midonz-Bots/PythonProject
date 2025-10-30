from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as time
import pyautogui as funcoesTeclado

navegador = opcoes.Chrome()
navegador.get("https://www.magazineluiza.com.br")
time.sleep(1)
navegador.find_element(By.ID, "suggestion-input").send_keys("geledeiras")
time.sleep(1)