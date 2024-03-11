import pyautogui
import time


while True:
    time.sleep(20)
    pyautogui.moveTo(32, 313)
    pyautogui.click()
    time.sleep(20)
    pyautogui.moveTo(29, 265)
    pyautogui.click()

#print(pyautogui.position())