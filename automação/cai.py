import pyautogui
import time
import pyperclip
import random

arrobas=["@jvnq","@jvnqcanal","@jvnq_e_moonkase","@jvnq_moonkase_erik_fan_page"]

while True:
    pyperclip.copy(str(arrobas[random.randrange(1,len(arrobas))])+" "+arrobas[0])
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    time.sleep(4)
    pyautogui.press('enter')
    time. sleep(60)
    
    
