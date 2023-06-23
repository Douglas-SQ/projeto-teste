import pyautogui

check=pyautogui.locateCenterOnScreen('check.png')

pyautogui.click(check[0],check[1],duration=1)
