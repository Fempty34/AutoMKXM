import flet as ft
import flet_core
import math
import pystray
from PIL import Image

from main import start
import config

tray_image = Image.open("src/images/app/tray_img.png")


def exit_app(icon, query):
    icon.stop()
    p.window_destroy()
    print("The App was closed/exited successfully!")


def default_item_clicked(icon, query):
    icon.visible = False
    p.window_skip_task_bar = False
    p.window_maximized = True
    p.update()
    print("Default button was pressed.")


tray_icon = pystray.Icon(
    name="Test",
    icon=tray_image,
    title="Flet in tray",
    menu=pystray.Menu(
        pystray.MenuItem(
            "Open App",
            default_item_clicked,  # alternative/broader callback: menu_item_clicked
            default=True  # set as default menu item
        ),
        pystray.MenuItem(
            "Close App",
            exit_app  # alternative/broader callback: menu_item_clicked
        )
    ),
    visible=False,
)


def on_window_event(e):
    if e.data == "minimize":
        tray_icon.visible = True
        p.window_skip_task_bar = True
    elif e.data == "restore":
        tray_icon.visible = False
        p.window_skip_task_bar = False
    elif e.data == "close":
        tray_icon.stop()
        e.page.window_destroy()

    p.update()


def main(page: ft.Page):
    global p
    p = page

    def write_occure(e):
        accuracy_count.value = "Current accuracy: " + str(math.ceil(accuracy_slider.value))
        page.update()

    def save_config(es):
        try:
            config.MKCMD = mkcmd_input.value.replace("\"", "\\")
            config.MKTITLE = mktitle_input.value
            config.accuracy = accuracy_slider.value

            config.current_tasks = [int(selected_task_1.value), int(selected_task_2.value), int(selected_task_3.value)]
            for tower, pos in config.config_towers.items():
                config.config_towers[tower] = [tower_config.rows[tower - 1].cells[1].content.value,
                                               tower_config.rows[tower - 1].cells[2].content.value]
            tray_icon.visible = True
            p.window_skip_task_bar = True
            p.window_minimized = True
            p.update()
            start()

        except Exception as e:
            dlg = ft.AlertDialog(
                title=ft.Text("Error", weight=ft.FontWeight.BOLD, color="#76ABAE", size=20),
                bgcolor="#31363F",
                content=ft.Text("Error while saving config:\n" + str(e), color="#EEEEEE", size=14)
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    page.on_window_event = on_window_event
    page.window_prevent_close = True
    page.title = "Configurate AutoMKXM"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_height = 568
    page.window_width = 340
    page.window_bgcolor = "#222831"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_visibility=False,
            thumb_color={
                ft.MaterialState.HOVERED: "#76ABAE",
                ft.MaterialState.DEFAULT: "#31363F",
            },
            thickness=0,
            radius=5,
            main_axis_margin=0,
            cross_axis_margin=0,
        )

    )

    mkcmd_input = ft.TextField(value=config.MKCMD, label="Location of MK", color="#EEEEEE", border_radius=10,
                               border_color="#31363F", border_width=2, cursor_color="#EEEEEE")
    mktitle_input = ft.TextField(value=config.MKTITLE, label="Title of MK", color="#EEEEEE", border_radius=10,
                                 border_color="#31363F", border_width=2, cursor_color="#EEEEEE")
    accuracy_slider = flet_core.CupertinoSlider(divisions=14, max=15, min=1, value=config.accuracy,
                                                active_color="#76ABAE",
                                                thumb_color="#31363F", on_change=write_occure)
    accuracy_count = ft.Text("Current accuracy: " + str(config.accuracy), text_align=ft.TextAlign.LEFT, color="#EEEEEE",
                             size=18, weight=ft.FontWeight.W_500)

    tower_config = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Tower", text_align=ft.TextAlign.LEFT, color="#EEEEEE",
                                  size=18, weight=ft.FontWeight.BOLD), numeric=True),
            ft.DataColumn(ft.Text("Pos X", text_align=ft.TextAlign.LEFT, color="#EEEEEE",
                                  size=18, weight=ft.FontWeight.BOLD), numeric=True),
            ft.DataColumn(ft.Text("Pos Y", text_align=ft.TextAlign.LEFT, color="#EEEEEE",
                                  size=18, weight=ft.FontWeight.BOLD), numeric=True),
        ],
    )
    for tower, pos in config.config_towers.items():
        tower_config.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(tower, color="#EEEEEE", size=17, weight=ft.FontWeight.W_500)),
                ft.DataCell(ft.TextField(value=pos[0], color="#EEEEEE", border_radius=0, border="none",
                                         keyboard_type=ft.KeyboardType.NUMBER,
                                         input_filter=ft.NumbersOnlyInputFilter())),
                ft.DataCell(ft.TextField(value=pos[1], color="#EEEEEE", border_radius=0, border="none",
                                         keyboard_type=ft.KeyboardType.NUMBER,
                                         input_filter=ft.NumbersOnlyInputFilter()))
            ]
        ))

    try:
        selected_task_1 = ft.TextField(value=config.current_tasks[0], label="Task 1", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())
    except Exception as e:
        selected_task_1 = ft.TextField(label="Task 1", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())
    try:
        selected_task_2 = ft.TextField(value=config.current_tasks[1], label="Task 2", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())
    except Exception as e:
        selected_task_2 = ft.TextField(label="Task 2", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())
    try:
        selected_task_3 = ft.TextField(value=config.current_tasks[2], label="Task 3", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())
    except Exception as e:
        selected_task_3 = ft.TextField(label="Task 3", color="#EEEEEE", border_radius=10,
                                       border_color="#31363F", border_width=2, cursor_color="#EEEEEE",
                                       keyboard_type=ft.KeyboardType.NUMBER, width=80, height=80,
                                       input_filter=ft.NumbersOnlyInputFilter())

    page.add(
        ft.Container(
            content=ft.Text('Configurator', text_align=ft.TextAlign.CENTER, color="#76ABAE", size=24,
                            weight=ft.FontWeight.BOLD),
            margin=ft.Margin(top=0, bottom=15, left=0, right=0),
        ),
        ft.Container(
            content=mkcmd_input,
            width=page.width - 100,
            padding=ft.Padding(top=0, bottom=0, left=5, right=5),
        ),
        ft.Container(
            content=mktitle_input,
            width=page.width - 100,
            padding=ft.Padding(top=0, bottom=0, left=5, right=5),
        ),
        ft.Container(
            content=accuracy_count,
            width=page.width - 100,
            margin=ft.Margin(top=10, bottom=0, left=5, right=0),
        ),
        ft.Container(
            content=accuracy_slider,
            width=page.width - 100,
            margin=ft.Margin(top=0, bottom=15, left=0, right=0),
        ),
        ft.Container(
            content=ft.Row(
                [selected_task_1, selected_task_2, selected_task_3],
                alignment=ft.MainAxisAlignment.CENTER,
                width=page.width - 100,
                spacing=25
            ),
            width=page.width - 100,
        ),
        ft.Container(
            content=tower_config,
            width=page.width - 100,
            margin=ft.Margin(top=0, bottom=15, left=0, right=0),
        ),
        ft.ElevatedButton(
            text="Save configuration",
            width=page.width - 100,
            bgcolor="#76ABAE",
            color="#EEEEEE",
            icon="save",
            on_click=save_config
        )
    )


if __name__ == "__main__":
    tray_icon.run_detached()
    ft.app(main)
