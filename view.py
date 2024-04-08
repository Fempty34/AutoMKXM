from time import sleep
import cv2
import numpy as np
from mss import mss
import pygetwindow
from config import *
import pyautogui
import time

def start_video():
    sct = mss()
    #try:
    #    window = pygetwindow.getWindowsWithTitle(MKTITLE)[0]
    #    window.activate()
    #except IndexError:
    #    raise RuntimeError('[ERROR] The window with the specified title(MKTITLE) was not found')

    print(colors['blue'] + "[INFO] Waiting for MK menu", flush=True)
    while True:
        sleep(0.5)
        sct_img = sct.grab(boxes["menu"][1])
        #cv2.imshow('screen', np.array(sct_img))
        try:
            menu = cv2.imread(boxes["menu"][0])
            compare_img = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(colors['red'] + '[ERROR] Error while getting img from screen.', e)

        #print(((menu - compare_img) ** 2).mean())
        if ((menu - compare_img) ** 2).mean() < 10 * accuracy:
            print('[INFO] Mortal Combat Menu has been started')
            sleep(1)
            break
        #print(pyautogui.position())

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        #if (cv2.waitKey(0) & 0xFF) == ord('s'):
        #    print(colors['green'] + "YES")
        #    sct_img = sct.grab(boxes["continue_quest"][1])
        #    cv2.imwrite('src/images/tasks/continue_quest.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('m'):
        #    sct_img = sct.grab(boxes["menu"][1])
        #    cv2.imwrite('src/images/menu/menu.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('t'):
        #    sct_img = sct.grab(boxes["tasks"][1])
        #    cv2.imwrite('src/images/tasks/tasks.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('c'):
        #    sct_img = sct.grab(boxes["claim"][1])
        #    cv2.imwrite('src/images/tasks/claim.png', np.array(sct_img))


def wait_for(src, box, pow=10):
    sct = mss()
    print(colors['blue'] + f"[INFO] Start waiting for {src}")
    start_time = time.time()
    while True:
        sleep(0.5)
        sct_img = sct.grab(box)
        compare_img1 = cv2.imread(src)
        compare_img2 = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)
        #print(((compare_img1 - compare_img2) ** 2).mean())
        if ((compare_img1 - compare_img2) ** 2).mean() < pow * accuracy:
            print(colors['blue'] + f"[INFO] Waiting for {src} has been ended")
            break
        if time.time() - start_time > 15:
            raise RuntimeError(f"[ERROR] Too many times left while waiting for {src}")


