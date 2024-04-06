from time import sleep
import cv2
import numpy as np
from mss import mss
import pygetwindow
from config import *
import pyautogui

start_box = {'top': 150, 'left': 243, 'width': 1372, 'height': 275}


def start_video():
    sct = mss()
    try:
        window = pygetwindow.getWindowsWithTitle(MKTITLE)[0]
        window.activate()
    except IndexError:
        print(colors['red'] + '[ERROR] The window with the specified title(MKTITLE) was not found')

    while True:
        sleep(0.5)
        sct_img = sct.grab(boxes["menu"][1])
        cv2.imshow('screen', np.array(sct_img))
        try:
            menu = cv2.imread(boxes["menu"][0])
            compare_img = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(colors['red'] + '[ERROR] Error while getting img from screen.', e)

        print(pyautogui.position())
        if ((menu - compare_img) ** 2).mean() < 10 * accuracy:
            print('[INFO] Mortal Combat Menu has been started')
            break

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        #if (cv2.waitKey(0) & 0xFF) == ord('r'):
        #    print(colors['green'] + "YES")
        #    sct_img = sct.grab(boxes["repeat"][1])
        #    cv2.imwrite('src/images/tasks/repeat.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('m'):
        #    sct_img = sct.grab(boxes["menu"][1])
        #    cv2.imwrite('src/images/menu/menu.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('t'):
        #    sct_img = sct.grab(boxes["tasks"][1])
        #    cv2.imwrite('src/images/tasks/tasks.png', np.array(sct_img))
        #if (cv2.waitKey(1) & 0xFF) == ord('c'):
        #    sct_img = sct.grab(boxes["claim"][1])
        #    cv2.imwrite('src/images/tasks/claim.png', np.array(sct_img))



def wait_for(src, box):
    sct = mss()
    print(colors['blue'] + f"[INFO] Start waiting for {src}")
    while True:
        sleep(0.5)
        sct_img = sct.grab(box)
        compare_img1 = cv2.imread(src)
        compare_img2 = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)
        print(((compare_img1 - compare_img2) ** 2).mean())
        if ((compare_img1 - compare_img2) ** 2).mean() < 13 * accuracy:
            print(colors['blue'] + f"[INFO] Waiting for {src} has been ended")
            break
