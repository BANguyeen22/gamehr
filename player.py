from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
import random

class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.walk_speed = 6
        self.run_speed = 18
        self.speed = self.walk_speed
        self.gravity = 0.5
        self.position =(30,1.2,26.5)

        # Footstep
        self.footstep = Audio('footst1.mp3', autoplay=False)
        self.footstep.volume = 0.6
        self.step_gap = 0.35
        self.step_timer = 0

    def update(self):
        # Chạy bình thường
        if held_keys['shift']:
            self.speed = self.run_speed
        else:
            self.speed = self.walk_speed

        super().update()

        # FOOTSTEP
        is_moving = (
            held_keys['w']
            or held_keys['a']
            or held_keys['s']
            or held_keys['d']
        )

        if is_moving and self.grounded:
            self.step_timer -= time.dt
            if self.step_timer <= 0:
                self.footstep.pitch = random.uniform(0.85, 1.15)
                self.footstep.play()
                self.step_timer = self.step_gap
        else:
            self.step_timer = 0
