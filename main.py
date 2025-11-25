from ursina import *
from panda3d.core import AmbientLight, DirectionalLight, Vec3, PointLight
from player import Player
from door import Door
from world import create_world
from stamina import StaminaBar
from ursina.shaders import lit_with_shadows_shader


app = Ursina()
Entity.default_shader = lit_with_shadows_shader
# ============================
# =======   LIGHT   ==========
# ============================


# Ambient Light (ánh sáng chung)
ambient_light = AmbientLight('ambient')
ambient_light.setColor((0.20, 0.20, 0.20, 1))    # tối vừa, không cháy sáng
ambient_node = render.attachNewNode(ambient_light)
render.setLight(ambient_node)

# Directional Light (ánh sáng mặt trời / đèn chính)
dir_light = DirectionalLight('directional')
dir_light.setColor((1, 1, 1, 1))
dir_light.setShadowCaster(True, 2048, 2048)      # bật bóng

dir_node = render.attachNewNode(dir_light)
dir_node.setHpr(45, -60, 0)                      # hướng ánh sáng từ trên xuống
render.setLight(dir_node)

# Vùng che tối bổ sung để tăng độ sâu

sky = Sky()

# ============================
# =====    PLAYER     ========
# ============================

player = Player()

player.collider = 'box'
player.disable()

stamina = StaminaBar(player)

# ============================
# =====    WORLD      ========
# ============================

create_world()

# ============================
# =====     DOORS     ========
# ============================

door1 = Door(texture = 'wood',collider = 'box',open_rot = -90,  origin = (0.5, 0, 0),scale=(4.5, 4.1, 0.2),position=(34.5, 2, 20.5))
door2 = Door(collider = 'box',texture = 'iron',open_rot = 90,   origin = (-0.5, 0, 0),   scale=(2.5, 5, 0.2),position=(38, 1.2, 30),
        color=color.azure)
door2.rotation_y = 90
doors = [door1, door2]

# ============================
# ===== UI PROMPT  ===========
# ============================

text_prompt = Text("", origin=(0, 0), y=-0.4, enabled=False)

# ============================
# ========  MENU  ============
# ============================

mouse.locked = False
mouse.visible = True
menu_bg = Entity(parent=camera.ui, model='quad', scale=2, color=color.black66, z=1)
title = Text("DC TULEN", parent=camera.ui, y=.3, scale=3, color=color.azure)

def start_game():
    menu_bg.disable()
    title.disable()
    play_btn.disable()
    setting_btn.disable()
    player.enable()
    mouse.visible = False
    mouse.locked = True

play_btn = Button(text="Chơi", parent=camera.ui, y=.05, scale=(.3,.1),
                  color=color.lime, on_click=start_game)
setting_btn = Button(text="Setting", parent=camera.ui, y=-.15, scale=(.3,.1),
                     color=color.orange)

# ============================
# =========  PAUSE  ==========
# ============================

pause_panel = Entity(parent=camera.ui, model='quad', scale=1.2,
                     color=color.rgba(0,0,0,180), enabled=False, z=1)
pause_title = Text("Pause", parent=pause_panel, y=.3, scale=2, color=color.azure)

def resume_game():
    pause_panel.enabled = False
    resume_btn.enabled = False
    quit_btn.enabled = False
    mouse.visible = False
    mouse.locked = True
    player.enable()

def return_to_menu():
    pause_panel.enabled = False
    resume_btn.enabled = False
    quit_btn.enabled = False
    menu_bg.enable()
    title.enable()
    play_btn.enable()
    setting_btn.enable()
    player.disable()
    mouse.visible = True
    mouse.locked = False

resume_btn = Button(text="Tiếp tục", parent=pause_panel, y=.05, scale=(.4,.12),
                    color=color.lime, enabled=False, on_click=resume_game)
quit_btn = Button(text="Trở về menu", parent=pause_panel, y=-.2, scale=(.4,.12),
                  color=color.orange, enabled=False, on_click=return_to_menu)


# ============================
# ========= UPDATE ===========
# ============================

ui_distance = 6

def update():
    if not player.enabled:
        text_prompt.enabled = False
        return

    # Kiểm tra cửa gần
    near = None
    for d in (door1, door2):
        if distance(player.position, d.position) < ui_distance:
            near = d
            break

    if near:
        text_prompt.enabled = True
        text_prompt.text = "Nhấn E để mở/đóng cửa"
    else:
        text_prompt.enabled = False


# ============================
# =========  INPUT  ==========
# ============================

interaction_distance = 6

def input(key):
    if key == 'e':
        for d in (door1, door2):
            if distance(player.position, d.position) < interaction_distance:
                d.toggle()

    if key == 'escape' and player.enabled:
        pause_panel.enabled = True
        resume_btn.enabled = True
        quit_btn.enabled = True
        mouse.visible = True
        mouse.locked = False
        player.disable()


app.run()
