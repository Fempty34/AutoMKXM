colors = {
    'red': '\033[31m',
    'blue': '\033[34m',
    'green': '\033[32m'
}

MKTITLE = "BlueStacks App Player"
MKCMD = 'C:\\"Program Files\\BlueStacks_nxt\\HD-Player.exe" --instance Pie64 --cmd launchAppWithBsx --package com.wb.goog.mkx --source desktop_shortcut'

accuracy = 8

boxes = {
    "menu": "src/images/menu/menu.png",
    "tasks": "src/images/tasks/tasks.png",
    "tasks_menu": "src/images/menu/tasks_menu.png",
    "claim": "src/images/tasks/claim.png",
    "repeat": "src/images/tasks/repeat.png",
    "start_quest": "src/images/tasks/start_quest.png",
    "continue_quest": "src/images/tasks/continue_quest.png",
    "towers": ["src/images/tasks/towers/1.png", "src/images/tasks/towers/2.png", "src/images/tasks/towers/3.png"
               "src/images/tasks/towers/4.png", "src/images/tasks/towers/5.png"]
}

current_tasks = []
started_tasks = [8]

config_tasks = {
    1: [3, 4, 5, 6, 7],
    2: [8, 9, 10, 11, 12],
    3: [13, 14, 15, 16, 17],
    4: [18, 19, 20, 21, 22],
    5: [23, 24, 25, 26, 27],
    6: [28, 29, 30, 31, 32],
    7: [33, 34, 35, 36, 37]
}

