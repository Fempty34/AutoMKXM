from time import sleep
import cv2
import numpy as np
from mss import mss

import config
from config import *
import time
import pygetwindow as gw


def start_video():
    try:
        window = gw.getWindowsWithTitle(config.MKTITLE)[0]
        print(window)
        window.activate()
        window.maximize()
    except Exception as e:
        print(colors['red'] + "[ERROR] " + str(e))
        print('Окно с указанным заголовком не найдено.')
    print(colors['blue'] + "[INFO] Waiting for MK menu", flush=True)
    sleep(0.5)
    select(boxes["menu"])


def select(src):
    sct = mss()
    print(colors['blue'] + f"[INFO] Start waiting for {src}")
    start_time = time.time()
    while True:
        sleep(0.5)
        sct_img = sct.grab(sct.monitors[0])
        compare_img2 = cv2.cvtColor(np.array(sct_img), cv2.COLOR_BGR2RGB)

        template = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
        template = cv2.cvtColor(np.array(template), cv2.COLOR_BGR2RGB)

        res = cv2.matchTemplate(compare_img2, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= 0.8)
        if len(loc[0]) != 0:
            print(colors['blue'] + f"[INFO] Waiting for {src} has been ended")
            for pt in zip(*loc[::-1]):
                x = pt[0]
                y = pt[1]
            return [x, y]

        if time.time() - start_time > 15 and src != "src/images/menu/menu.png":
            raise RuntimeError(f"[ERROR] Too many times left while waiting for {src}")
