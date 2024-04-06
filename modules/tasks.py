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

        pg.click(config_towers[tower][0], config_towers[tower][1])

        #TODO scroll and start
        for i in range(0, scroll):
            pass

        start = task in started_tasks

        if not start:
            wait_for(boxes['start_quest'][0], boxes['start_quest'][1])
            pg.click(1155, 850)
            sleep(2)

            pg.moveTo(240, 840, 0.7)
            pg.mouseDown(button='left')
            pg.moveTo(240, 470, 0.7)
            pg.moveTo(760, 470, 0.7)
            pg.mouseUp(button='left')

            pg.moveTo(240, 840, 0.7)
            pg.mouseDown(button='left')
            pg.moveTo(240, 470, 0.7)
            pg.moveTo(940, 470, 0.7)
            pg.mouseUp(button='left')

            pg.moveTo(240, 840, 0.7)
            pg.mouseDown(button='left')
            pg.moveTo(240, 470, 0.7)
            pg.moveTo(1035, 470, 0.7)
            pg.mouseUp(button='left')

            wait_for(boxes['continue_quest'][0], boxes['continue_quest'][1])
            pg.click(1567, 250)
            sleep(2)
            pg.click(1243, 943)
            print(colors['green'] + f"[TASKS] Task {task} in tower {tower} has been started successfully")
            started_tasks.append(task)
            sleep(3)
            pg.click(330, 500)
            #TODO DETECT CHANCE
        else:
            wait_for(boxes['claim'][0], boxes['claim'][1], 2)
            pg.click(1400, 340)
            wait_for(boxes['repeat'][0], boxes['repeat'][1])
            pg.click(330, 945)
            print(colors['green'] + f"[TASKS] Task {task} in tower {tower} has been repeated successfully")
            wait_for(boxes['tasks'][0], boxes['tasks'][1])




