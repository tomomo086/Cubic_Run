# ファイル名: `player.py`

# 目的:
# プレイヤーキャラクター（警備員）の属性（画像、位置、速度、残機）と動作（移動、ジャンプ、ダメージ処理）を管理する `Player` クラスを実装する。このクラスは、プレイヤーの入力に応じた挙動と、ゲーム内の物理法則（重力など）を適用する。

# 詳細な指示:

# 1. 必要なモジュールのインポート:
#     *   `import pygame`
#     *   `from config import *` # config.pyから必要な定数をインポート（例: `PLAYER_SPEED`, `PLAYER_JUMP_STRENGTH`, `GRAVITY`, `PLAYER_INITIAL_LIVES`, `INVINCIBILITY_DURATION_FRAMES`, `TILE_SIZE`, `PLAYER_IMAGE_PATH` など）

# 2. `Player` クラスの定義:
#     *   `pygame.sprite.Sprite` を継承した `Player` クラスを定義する。
#     *   **`__init__(self, x: int, y: int):`**
#         *   `super().__init__()` を呼び出す。
#         *   **画像:**
#             *   `self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()`
#             *   `self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))` # 画像をTILE_SIZEにスケーリング
#             *   `self.original_image = self.image` # 元の画像を保存（反転用）
#         *   **Rectオブジェクト:** `self.rect = self.image.get_rect(topleft=(x, y))`
#         *   **速度:**
#             *   `self.change_x: float = 0` # 横方向の速度
#             *   `self.change_y: float = 0` # 縦方向の速度
#         *   **残機:** `self.lives: int = PLAYER_INITIAL_LIVES`
#         *   **ジャンプ状態:** `self.on_ground: bool = False` # プレイヤーが地面にいるかどうか
#         *   **無敵状態:**
#             *   `self.invincible: bool = False`
#             *   `self.invincible_timer: int = 0`

#     *   **移動メソッド:**
#         *   **`go_left(self):`**
#             *   `self.change_x = -PLAYER_SPEED`
#             *   `self.image = pygame.transform.flip(self.original_image, True, False)` # 画像を水平反転
#         *   **`go_right(self):`**
#             *   `self.change_x = PLAYER_SPEED`
#             *   `self.image = pygame.transform.flip(self.original_image, False, False)` # 画像を元に戻す
#         *   **`stop(self):`**
#             *   `self.change_x = 0`
#         *   **`jump(self):`**
#             *   `if self.on_ground:` # 地面にいる場合のみジャンプ可能
#                 *   `self.change_y = PLAYER_JUMP_STRENGTH`
#                 *   `self.on_ground = False`

#     *   **更新メソッド (`update` メソッド):
#         *   **重力の適用:** `self.change_y += GRAVITY`
#         *   **X座標の更新:** `self.rect.x += self.change_x`
#         *   **Y座標の更新:** `self.rect.y += self.change_y`
#         *   **無敵タイマーの更新:**
#             *   `if self.invincible_timer > 0:`
#                 *   `self.invincible_timer -= 1`
#                 *   `if self.invincible_timer == 0:`
#                     *   `self.invincible = False`

#     *   **ダメージ処理メソッド (`take_damage` メソッド):
#         *   `def take_damage(self):`
#             *   `if not self.invincible:`
#                 *   `self.lives -= 1`
#                 *   `self.invincible = True`
#                 *   `self.invincible_timer = INVINCIBILITY_DURATION_FRAMES`
#                 *   # ダメージを受けた際の視覚的フィードバック（点滅など）や効果音の再生をここに記述する。

#     *   **描画メソッド (`draw` メソッド):
#         *   `def draw(self, screen: pygame.Surface):`
#             *   `screen.blit(self.image, self.rect)`

# 考慮事項:
# *   **地面との衝突判定:** `update` メソッド内で、ステージのプラットフォームとの衝突を処理する必要がある。衝突した場合、`self.rect.bottom` をプラットフォームのY座標に合わせ、`self.change_y` を0にし、`self.on_ground = True` に設定する。この処理は `stage.py` の情報と連携して `main.py` または `player.py` 内で行われる。
# *   プレイヤーの画像ファイルは、`config.py` で定義されたパス（`PLAYER_IMAGE_PATH`）に存在することを前提とする。
# *   `main.py` からプレイヤーの `update()` と `draw()` メソッドが呼び出されることを想定する。
# *   プレイヤーが画面外に出ないようにする処理（特に左右の境界）は、`update` メソッド内または `main.py` で実装する。