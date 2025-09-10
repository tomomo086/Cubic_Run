import pygame
import os

# Pygameの初期化
pygame.init()

# 画像サイズ
size = (40, 40)

# 色の定義
colors = {
    "player": (0, 0, 255),
    "enemy_t": (255, 0, 0),
    "enemy_h": (255, 165, 0),
    "boss": (128, 0, 128),
    "item": (255, 255, 0)
}

# assetsフォルダの存在確認と作成
if not os.path.exists("assets"):
    os.makedirs("assets")

# 各画像の生成と保存
for name, color in colors.items():
    # スクリーンオブジェクトの作成
    screen = pygame.Surface(size)
    
    # 色付き四角形を描画
    screen.fill(color)
    
    # 画像ファイル名
    filename = f"{name}.png"
    
    # 画像保存
    pygame.image.save(screen, os.path.join("assets", filename))

# 完了メッセージの表示
print("プレースホルダー画像の生成が完了しました。")