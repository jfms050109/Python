import pyautogui
import time


while True:
    time.sleep(1)
    pyautogui.keyDown('a')
    time.sleep(1)
    pyautogui.keyUp('a')
    time.sleep(1)
    pyautogui.keyDown('d')
    time.sleep(1)
    
    pyautogui.keyUp('d')
