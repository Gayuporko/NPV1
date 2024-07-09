import os
from datetime import datetime
import pyautogui
import time
pyautogui.FAILSAFE= False
import subprocess
import keyboard
time.sleep(2)
# subprocess.run("C:\\Program Files\\Notepad++\\notepad++.exe")
# pyautogui.press('win')
# time.sleep(1)
# pyautogui.typewrite('Notepad++')
# time.sleep(1)
# pyautogui.press('enter')
keyboard.press_and_release('win + r')
time.sleep(1)
pyautogui.typewrite('Notepad++')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('ctrl', 'n')
time.sleep(1)
pyautogui.typewrite('Hello')
time.sleep(1)
cwd = "D:\\Jenkins_trail"
# time.sleep(1)
timestamp = datetime.now().strftime("%H%M%S")
file_name = f"example_{timestamp}.txt"
time.sleep(1)
file_path = os.path.join(cwd, file_name)
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.typewrite(file_path)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt','F4')

