from PIL import Image

# assetsフォルダを作成
import os
if not os.path.exists('assets'):
    os.makedirs('assets')

# 画像生成関数
def create_image(color, filename):
    # 新しい40x40ピクセルの画像を作成
    img = Image.new('RGB', (40, 40), color=color)
    # 画像を保存
    img.save(f'assets/{filename}')
    print(f'{filename} が作成されました')

# 各画像を作成
create_image((0, 0, 255), 'player.png')   # 青色の四角形 (プレイヤー)
create_image((255, 0, 0), 'enemy_t.png')  # 赤色の四角形 (細長警備員T)
create_image((255, 165, 0), 'enemy_h.png')# 橙色の四角形 (ずんぐり警備員H)
create_image((128, 0, 128), 'boss.png')    # 紫色の四角形 (社長)
create_image((255, 255, 0), 'item.png')   # 黄色の四角形 (アイテム)

print('全ての画像生成が完了しました')