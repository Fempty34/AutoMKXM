import subprocess
from time import sleep
import pyautogui
import cv2
import numpy as np
from mss import mss

cmd = ('"C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe" --instance Pie64 --cmd launchAppWithBsx --package '
       '"com.wb.goog.mkx" --source desktop_shortcut')
colors = {
    'red': '\033[31m',
    'blue': '\033[34m'
}
start_box = {'top': 150, 'left': 243, 'width': 1372, 'height': 275}

sct = mss()
try:
    subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    print(colors['blue'] + "MortalKombat has been launched!")

    while True:
        sleep(1)
        sct_img = sct.grab(start_box)
        cv2.imshow('screen', np.array(sct_img))
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        print(pyautogui.position())
except Exception as e:
    print(colors['red'] + "[ERROR] " + str(e))
finally:
    subprocess.Popen("taskkill /im HD-Player.exe /f")
    print("\n\n[INFO] MortalKombat has been closed!")
