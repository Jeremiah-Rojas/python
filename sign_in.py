'''
This python script is meant to automate the task of signing into whatever website you choose.
'''

import pyautogui
import subprocess # type: ignore
import time

# Navigates to www.example.com in firefox (You can change the browser by changing the file path accordingly)
subprocess.Popen([r"C:\Program Files\Mozilla Firefox\firefox.exe", "www.example.com"])
time.sleep(5)

# Clicks on the account name
    # To find the position of where you want to click, run the commands:
    #  time.sleep(4)
    #  print(pyautogui.position())
pyautogui.moveTo(922, 619, duration=1) # Duration is how long the mouse will take to get to the specified location; in this case, 1 second.
pyautogui.click()

# Enters in password and presses enter
time.sleep(5)
pyautogui.write("password")
time.sleep(.5)
pyautogui.press("enter")
