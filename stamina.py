# stamina.py
from ursina import *

class StaminaBar(Entity):
    def __init__(self, player, max_stamina=100):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.lime,
            scale=(0.3, 0.03),
            position=(-0.5, 0.45),
        )
        self.player = player
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina

    def update(self):
        # Kiểm tra player đang chạy
        is_running = (
            held_keys['shift'] and 
            (held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d'])
        )
        if is_running and self.current_stamina > 0:
            self.current_stamina -= 20 * time.dt  # giảm stamina
        else:
            self.current_stamina += 15 * time.dt  # hồi stamina

        self.current_stamina = clamp(self.current_stamina, 0, self.max_stamina)
        self.scale_x = 0.3 * (self.current_stamina / self.max_stamina)
