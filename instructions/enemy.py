# ファイル名: `enemy.py`

# 目的:
# 敵キャラクター（警備員T、警備員H、社長）の属性と動作を管理するクラスを実装する。これらのクラスは、ゲーム内の敵の挙動を定義し、プレイヤーとのインタラクションを可能にする。

# 詳細な指示:

# 1. 必要なモジュールのインポート:
#     *   `import pygame`
#     *   `from config import *` # config.pyから必要な定数をインポート（例: `ENEMY_SPEED_T`, `ENEMY_T_IMAGE_PATH`, `TILE_SIZE` など）

# 2. `Enemy` 基底クラスの定義:
#     *   `pygame.sprite.Sprite` を継承した `Enemy` クラスを定義する。
#     *   **`__init__(self, x: int, y: int, speed: float, image_path: str, walk_range_start: int, walk_range_end: int):`**
#         *   `super().__init__()` を呼び出す。
#         *   **画像:**
#             *   `self.image = pygame.image.load(image_path).convert_alpha()`
#             *   `self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))` # 画像をTILE_SIZEにスケーリング
#             *   `self.original_image = self.image` # 元の画像を保存（反転用）
#         *   **Rectオブジェクト:** `self.rect = self.image.get_rect(topleft=(x, y))`
#         *   **速度:** `self.speed = speed`
#         *   **移動方向:** `self.direction = 1` # 1:右, -1:左 (初期は右方向)
#         *   **移動範囲:**
#             *   `self.walk_range_start = walk_range_start` # 敵が左端に到達するX座標
#             *   `self.walk_range_end = walk_range_end` # 敵が右端に到達するX座標
#         *   **状態フラグ:** `self.is_defeated = False` # プレイヤーに倒されたかどうか

#     *   **`update(self):`**
#         *   `if self.is_defeated: return` # 倒されたら更新処理をスキップ
#         *   `self.rect.x += self.speed * self.direction`
#         *   **移動範囲のチェックと方向転換:**
#             *   `if self.direction == 1 and self.rect.right >= self.walk_range_end:`
#                 *   `self.direction = -1`
#                 *   `self.image = pygame.transform.flip(self.original_image, True, False)` # 画像を水平反転
#             *   `elif self.direction == -1 and self.rect.left <= self.walk_range_start:`
#                 *   `self.direction = 1`
#                 *   `self.image = pygame.transform.flip(self.original_image, False, False)` # 画像を元に戻す

#     *   **`draw(self, screen: pygame.Surface):`**
#         *   `screen.blit(self.image, self.rect)` # 敵を画面に描画

# 3. 特定の敵キャラクタークラスの定義:
#     *   `Enemy` クラスを継承して、以下の3つのクラスを定義する。
#         *   **`EnemyT(Enemy):`** (細長の警備員T)
#             *   `__init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):`
#                 *   `super().__init__(x, y, ENEMY_SPEED_T, ENEMY_T_IMAGE_PATH, walk_range_start, walk_range_end)`
#         *   **`EnemyH(Enemy):`** (ずんぐりむっくりの警備員H)
#             *   `__init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):`
#                 *   `super().__init__(x, y, ENEMY_SPEED_H, ENEMY_H_IMAGE_PATH, walk_range_start, walk_range_end)`
#         *   **`President(Enemy):`** (全身スーツの男、社長)
#             *   `__init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):`
#                 *   `super().__init__(x, y, BOSS_SPEED, BOSS_IMAGE_PATH, walk_range_start, walk_range_end)`
#                 *   # 社長固有の追加プロパティや挙動があればここに記述（例: 攻撃パターン、体力、特殊能力など）

# 4. プレイヤーによる踏みつけ処理 (`defeat` メソッド):
#     *   `Enemy` クラスに `defeat(self):` メソッドを追加する。
#     *   `self.is_defeated = True` に設定する。
#     *   `self.kill()` を呼び出して、このSpriteを所属するすべてのSpriteグループから削除する。
#     *   # 敵が倒された際の視覚的フィードバック（例: 爆発アニメーション、消滅エフェクト）や効果音の再生をここに記述する。

# 考慮事項:
# *   敵の画像ファイルは、`config.py` で定義されたパス（例: `assets/enemy_t.png`）に存在することを前提とする。SLMは、これらのパスが有効であることを前提にコードを生成する。
# *   `walk_range_start` と `walk_range_end` は、敵が往復するX座標の範囲を定義する。これらの値は、ステージの設計に応じて適切に設定される必要がある。
# *   `President` は最終ボスであるため、他の敵とは異なる特別な挙動（例: 攻撃、体力、倒し方）を持つ可能性があるが、現時点ではシンプルな左右往復移動で実装し、必要に応じて後で拡張する。
# *   敵の描画は `draw` メソッドで行い、`main.py` から呼び出されることを想定する。`pygame.sprite.Group` を使用して敵を管理する場合、グループの `draw()` メソッドが各Spriteの `draw()` メソッドを自動的に呼び出す。
