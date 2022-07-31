import pyautogui 
import time 

time.sleep(5)

repetir = 10 

for _ in range (repetir):

    file = open('lapotah.txt', 'r', encoding='utf-8')
    time.sleep(2)
    for frase in file:
        pyautogui.typewrite(frase)
        time.sleep(2)
        pyautogui.press('enter')
