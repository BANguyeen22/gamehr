from ursina import *

class Door(Entity):
    def __init__(self, **kwargs):
        defaults = dict(
            model='cube',
            color=color.brown,
            collider='box',
        )
        defaults.update(kwargs)

        super().__init__(**defaults)


        # pivot xoay nằm ở cạnh bản lề
        

        # --- TRIGGER ---
        

        # TRẠNG THÁI CỬA
        self.is_open = False
        self.closed_rot = 0
        #.open_rot = -90

        # ÂM THANH
        self.sound_open = Audio('opendoor.mp3', autoplay=False)
        self.sound_close = Audio('opendoor.mp3', autoplay=False)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def toggle(self):
        if not self.is_open:
            self.animate('rotation_y', self.open_rot, 0.15, curve=curve.out_expo)
            self.sound_open.play()
        else:
            self.animate('rotation_y', self.closed_rot, 0.15, curve=curve.in_expo)
            self.sound_close.play()
        self.is_open = not self.is_open
