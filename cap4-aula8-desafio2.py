import pyautogui
import pyperclip

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(1055,317, duration=1)
escrever('Automação é Incrível')


