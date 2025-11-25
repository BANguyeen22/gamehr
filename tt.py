from ursina import *
from ursina.shaders import basic_lighting_shader
from random import randint
from ursina.prefabs.editor_camera import EditorCamera
import math
from ursina.prefabs.first_person_controller import FirstPersonController




game=Ursina()



dog = Entity(
    model='Wolf_obj.obj',
    scale=4,
    position=(5,0,5),
    collider='box'  # collider giúp nhận click hoặc va chạm
)
uh = Entity(
    model='cottage.obj',
    scale=1,
    position=(1,0,1),
    collider='box'  # collider giúp nhận click hoặc va chạm
)


vision_angle = 60   
vision_distance = 90  
speed = 3

def update():
    direction = player.position - dog.position
    distance = direction.length()

    if distance < vision_distance:
        dog.look_at(player)
        dog.position += direction.normalized() * speed * time.dt





class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.walk_speed = 6  # Tốc độ đi bộ bình thường
        self.run_speed = 16  # Tốc độ chạy nhanh
        self.speed = self.walk_speed  # Tốc độ hiện tại (có thể l walk_speed hoặc run_speed)

    def update(self):
        # Kiểm tra nếu phím Shift đang được giữ
        if held_keys['shift']:
            self.speed = self.run_speed  # Chạy nhanh
        else:
            self.speed = self.walk_speed  # Đi bộ bình thường
        
        # Gọi phương thức update của FirstPersonController
        super().update()

player = Player()  

footstep = Audio('footst1.mp3', autoplay=False)
footstep.volume = 0.6   # chỉnh âm lượng

step_gap = 0.35          # thời gian giữa 2 bước
step_timer = 0


def update():
    global step_timer

    # kiểm tra người chơi có đang di chuyển không
    is_moving = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']

    if is_moving and player.grounded:     # grounded = đang đứng trên mặt đất
        step_timer -= time.dt

        if step_timer <= 0:
            # random pitch cho tự nhiên
            footstep.pitch = random.uniform(0.85, 1.15)

            footstep.play()
            step_timer = step_gap
    else:
        # reset khi đứng yên
        step_timer = 0

ground=Entity(model='plane' , texture='ac/stone.png',
           collider='box',texture_scale=(100, 100), scale=(100,1,100))
# toàn 



wall1 = Entity(
    model='cube',
    texture='brick',
    collider='box',
    scale=(100,10,5),
    position=(0,5,50),
    texture_scale=(5, 5),
    color=color.orange)











wall2 = duplicate(wall1,z=-50,
                  collider='box',
                  color=color.brown,shader=basic_lighting_shader)
wall3 = duplicate(wall1,rotation_y=90,
                 position=(50,5,0),
                 scale=(100,10,2),
                 collider='mesh',
                 color=color.brown,shader=basic_lighting_shader)
wall4 = duplicate(wall2,rotation_y=90,
                 position=(50,5,0),
                 scale=(100,10,2),
                 collider='mesh',
                 color=color.brown,shader=basic_lighting_shader)

#--------------------------------------------------------------------
#go lock chuot
def input(key):
    if key == 'escape':
        window.lock_mouse = not window.lock_mouse
        print('Lock mouse:', window.lock_mouse)


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



box1=Entity(model='cube',texture='ac/grass-block.png', texture_scale=(100, 100), 
            collider='mesh', position=(4,0.6,3),
            color=color.green,shader=basic_lighting_shader)
box1=Entity(model='cube',texture='ac/grass-block.png', texture_scale=(100, 100), 
            collider='mesh', position=(5,0.6,3),
            color=color.green,shader=basic_lighting_shader)



pivot=Entity()
DirectionalLight(parent=pivot,y=2,z=3,rotation=(45,-45,45),shadows=True)

window.fullscreen=False
window.title = 'toàn.exe'

window.lock_mouse = False



game.run()

