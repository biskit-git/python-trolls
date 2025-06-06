import pyautogui
import subprocess
import time

def mouse_msedge():
 while True:
  time.sleep(0.001)
  pyautogui.mouseDown(520, 450, duration=5)

while True:
        time.sleep(0.001)
        subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

mouse_msedge()
