# นำเข้า pygame,sys,random
import pygame
import sys
import random

# กำหนด Pygame
pygame.init()

# กำหนดค่าี่
SCREEN_WIDTH = 720 #ความกว้างจอ
SCREEN_HEIGHT = 720 #ความสูงของจอ
GRID_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 15 #ความเร็วงู
# ปรับตามต้องการ

# สี
YELLOW = (255, 255, 0)  # สีเหลือง
BLUE = (0, 0, 255)  # สีฟ้า


# ทิศทาง
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# กำหนดหน้าจอ
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('เกมส์งู3310')

# กำหนดงู
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = RIGHT
snake_length = 1

# กำหนดอาหาร
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# ระบบคะแนน
score = 0
font = pygame.font.Font(None, 36)

#สถานะเกมส์เสร็จสิ้น
game_over = False

# วนลูปหลักของเกม
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # ย้ายงู
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # ตรวจสอบการชนกับอาหาร
    if snake[0] == food:
        snake_length += 2
        score += 2  # เพิ่มคะแนน
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    # ตรวจสอบการชนกับผนัง
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        game_over = True

    # ตรวจสอบการชนกับตัวเอง
    if snake[0] in snake[1:]:
        game_over = True

    # ตัดงูหากมีความยาวเกินไป
    if len(snake) > snake_length:
        snake.pop()

    # วาดพื้นหลัง
    screen.fill(BLUE)  

    # วาดอาหาร
    pygame.draw.rect(
        screen, YELLOW, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # วาดงู
    for segment in snake:
        pygame.draw.rect(
            screen, YELLOW, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # แสดงคะแนน
    text = font.render(f'Score: {score}', True, YELLOW)
    screen.blit(text, (10, 10))

    # อัปเดตหน้าจอ
    pygame.display.update()

    # ควบคุมความเร็วของเกม
    pygame.time.Clock().tick(SNAKE_SPEED)

# ปิด Pygame
pygame.quit()
sys.exit()
