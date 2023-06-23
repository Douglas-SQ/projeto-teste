import pyautogui
import pyperclip

email=pyautogui.prompt(text='Informe o seu e-mail',title='Informações')
senha=pyautogui.password(text='Informe a sua senha',title='senha',mask='*')

pyperclip.copy(email)
