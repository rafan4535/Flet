import flet as ft


def main(page: ft.Page):
    page.title = "test2"
    page.window_height = 600
    page.window_width = 350
    page.window_always_on_top = True
    page.window_title_bar_hidden = False

    page.add(
        ft.Text("test")
    )


ft.app(target=main)
