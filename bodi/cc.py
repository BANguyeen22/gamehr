from ursina import *
from random import randint
import math

# Khởi tạo ứng dụng Ursina
app = Ursina()

# Thiết lập camera FPS

window.lock_mouse = False  # Chuột bị khóa vào giữa cửa sổ khi bắt đầu

# Tạo một số đối tượng để nhìn thấy trong không gian 3D
player = Entity(model='cube', color=color.orange, scale=(1, 1, 1), position=(0, 0, 0))

# Kẻ địch (sử dụng cube đơn giản làm mô hình)
enemy = Entity(model='cube', color=color.red, scale=(1, 2, 1), position=(10, 0, 10))

# Tốc độ di chuyển của kẻ địch
enemy_speed = 3

# Hàm cập nhật mỗi frame
def update():
    # Điều khiển di chuyển camera (FPS)
    if window.lock_mouse:  # Nếu chuột bị khóa vào tâm
        camera.rotation_x -= mouse.dy * 0.1  # Di chuyển camera theo trục x (lên/xuống)
        camera.rotation_y += mouse.dx * 0.1  # Di chuyển camera theo trục y (trái/phải)
    
    # Di chuyển camera theo WASD
    speed = 5 * time.dt  # Tốc độ di chuyển
    if held_keys['w']:  # Di chuyển về phía trước
        camera.position += camera.forward * speed
    if held_keys['s']:  # Di chuyển lùi
        camera.position -= camera.forward * speed
    if held_keys['a']:  # Di chuyển sang trái
        camera.position -= camera.right * speed
    if held_keys['d']:  # Di chuyển sang phải
        camera.position += camera.right * speed
    
    # Kẻ địch di chuyển về phía người chơi
    direction_to_player = player.position - enemy.position  # Tính vector hướng tới người chơi
    direction_to_player = direction_to_player.normalized()  # Chuẩn hóa vector để tránh di chuyển nhanh hơn theo một hướng
    enemy.position += direction_to_player * enemy_speed * time.dt  # Di chuyển kẻ địch về phía người chơi
    
    # Kẻ địch thay đổi màu khi gần người chơi
    if distance(player.position, enemy.position) < 5:  # Nếu kẻ địch ở gần người chơi
        enemy.color = color.green  # Chuyển màu kẻ địch thành màu xanh (kẻ địch thấy người chơi)
    else:
        enemy.color = color.red  # Nếu không thì kẻ địch có màu đỏ (kẻ địch không thấy người chơi)

# Khởi chạy ứng dụng
app.run()
