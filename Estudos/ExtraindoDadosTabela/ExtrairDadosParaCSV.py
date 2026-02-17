from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pyautogui as time

driver = webdriver.Chrome()
driver.get('https://clone-olx-devaprender.netlify.app')
time.sleep(3)
produto = driver.find_elements(By.XPATH, '//*[@id="root"]/div/main/div[2]/div[1]/div[2]/h3')
preco = driver.find_elements(By.XPATH,'//*[@id="root"]/div/main/div[2]/div[1]/div[2]/div[1]/span')

for produto,preco in zip(produto,preco):
    with open('Produtos.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{produto.text},{preco.text},{os.linesep}')
