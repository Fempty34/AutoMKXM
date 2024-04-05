import os
from time import sleep
import cv2
import numpy as np
from mss import mss

import win32gui
import win32ui
from ctypes import windll
from PIL import Image


def start_video(pos):
    #sct = mss()
    while True:
        sleep(0.5)
        #sct_img = sct.grab(pos)

        sct_img = get_screen()

        cv2.imshow('screen', np.array(sct_img))
        menu = cv2.imread('src/images/menu.png')
        compare_img = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)

        if ((menu - compare_img) ** 2).mean() < 60:
            print('[INFO] Mortal Combat Menu has been started')
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        if (cv2.waitKey(1) & 0xFF) == ord('s'):
            cv2.imwrite('src/images/daily_reward.png', np.array(sct_img))


def get_screen():
    window_name = os.getenv('MKWINDOWNAME')
    hwnd = win32gui.FindWindow(None, window_name)

    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        # PrintWindow Succeeded
        return im
    else:
        return -1
