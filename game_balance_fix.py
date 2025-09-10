# game_balance_fix.py

import pygame

# 初期化
pygame.init()

# 画面設定
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 色定義
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# プレイヤー設定
player_size = 50
player_pos = [400, 500]

# 敵設定
enemy_size = 50
enemy_list = [[100, 100], [600, 200], [300, 400]]

# ゴール設定
goal_pos = [750, 500]

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 背景
    screen.fill(WHITE)

    # プレイヤー
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    # 敵
    for enemy in enemy_list:
        pygame.draw.rect(screen, GREEN, (enemy[0], enemy[1], enemy_size, enemy_size))

    # ゴール
    pygame.draw.rect(screen, GREEN, (goal_pos[0], goal_pos[1], 50, 50))

    # 更新
    pygame.display.flip()
    clock.tick(30)

pygame.quit()