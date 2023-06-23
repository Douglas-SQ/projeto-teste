import pyautogui
from time import sleep

pyautogui.moveTo(901,396,duration=1)
for i in range(100):
    
    posicaox=pyautogui.position()[0]
    posicaoy=pyautogui.position()[1]

    if posicaox ==901 and posicaoy==396:
        sleep(0.1)
        pyautogui.click()
    else:
        pyautogui.moveTo(901,396,duration=1)
        sleep(0.1)
        pyautogui.click()



