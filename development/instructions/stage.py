# ファイル名: `stage.py`

# 目的:
# ゲームのステージ（地形、障害物、ゴール地点）を定義し、描画する `Stage` クラスを実装する。このクラスは、ステージのレイアウトを管理し、プレイヤーや敵との衝突判定に必要な情報を提供する。

# 詳細な指示:

# 1. 必要なモジュールのインポート:
#     *   `import pygame`
#     *   `from config import *` # config.pyから必要な定数をインポート（例: `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `HOLE_FALL_Y`, `BROWN`, `GREEN`, `BLACK` など）

# 2. `Stage` クラスの定義:
#     *   `class Stage:`
#     *   **`__init__(self):`**
#         *   **ステージレイアウトの定義:**
#             *   ステージのレイアウトを文字列のリストとして定義する。各文字はタイルの種類を表す。
#             *   **例 (シンプルな1面構成):**
#                 ```python
#                 self.level_layout: list[str] = [
#                     "                                        ", # 0
#                     "                                        ", # 1
#                     "                                        ", # 2
#                     "                                        ", # 3
#                     "                                        ", # 4
#                     "                                        ", # 5
#                     "                                        ", # 6
#                     "                                        ", # 7
#                     "                                        ", # 8
#                     "                                        ", # 9
#                     "                                        ", # 10
#                     "                                        ", # 11
#                     "                                        ", # 12
#                     "X       X                               ", # 13
#                     "X       X                               ", # 14
#                     "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", # 15 (地面)
#                 ]
#                 # 各文字の意味:
#                 # 'X': 地面/ブロック (衝突判定あり)
#                 # ' ': 空中 (衝突判定なし)
#                 # 'G': ゴール地点 (衝突判定あり、プレイヤーが到達するとゲームクリア)
#                 # ステージの幅は SCREEN_WIDTH // TILE_SIZE に合わせる
#                 # ステージの高さは SCREEN_HEIGHT // TILE_SIZE に合わせる
#                 ```
#         *   **プラットフォームのRectオブジェクトリストの生成:**
#             *   `self.platforms: list[pygame.Rect] = []`
#             *   `self.goal_rect: pygame.Rect | None = None`
#             *   ステージレイアウトをループ処理し、各タイルに対応する `pygame.Rect` オブジェクトを作成する。
#             *   `for row_index, row in enumerate(self.level_layout):`
#                 *   `for col_index, tile in enumerate(row):`
#                     *   `x = col_index * TILE_SIZE`
#                     *   `y = row_index * TILE_SIZE`
#                     *   `if tile == 'X':`
#                         *   `platform_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)`
#                         *   `self.platforms.append(platform_rect)`
#                     *   `elif tile == 'G':`
#                         *   `self.goal_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)`
#                         *   # ゴールは1つなので、見つけたらループを抜ける（オプション）

#     *   **ステージの描画メソッド (`draw` メソッド):
#         *   `def draw(self, screen: pygame.Surface):`
#             *   **背景の描画:** `screen.fill(BLACK)` # まず背景を塗りつぶす
#             *   ステージレイアウトをループ処理し、各タイルに対応する色付きの四角形を描画する。
#             *   `for row_index, row in enumerate(self.level_layout):`
#                 *   `for col_index, tile in enumerate(row):`
#                     *   `x = col_index * TILE_SIZE`
#                     *   `y = row_index * TILE_SIZE`
#                     *   `if tile == 'X':`
#                         *   `pygame.draw.rect(screen, BROWN, (x, y, TILE_SIZE, TILE_SIZE))` # 地面/ブロックを茶色で描画
#                     *   `elif tile == 'G' and self.goal_rect:`
#                         *   `pygame.draw.rect(screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))` # ゴールを緑色で描画

#     *   **プラットフォーム取得メソッド (`get_platforms`):
#         *   `def get_platforms(self) -> list[pygame.Rect]:`
#             *   `return self.platforms`

#     *   **ゴール到達判定メソッド (`is_goal_reached`):
#         *   `def is_goal_reached(self, player_rect: pygame.Rect) -> bool:`
#             *   `if self.goal_rect:`
#                 *   `return player_rect.colliderect(self.goal_rect)` # プレイヤーのRectとゴールのRectが衝突しているか
#             *   `return False`

#     *   **穴落ち判定メソッド (`is_in_hole`):
#         *   `def is_in_hole(self, player_rect: pygame.Rect) -> bool:`
#             *   `return player_rect.top > HOLE_FALL_Y` # プレイヤーのY座標がHOLE_FALL_Yを超えたら穴落ちと判定

# 考慮事項:
# *   **ステージレイアウトの設計:** `self.level_layout` は、ゲームのステージを視覚的に表現する。各行は画面の高さ、各列は画面の幅に対応する。`SCREEN_WIDTH // TILE_SIZE` と `SCREEN_HEIGHT // TILE_SIZE` を考慮してレイアウトのサイズを決定する。
# *   **地形の描画:** 現時点では、`pygame.draw.rect` で色付きの四角形を描画する。将来的には、画像ファイルを使用してより詳細な地形を描画することも可能。
# *   **定数の利用:** `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `HOLE_FALL_Y`, `BROWN`, `GREEN`, `BLACK` など、`config.py` で定義された定数を積極的に使用する。
# *   **`main.py` との連携:** `main.py` からステージの `draw()` メソッドが呼び出されることを想定する。また、プレイヤーとプラットフォームの正確な衝突判定は、`player.py` の `update` メソッド内、または `main.py` のゲームロジック部分で、`self.platforms` を利用して実装される。
