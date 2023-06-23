import pyautogui
import webbrowser
from time import sleep
# DESAFIO 🥇

# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.click(988,175,duration=1)
pyautogui.scroll(-2500)
pyautogui.click(866,336,duration=1)
pyautogui.typewrite('Douglas Sarti Quaresma')
# 3) Clique em alerta, para gerar a alerta
pyautogui.click(794,372,duration=1)
# 4) Feche a alerta
pyautogui.click(1199,209,duration=1)
# 5) Suba a página totalmente para cima
pyautogui.press('home')
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos 
# para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
sleep(2)
pyautogui.scroll(-4200)
pyautogui.click(810,232,duration=1)
pyautogui.press('esc')
pyautogui.click(815,348,duration=1)
pyautogui.press('esc')

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU!!',title='Parabéns')


