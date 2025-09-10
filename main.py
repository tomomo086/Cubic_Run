# ファイル名: main.py  
# 目的: Pygameメインループとゲーム状態管理

# 1. 必要なモジュールのインポート
import pygame
from config import *  # config.pyからすべての定数をインポート
from screens import draw_title_screen, draw_game_over_screen, draw_game_clear_screen
from player import Player
from enemy import EnemyT, EnemyH, President
from stage import Stage
from item import Item

# 2. Pygameの初期化と画面設定
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# 3. ゲーム状態とオブジェクトの管理
current_game_state = GAME_STATE_TITLE
# グローバルゲームオブジェクトの宣言
player = None
enemies = None  # pygame.sprite.Group()
items = None    # pygame.sprite.Group()
stage = None

# 4. ゲームのリセット関数
def reset_game():
    global player, enemies, items, stage
    # ステージを作成
    stage = Stage()
    # プレイヤーを安全な初期位置に作成（左端、地面上）
    player = Player(50, 500)  # 敵から離れた安全な位置
    # 敵グループを作成
    enemies = pygame.sprite.Group()
    # 敵を中央〜右側に配置して衝突を回避
    enemy_t = EnemyT(400, 520, 350, 450)  # 中央付近
    enemy_h = EnemyH(600, 520, 550, 650)  # 右側
    enemies.add(enemy_t, enemy_h)
    # アイテムグループを作成
    items = pygame.sprite.Group()
    # アイテムを追加
    item = Item(350, 480)
    items.add(item)

# 5. メインゲームループ
def game_loop():
    global current_game_state
    running = True
    
    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if current_game_state == GAME_STATE_TITLE:
                    if event.key == pygame.K_RETURN:
                        current_game_state = GAME_STATE_PLAYING
                        reset_game()  # ゲーム開始時にリセット処理を呼び出す
                elif current_game_state == GAME_STATE_GAME_OVER or current_game_state == GAME_STATE_GAME_CLEAR:
                    if event.key == pygame.K_r:
                        current_game_state = GAME_STATE_PLAYING
                        reset_game()  # ゲームリスタート時にリセット処理を呼び出す
                    if event.key == pygame.K_q:
                        running = False
                # プレイヤーのジャンプ入力処理（1回のキー押下で実行）
                if current_game_state == GAME_STATE_PLAYING:
                    if event.key == pygame.K_SPACE:
                        player.jump()
        
        # 連続キー入力処理（ゲームプレイ中のみ）
        if current_game_state == GAME_STATE_PLAYING:
            keys = pygame.key.get_pressed()  # 現在押されているキーを取得
            if keys[pygame.K_LEFT]:
                player.go_left()
            elif keys[pygame.K_RIGHT]:
                player.go_right()
            else:
                player.stop()  # キーが押されていない場合は停止
        
        # ゲームロジックの更新と描画
        if current_game_state == GAME_STATE_TITLE:
            draw_title_screen(screen)
        elif current_game_state == GAME_STATE_PLAYING:
            screen.fill(BLACK)  # 背景を黒で塗りつぶす
            # オブジェクトの更新
            player.update(stage.get_platforms())  # プラットフォーム情報を渡して衝突判定
            enemies.update()
            items.update()
            # 衝突判定
            # プレイヤーと敵の衝突
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect) and not enemy.is_defeated:
                    # プレイヤーが敵の上から踏んだ場合
                    if player.rect.bottom <= enemy.rect.top + 10 and player.change_y > 0:
                        enemy.defeat()
                    # 横から接触した場合
                    else:
                        player.take_damage()
            # プレイヤーとアイテムの衝突
            for item in items:
                if player.rect.colliderect(item.rect) and not item.collected:
                    item.collect()
                    if item.item_type == "invincibility":
                        player.invincible = True
                        player.invincible_timer = INVINCIBILITY_DURATION_FRAMES
            # 描画処理
            stage.draw(screen)
            enemies.draw(screen)  # pygame.sprite.Groupの標準draw()メソッド使用
            items.draw(screen)    # pygame.sprite.Groupの標準draw()メソッド使用
            player.draw(screen)   # プレイヤーは最後に描画
            # UI表示（残機など）
            font = pygame.font.Font(None, 36)
            lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
            screen.blit(lives_text, (10, 10))
            # ゲーム状態のチェック
            if player.lives <= 0:
                current_game_state = GAME_STATE_GAME_OVER
            if stage.is_goal_reached(player.rect):
                current_game_state = GAME_STATE_GAME_CLEAR
            if stage.is_in_hole(player.rect):
                player.take_damage()
                player.rect.x, player.rect.y = 100, 400  # プレイヤーを初期位置に戻す
        elif current_game_state == GAME_STATE_GAME_OVER:
            draw_game_over_screen(screen)
        elif current_game_state == GAME_STATE_GAME_CLEAR:
            draw_game_clear_screen(screen)
        
        # 画面の更新
        pygame.display.flip()
        # フレームレート制御
        clock.tick(60)  # 60 FPSに設定

# 6. ゲーム終了処理
    pygame.quit()

# 7. エントリーポイント
if __name__ == "__main__":
    game_loop()