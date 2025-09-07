# ファイル名: `item.py`

# 目的:
# 強化アイテム（リポDのようなドリンク）の属性と動作を管理する `Item` クラスを実装する。このクラスは、アイテムの表示、プレイヤーによる取得、および取得後の消滅を処理する。

# 詳細な指示:

# 1. 必要なモジュールのインポート:
#     *   `import pygame`
#     *   `from config import *` # config.pyから必要な定数をインポート（例: `ITEM_IMAGE_PATH`, `TILE_SIZE` など）

# 2. `Item` クラスの定義:
#     *   `pygame.sprite.Sprite` を継承した `Item` クラスを定義する。
#     *   **`__init__(self, x: int, y: int, item_type: str = "invincibility"):`**
#         *   `super().__init__()` を呼び出す。
#         *   **画像:**
#             *   `self.image = pygame.image.load(ITEM_IMAGE_PATH).convert_alpha()` # 画像を読み込み、アルファチャンネルを保持
#             *   `self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))` # 画像をconfig.TILE_SIZEにスケーリング
#             *   # 例: プレイヤーや敵と同じサイズにすることで、ゲーム内の見た目を統一する。
#         *   **Rectオブジェクト:** `self.rect = self.image.get_rect(topleft=(x, y))` # 画像の位置とサイズを定義
#         *   **アイテムの種類:** `self.item_type: str = item_type` # アイテムの種類（例: "invincibility"）。これにより、取得時の効果を区別できる。
#         *   **取得済みフラグ:** `self.collected: bool = False` # プレイヤーに取得されたかどうかを示すフラグ

#     *   **描画メソッド (`draw` メソッド):
#         *   `def draw(self, screen: pygame.Surface):`
#             *   `if not self.collected:` # アイテムがまだ取得されていない場合のみ描画する
#                 *   `screen.blit(self.image, self.rect)`

#     *   **取得処理メソッド (`collect` メソッド):
#         *   `def collect(self):`
#             *   `self.collected = True` # アイテムが取得されたことをマーク
#             *   `self.kill()` # このSpriteを所属するすべてのSpriteグループから削除する。これにより、画面から消え、衝突判定の対象外となる。
#             *   # **アイテム取得時の効果音:**
#             *   # 例: `pygame.mixer.Sound("assets/sounds/item_collect.wav").play()` のように、効果音ファイルを読み込み再生する。
#             *   # **アイテム取得時の視覚的フィードバック:**
#             *   # 例: 短いアニメーション（アイテムが弾ける、光るなど）、パーティクルエフェクト、またはコンソールにメッセージを出力する（デバッグ用）。
#             *   # print(f"Item '{self.item_type}' collected!")

# 考慮事項:
# *   アイテムの画像ファイルは、`config.py` で定義されたパス（`ITEM_IMAGE_PATH`）に存在することを前提とする。SLMは、これらのパスが有効であることを前提にコードを生成する。
# *   アイテムの配置は、ステージのレイアウトと連携して行う。
# *   プレイヤーがアイテムを取得した際の具体的な効果（無敵時間の付与など）は、`main.py` での衝突判定と連携して `player.py` のメソッド（例: `player.activate_invincibility()`) を呼び出す形で実装する。`item_type` を利用して、異なるアイテムが異なる効果を持つようにできる。
# *   `main.py` からアイテムの `draw()` メソッドが呼び出されることを想定する。`pygame.sprite.Group` を使用してアイテムを管理する場合、グループの `draw()` メソッドが各Spriteの `draw()` メソッドを自動的に呼び出す。
