from time import sleep

import pyautogui as pg


current_tasks = [4]
started_tasks = [4]

config_tasks = {
    1: [1, 2, 3],
    2: [4]
}
config_towers = {
    1: [933, 480],
    2: [800, 520]
}

def task_handler():
    print("[INFO] Task manager has been started")
    sleep(1)
    pg.click(1500, 280)
    sleep(3)
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
        sleep(3)

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
            sleep(3)
            pg.click(330, 945)
            sleep(10)



