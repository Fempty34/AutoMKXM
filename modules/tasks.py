import pyautogui as pg

from view import *


def task_handler():
    print(colors['blue'] + "[INFO] Task manager has been started")
    sleep(1)
    x, y = select(boxes['tasks_menu'])
    pg.click(x + 10, y + 10)
    sleep(1)
    for task in current_tasks:
        if task not in range(2, 57):
            continue

        tower = 0
        scroll = 0

        for key, value in config_tasks.items():
            if task in value:
                tower = key
                scroll = value.index(task)
                break

        x, y = select(boxes['towers'][tower - 1])
        pg.click(x + 3, y - 4)
        #TODO scroll and start
        for i in range(0, scroll):
            pass

        start = task in started_tasks

        if not start:
            select(boxes['start_quest'])
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

            select(boxes['continue_quest'])
            pg.click(1567, 250)
            sleep(2)
            pg.click(1243, 943)
            print(colors['green'] + f"[TASKS] Task {task} in tower {tower} has been started successfully")
            started_tasks.append(task)
            sleep(3)
            pg.click(330, 500)
            #TODO DETECT CHANCE
        else:
            select(boxes['claim'])
            select(boxes['repeat'])
            print(colors['green'] + f"[TASKS] Task {task} in tower {tower} has been repeated successfully")
            select(boxes['tasks'])
