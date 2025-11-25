from ursina import *

class MainMenu(Entity):
    def __init__(self, start_callback, setting_callback):
        super().__init__()

        self.bg = Panel(scale=2, color=color.rgba(0,0,0,180))

        self.start_btn = Button(
            text="Chơi",
            scale=(0.3, 0.1),
            y=0.1,
            on_click=start_callback
        )

        self.setting_btn = Button(
            text="Settings",
            scale=(0.3, 0.1),
            y=-0.1,
            on_click=setting_callback
        )
