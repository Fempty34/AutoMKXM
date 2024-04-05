import subprocess
from time import sleep
import os
from dotenv import load_dotenv
import view
from modules import tasks

load_dotenv()

cmd = os.getenv('MORTALCOMBATCMD')
colors = {
    'red': '\033[31m',
    'blue': '\033[34m'
}


def start():
    try:
        subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        print(colors['blue'] + "MortalKombat has been launched!")
        sleep(1.5)
        view.start_video()
        tasks.task_handler()

    except Exception as e:
        print(colors['red'] + "[ERROR] " + str(e))
    finally:
        subprocess.Popen("taskkill /im HD-Player.exe /f")
        print("\n\n[INFO] MortalKombat has been closed!")


if __name__ == "__main__":
    start()
    print(colors['blue'] + "[INFO] Finished")
