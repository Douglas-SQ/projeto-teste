import pyautogui
import webbrowser
from time import sleep
# DESAFIO 🥇

# entrar na última publicaçao

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

pyautogui.move(0,40,duration=1)
pyautogui.click()
# verificar se já foi curtida
sleep(4)

curtida=pyautogui.locateCenterOnScreen('curtida.png')
naocurtida=pyautogui.locateCenterOnScreen('naocurtida2.png')
# senão foi curtido, curtir e comentar
print(naocurtida)
if naocurtida != None:
    pyautogui.click(naocurtida[0],naocurtida[1],duration=1)
    comentar=pyautogui.locateCenterOnScreen('comentar.png')
    pyautogui.click(comentar[0],comentar[1],duration=1)
    sleep(1)
    comentario=pyautogui.locateCenterOnScreen('comentario.png')
    pyautogui.click(comentario[0],comentario[1],duration=1)
    pyautogui.typewrite('Top!')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('esc')

# print(pyautogui.KEYBOARD_KEYS)
# lista=pyautogui.KEYBOARD_KEYS
# for item in lista:
#     print(item)



# senão foi curtido, curtir e comentar
# se já foi curtida não fazer nada
# pausar o bot por 24 horas.
