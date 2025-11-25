from ursina import *
from ursina.shaders import basic_lighting_shader
from panda3d.core import AmbientLight,DirectionalLight,PointLight
from ursina.shaders import lit_with_shadows_shader

def create_world():
    # ======= WORLD OBJECTS =======
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
    
    tran = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='mesh',
        scale=(40,20,1),
        position=(49,6.5,25.5),
        texture_scale=(10, 10),
        color=color.gray, shader=lit_with_shadows_shader
        
    )
   
    tran.rotation_x = 90
    wallt1 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='mesh',
        scale=(60,10,1),
        position=(0,2,20),
        texture_scale=(10, 10),
        color=color.gray, shader=basic_lighting_shader
    )

    wallt2 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='mesh',
        scale=(17,10,1),
        position=(43,2,20),
        texture_scale=(10, 10),
        color=color.gray, shader=basic_lighting_shader
    )

    wallt3 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='mesh',
        scale=(4.6,3,1),
        position=(32.2,5.5,20),
        texture_scale=(30, 30),
        color=color.gray, shader=basic_lighting_shader
    )

    wallt4 = Entity(
        model='cube',
        texture='ac/wc.png',
        collider='mesh',
        scale=(3,2,0.2),
        position=(32.2,5.2,19),
        texture_scale=(30, 30),
        color=color.white, shader=basic_lighting_shader
    )
    wallt5 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='box',
        scale=(7,10,1),
        position=(38,1.2,24),
        texture_scale=(10, 10),
        color=color.white, shader=basic_lighting_shader
    )
    wallt5.rotation_y = 90
    wallt6 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='box',
        scale=(7,10,1),
        position=(38,1.2,33.5),
        texture_scale=(10, 10),
        color=color.white, shader=basic_lighting_shader
    )
    wallt6.rotation_y = 90
    wallt7 = Entity(
        model='cube',
        texture='ac/tuonggachtrang.jpg',
        collider='box',
        scale=(2.5, 3, 1),
        position=(38, 5, 28.75),
        texture_scale=(1,1 ),
        color=color.white, shader=basic_lighting_shader
    )
    wallt7.rotation_y = 90
    # Tree
    tree = Entity(
        model='tree1.obj',
        scale=0.5,
        position=(5,0,5),
        collider='mesh'
    )

    # Toilet
    toilet = Entity(
        model='toilet.obj',
        scale=0.06,
        texture='ac/Toilet.jpg',
        position=(48,1.2,22),
        collider='box',
        color=color.white, shader=basic_lighting_shader,
    )
    toilet.rotation_x = 270
    toilet1 = Entity(
        model='toilet.obj',
        scale=0.06,
        texture='ac/Toilet.jpg',
        position=(45,1.2,22),
        collider='box',
        color=color.white, shader=basic_lighting_shader,
    ) 
    toilet1.rotation_x = 270
    
    
    # ======= TOILET LIGHT (NOW INSIDE create_world) =======
    
    ceiling = Entity(model='cube', scale=(5,0.1,5), position=(0,3,0), color=color.gray)

    lamp_body = Entity(
        parent=ceiling,
        model='cylinder',
        scale=(0.4, 0.2, 0.4),
        position=(0, -0.15, 0),
        color=color.rgba(255, 255, 170, 200)
    )

    bulb = Entity(
        parent=lamp_body,
        model='sphere',
        scale=0.25,
        position=(0, -0.20, 0),
        color=color.rgba(255, 255, 170, 200),
        glow=0.4
    )

    
