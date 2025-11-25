from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# -------- WORLD --------
ground = Entity(model='plane', scale=(100,1,100), texture='white_cube', collider='box')

# -------- PLAYER --------
player = FirstPersonController()
player.gravity = 0.5
player.cursor.visible = True

# -------- GRANNY ENEMY --------
class Granny(Entity):
    def __init__(self, **kwargs):
        super().__init__(model='granny.glb', scale=2, position=(10,0,10))
        self.speed = 2
        self.chase_distance = 15   # khoảng cách thấy player
        self.attack_distance = 2   # khoảng cách để "ăn" player
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        # Tính vector hướng tới player
        direction = player.position - self.position
        distance = direction.length()
        if distance < self.chase_distance:
            self.look_at(player.position)
            if distance > self.attack_distance:
                self.position += direction.normalized() * self.speed * time.dt
            else:
                print("Game Over! Granny bắt bạn rồi!")
                # Bạn có thể thêm restart hoặc reset player
