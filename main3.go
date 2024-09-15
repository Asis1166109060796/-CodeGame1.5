import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (173, 216, 230)


PLAYER_COLOR = (0, 0, 128)
GROUND_COLOR = (188, 143, 143)


PLAYER_SIZE = 40
PLAYER_SPEED = 1
GRAVITY = 1
JUMP_STRENGTH = 20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario-like Game")

# กำหนดตัวละครของผู้เล่นและตัวแปรเกี่ยวกับการกระโดด
player = pygame.Rect(50, 450, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 0
is_jumping = False

# กำหนดพื้นดิน
ground = pygame.Rect(0, 500, WIDTH, 100)

# กำหนดตัวแปร running ให้เป็น True เพื่อเริ่มลูปหลักของเกม
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    # เพิ่มฟังก์ชันกระโดด
    def jump():
        global player_speed, is_jumping, keys  # เพิ่มตัวแปร keys ที่ถูกเรียกใช้งานภายในฟังก์ชัน
        if not is_jumping:
            # ตรวจสอบว่าปุ่มสเปซถูกกดและผู้เล่นชนกับพื้น
            if keys[pygame.K_SPACE] and player.colliderect(ground):
                is_jumping = True
                player_speed = -JUMP_STRENGTH

    jump()
    if not is_jumping:
        player_speed += GRAVITY

    player.y += player_speed

    if player.colliderect(ground):
        is_jumping = False
        player.y = ground.y - player.height

    # สร้างฟังก์ชันเพิ่มของตกลง
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    pygame.draw.rect(screen, GROUND_COLOR, ground)
    pygame.display.update()


pygame.quit()
sys.exit()