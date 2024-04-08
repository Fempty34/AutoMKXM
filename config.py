colors = {
    'red': '\033[31m',
    'blue': '\033[34m',
    'green': '\033[32m'
}

MKTITLE = "BlueStacks App Player"
MKCMD = 'C:\\"Program Files\\BlueStacks_nxt\\HD-Player.exe" --instance Pie64 --cmd launchAppWithBsx --package com.wb.goog.mkx --source desktop_shortcut'

accuracy = 8

boxes = {
    "menu": ["src/images/menu/menu.png", {'top': 180, 'left': 360, 'width': 1372, 'height': 275}],
    "tasks": ["src/images/tasks/tasks.png", {'top': 330, 'left': 180, 'width': 1390, 'height': 610}],
    "claim": ["src/images/tasks/claim.png", {'top': 290, 'left': 1220, 'width': 360, 'height': 90}],
    "repeat": ["src/images/tasks/repeat.png", {'top': 900, 'left': 150, 'width': 330, 'height': 60}],
    "start_quest": ["src/images/tasks/start_quest.png", {'top': 810, 'left': 940, 'width': 350, 'height': 80}],
    "continue_quest": ["src/images/tasks/continue_quest.png", {'top': 220, 'left': 1410, 'width': 305, 'height': 65}],

}

current_tasks = [8, 13, 0]
started_tasks = [8]

config_tasks = {
    1: [3, 4, 5, 6, 7],
    2: [8, 9, 10, 11, 12],
    3: [13, 14, 15, 16, 17]
}
config_towers = {
    1: [933, 480],
    2: [800, 520],
    3: [1180, 381]
}