from time import sleep
import cv2
import numpy as np
from mss import mss


def start_video(pos):
    sct = mss()
    while True:
        sleep(0.5)
        sct_img = sct.grab(pos)
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
