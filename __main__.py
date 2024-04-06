import subprocess
from time import sleep
import os
from dotenv import load_dotenv
import view

from modules import tasks
from config import *

load_dotenv()

cmd = os.getenv('MORTALCOMBATCMD')


def start():
    try:
        subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        print(colors['green'] + "MortalKombat has been launched!")
        sleep(1.5)
        view.start_video()
        tasks.task_handler()
        print(colors['green'] + "Code successfully executed!")
        sleep(2)
    except Exception as e:
        print(colors['red'] + "[ERROR] " + str(e))
    finally:
        subprocess.Popen("taskkill /im HD-Player.exe /f")
        sleep(0.5)
        print(colors["green"], "MortalKombat has been closed!")


if __name__ == "__main__":
    start()
    print(colors['green'] + "Finished!")
