import pyautogui as pg

from view import *


def task_handler():
    print(colors['blue'] + "[INFO] Task manager has been started")
    sleep(1)
    pg.click(1500, 280)

    wait_for(boxes['tasks'][0], boxes['tasks'][1])
    for task in current_tasks:
        tower = 0
        scroll = 0

        for key, value in config_tasks.items():
            if task in value:
                tower = key
                scroll = value.index(task)
                break
        print("[INFO] Tower:", tower)
        pg.click(config_towers[tower][0], config_towers[tower][1])
        wait_for(boxes['claim'][0], boxes['claim'][1])

        #TODO scroll and start
        for i in range(0, scroll):
            pass

        start = task in started_tasks

        if not start:
            pg.click(1155, 850)
            sleep(2)
            pg.moveTo(240, 840, 0.5)
            pg.mouseDown(button='left')
            pg.moveTo(760, 470, 0.5)
            pg.mouseUp(button='left')

            pg.moveTo(240 + 156, 840, 0.5)
            pg.mouseDown(button='left')
            pg.moveTo(940, 470)
            pg.mouseUp(button='left')

            pg.moveTo(240 + 156 + 156, 840, 0.5)
            pg.mouseDown(button='left')
            pg.moveTo(1010, 470)
            pg.mouseUp(button='left')

            #TODO DETECT CHANCE
        else:
            pg.click(1400, 340)
            wait_for(boxes['repeat'][0], boxes['repeat'][1])
            pg.click(330, 945)
            print(colors['green'] + f"[TASKS] Task {task} in tower {tower} has been repeated successfully")




