import pyautogui as escolha_opcao
import pyautogui as timeslep
import pyautogui as abrirArquivos

opcao = escolha_opcao.confirm('Clique no botão desejado',
                              buttons=['Excel', 'Word','Notepad'])

if opcao == 'Excel':
    print('você escolheu Excel')

    abrirArquivos.hotkey('win','r')
    timeslep.sleep(2)
    abrirArquivos.typewrite('excel')
    timeslep.sleep(2)
    abrirArquivos.press('enter')
elif opcao == 'Word':
    print('voce escolheu Word')
    abrirArquivos.hotkey('win','r')
    timeslep.sleep(2)
    abrirArquivos.typewrite('winword')
    timeslep.sleep(2)
    abrirArquivos.press('enter')
else:
    print('voce escolheu Notepad')

    abrirArquivos.hotkey('win','r')
    timeslep.sleep(2)
    abrirArquivos.typewrite('notepad')
    timeslep.sleep(2)
    abrirArquivos.press('enter')
    timeslep.sleep(2)
    escolha_opcao.typewrite('Voce abriu o Notepad')