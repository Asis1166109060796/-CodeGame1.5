#นำเข้าโมดูล pygame และโมดูล sys
import pygame
import sys

#เริ่มต้น Pygame
pygame.init()

#กำหนดขนาดหน้าต่างและสีพื้นหลัง
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (173, 216, 230)

#กำหนดสีของผู้เล่นและพื้น
PLAYER_COLOR = (0, 128, 0)
GROUND_COLOR = (188, 143, 143)

#กำหนดขนาดของผู้เล่น และค่าคงที่อื่น ๆ
PLAYER_SIZE = 40
PLAYER_SPEED = 1
GRAVITY = 1
JUMP_STRENGTH = 20

#สร้างหน้าต่างเกม
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario-like Game")

#กำหนดตัวละครของผู้เล่นและตัวแปรเกี่ยวกับการกระโดด
player = pygame.Rect(50, 450, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 0
is_jumping = False

#กำหนดพื้นดิน
ground = pygame.Rect(0, 500, WIDTH, 100)

#กำหนดตัวแปร running ให้เป็น True เพื่อเริ่มลูปหลักของเกม
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #ตรวจสอบว่าปุ่มลูกศรซ้ายถูกกด ถ้าใช่ ให้เคลื่อนที่ผู้เล่นไปทางซ้าย
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    #ตรวจสอบว่าปุ่มลูกศรขวาถูกกด ถ้าใช่ ให้เคลื่อนที่ผู้เล่นไปทางขวา
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    #ตรวจสอบว่าผู้เล่นไม่ได้กระโดดอยู่
    if not is_jumping:
        #ตรวจสอบว่าปุ่มสเปซถูกกดและผู้เล่นชนกับพื้น
        if keys[pygame.K_SPACE] and player.colliderect(ground):
            # ้าทั้งสองเงื่อนไขเป็นจริง, กำหนด is_jumping เป็น True
            is_jumping = True
            #กำหนดความเร็วของผู้เล่นเพื่อกระโดดขึ้นด้วยค่า -JUMP_STRENGTH
            player_speed = -JUMP_STRENGTH
    #ถ้าผู้เล่นอยู่ในขั้นตอนกระโดด, เพิ่มความเร็วของผู้เล่นด้วย GRAVITY
    else:
        player_speed += GRAVITY

    #เปลี่ยนตำแหน่ง y ของผู้เล่นตามความเร็ว
    player.y += player_speed

    #ตรวจสอบการชนกับพื้น
    if player.colliderect(ground):
        #หากชน, กำหนด is_jumping เป็น False เพื่อบอกว่าผู้เล่นไม่กระโดด
        is_jumping = False
        #กำหนดตั้งค่าตำแหน่ง y ของผู้เล่นให้เท่ากับส่วนบนของพื้น
        player.y = ground.y - player.height

    #ย้ายผู้เล่นและพื้นไปยังหน้าจอโดยลบและวาดใหม่
    screen.fill(BACKGROUND_COLOR) #เติมพื้นหลังด้วยสีพื้นหลัง
    pygame.draw.rect(screen, PLAYER_COLOR, player) #วาดผู้เล่น
    pygame.draw.rect(screen, GROUND_COLOR, ground)#วาดพื้น
    pygame.display.update()#ปรับจอ

# สิ้นสุด Pygame และออกจากโปรแกรม
pygame.quit()
sys.exit()