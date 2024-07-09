import pyautogui
import keyboard
import time
# Open Microsoft Word
keyboard.press_and_release('win + r')
time.sleep(1)
pyautogui.typewrite('winword')
time.sleep(1)
keyboard.press_and_release('enter')
# Wait for Word to open
time.sleep(3)
# Type "hello world" into the opened Word document
pyautogui.typewrite("hello world")
# Save the file in current working directory
keyboard.press_and_release('ctrl + s')
time.sleep(1)
pyautogui.typewrite('MyDocument.docx')  # Set your desired filename here
time.sleep(.5)
keyboard.press_and_release('enter')
