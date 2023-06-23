import pyautogui
import pyperclip

pyautogui.alert(text='Iniciando automação',title='alerta')
email=pyautogui.prompt(text='Informe o seu e-mail',title='Informações')
senha=pyautogui.password(text='Informe a sua senha',title='senha',mask='*')
pyautogui.click(922,263,duration=1)

pyperclip.copy(email)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyperclip.copy(senha)
pyautogui.hotkey('ctrl','v')

resposta=pyautogui.confirm(text='deseja continuar?',buttons=['sim','não'])
pyautogui.alert(text=resposta,title='confirmação')
