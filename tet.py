from ursina import *
from ursina.shaders import basic_lighting_shader
from random import randint
from ursina.prefabs.editor_camera import EditorCamera
import math
from ursina.prefabs.first_person_controller import FirstPersonController
import random

game=Ursina()

# ---------- DOG ENTITY ----------

tree = Entity(
    model='tree1.obj',
    scale=0.5,
    position=(5,0,5),
    collider='mesh'  # collider giúp nhận click hoặc va chạm
)

# ---------- PLAYER ----------
class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.walk_speed = 6
        self.run_speed = 16
        self.speed = self.walk_speed

    def update(self):
        if held_keys['shift']:
            self.speed = self.run_speed
        else:
            self.speed = self.walk_speed
        
        super().update()

player = Player()


# ---------- FOOTSTEP SOUND ----------
footstep = Audio('footst1.mp3', autoplay=False)
footstep.volume = 0.6
step_gap = 0.35
step_timer = 0


# ---------- SINGLE UPDATE FUNCTION ----------
def update():
    global step_timer

    # ---------------- FOOTSTEP ----------------
    is_moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']

    if is_moving and player.grounded:
        step_timer -= time.dt
        if step_timer <= 0:
            footstep.pitch = random.uniform(0.85, 1.15)
            footstep.play()
            step_timer = step_gap
    else:
        step_timer = 0

    # ---------------- DOG AI ----------------
   



# ---------- WORLD ----------
ground = Entity(model='plane', texture='ac/stone.png',
                collider='box', texture_scale=(100, 100), scale=(100,1,100))

wall1 = Entity(
    model='cube',
    texture='brick',
    collider='box',
    scale=(100,10,5),
    position=(0,5,50),
    texture_scale=(5, 5),
    color=color.orange
)

wall2 = duplicate(wall1, z=-50, color=color.brown, shader=basic_lighting_shader)
wall3 = duplicate(wall1, rotation_y=90, position=(50,5,0), scale=(100,10,2),
                  collider='mesh', color=color.brown, shader=basic_lighting_shader)
wall4 = duplicate(wall2, rotation_y=90, position=(50,5,0), scale=(100,10,2),
                  collider='mesh', color=color.brown, shader=basic_lighting_shader)

wallt1 = Entity(
    model='cube',
    texture='ac/tuonggachtrang.jpg',
    collider='mesh',
    scale=(60,10,1),
    position=(0,2,20),
    texture_scale=(10, 10),
    color=color.gray,shader=basic_lighting_shader
    )
wallt2 = Entity(
    model='cube',
    texture='ac/tuonggachtrang.jpg',
    collider='mesh',
    scale=(17,10,1),
    position=(43,2,20),
    texture_scale=(10, 10),
    color=color.gray,shader=basic_lighting_shader
    )
wallt3 = Entity(
    model='cube',
    texture='ac/tuonggachtrang.jpg',
    collider='mesh',
    scale=(4.6,3,1),
    position=(32.2,5.5,20),
    texture_scale=(30, 30),
    color=color.gray,shader=basic_lighting_shader
)
wallt4 = Entity(
    model='cube',
    texture='ac/wc.png',
    collider='mesh',
    scale=(3,2,0.5),
    position=(32.2,5.2,19),
    texture_scale=(30, 30),
    color=color.white,shader=basic_lighting_shader
)

# ---------- INPUT ----------
def input(key):
    if key == 'escape':
        window.lock_mouse = not window.lock_mouse
        print('Lock mouse:', window.lock_mouse)


# ---------- LIGHT ----------
pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, rotation=(45,-45,45), shadows=True)

window.fullscreen = False
window.title = 'toàn.exe'
window.lock_mouse = False
#########################
# MENU CHÍNH (UI)
#########################

# Ẩn player khi chưa chơi
player.disable()

# Unlock chuột để bấm nút menu
mouse.visible = True
mouse.locked = False

# Nền mờ
menu_bg = Entity(parent=camera.ui, model='quad', scale=2, color=color.black66, z=1)

# Tiêu đề
title = Text("DC TULEN", parent=camera.ui, y=.3, scale=3, color=color.azure)

# Hàm bắt đầu game
def start_game():
    menu_bg.disable()
    title.disable()
    play_btn.disable()
    setting_btn.disable()

    # bật player
    player.enable()

    # lock chuột lại cho FPS
    mouse.visible = False
    mouse.locked = True


# Nút chơi
play_btn = Button(
    text="Chơi",
    parent=camera.ui,
    y=.05,
    scale=(.3, .1),
    color=color.lime,
    on_click=start_game
)

# Nút setting (để trống)
setting_btn = Button(
    text="Setting",
    parent=camera.ui,
    y=-.15,
    scale=(.3, .1),
    color=color.orange,
)

# ============================
# CÁNH CỬA + UI TƯƠNG TÁC
# ============================

class Door(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'cube'
        self.scale = (1, 2, 0.1)
        self.color = color.brown
        self.origin = (0.5, 0, 0)   # giúp cửa xoay như bản lề
        self.position = (3, 0, 3)

        self.is_open = False
        self.rotation_y = 0
        self.closed_rot = 0
        self.open_rot = -90    # xoay sang phải

        for key, value in kwargs.items():
            setattr(self, key, value)

    def toggle(self):
        if not self.is_open:
            self.animate('rotation_y', self.open_rot, duration=.3, curve=curve.ease_out)
        else:
            self.animate('rotation_y', self.closed_rot, duration=.3, curve=curve.ease_in)
        self.is_open = not self.is_open


door = Door()

# UI hiển thị khi ở gần cửa
text_prompt = Text("", origin=(0, 0), y=-0.4, enabled=False)


def update():
    # kiểm tra khoảng cách người chơi với cửa
    dist = distance(player.position, door.position)

    if dist < 2:      # đứng gần cửa 2 mét
        text_prompt.text = "Nhấn E để mở/đóng cửa"
        text_prompt.enabled = True

        if held_keys['e']:
            door.toggle()

    else:
        text_prompt.enabled = False

game.run()
