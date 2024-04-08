import subprocess
from time import sleep
import os
import view
import psutil

from modules import tasks
from config import *


def start():
    try:
        subprocess.Popen(MKCMD + " /user:Administrator", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        print(colors['green'] + "MortalKombat has been launched!")
        sleep(1.5)
        for proc in psutil.process_iter():
            if proc.name() == 'BlueStacks X.exe':
                proc.terminate()
        view.start_video()
        tasks.task_handler()
        print(colors['green'] + "Code successfully executed!")
        sleep(2)
    except Exception as e:
        print(colors['red'] + "[ERROR] " + str(e))
    finally:
        subprocess.Popen("taskkill /im HD-Player.exe /f")
        sleep(0.5)
        print(colors["green"] + "MortalKombat has been closed!")


if __name__ == "__main__":
    os.system('python app/app.py')
    #start()
    print(colors['green'] + "Finished!")
