import pyautogui
import webbrowser
from time import sleep
# DESAFIO 🥇
# entrar na página do instagram
webbrowser.open('https://www.instagram.com')
# fazer login
logo_insta=pyautogui.locateCenterOnScreen('logo_insta.png')
pyautogui.moveTo(logo_insta[0],logo_insta[1],duration=1)
pyautogui.move(0,80,duration=1)
pyautogui.click()
pyautogui.typewrite('douglashdcloud.cursos@gmail.com')
pyautogui.press('tab')
pyautogui.typewrite('instagram@1218')
entra=pyautogui.locateCenterOnScreen('entra_insta2.png')
pyautogui.click(entra[0],entra[1],duration=1)
sleep(5)
agoranao=pyautogui.locateCenterOnScreen('agora_nao.png')
pyautogui.click(agoranao[0],agoranao[1],duration=1)
# pesquisar página para curtir
sleep(8)
pesquisa=pyautogui.locateCenterOnScreen('pesq_insta.png')
pyautogui.click(pesquisa[0],pesquisa[1],duration=1)
pyautogui.typewrite('nike')
# clicar no link da página
sleep(5)
nike=pyautogui.locateCenterOnScreen('nike.png')
pyautogui.click(nike[0],nike[1],duration=1)

# entrar na última publicaçao
sleep(8)
publi1=pyautogui.locateCenterOnScreen('publicações_ativo.png')
publi2=pyautogui.locateCenterOnScreen('publicações_inativo.png')
publi3=pyautogui.locateCenterOnScreen('publicações_menor_ativo.png')
publi4=pyautogui.locateCenterOnScreen('publicações_menor_inativo.png')
if publi1 != None:
    pyautogui.click(publi1[0],publi1[1],duration=1)
elif publi2!=None:
    pyautogui.click(publi2[0],publi2[1],duration=1)
elif publi3!=None:
    pyautogui.click(publi3[0],publi3[1],duration=1)
elif publi4!=None:
    pyautogui.click(publi4[0],publi4[1],duration=1)





# verificar se já foi curtida
# senão foi curtido, curtir e comentar
# se já foi curtida não fazer nada
# pausar o bot por 24 horas.
