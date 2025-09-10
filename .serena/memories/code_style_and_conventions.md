# コードスタイルと規約

## 全般的なスタイル
- **言語**: 日本語コメント推奨
- **エンコーディング**: UTF-8
- **インデント**: 4スペース（Pythonデフォルト）

## 命名規則
- **クラス名**: PascalCase（例: `Player`, `EnemyT`, `EnemyH`）
- **関数名・メソッド名**: snake_case（例: `game_loop`, `take_damage`, `draw_title_screen`）
- **定数**: UPPER_SNAKE_CASE（例: `SCREEN_WIDTH`, `PLAYER_SPEED`）
- **変数名**: snake_case（例: `current_game_state`, `change_x`）

## 型ヒント
```python
# 基本的な型ヒント使用
def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, 
              color: tuple[int, int, int], x: int, y: int, 
              center: bool = False, antialias: bool = True):

# クラス属性の型ヒント
self.change_x: float = 0
self.change_y: float = 0
self.lives: int = PLAYER_INITIAL_LIVES
self.on_ground: bool = False
```

## docstring規約
現在の指示書では詳細なdocstringは使用されていないが、以下の形式を推奨：
```python
def take_damage(self):
    """プレイヤーがダメージを受ける処理
    
    無敵状態でない場合のみ残機を減らし、
    一定時間無敵状態にする。
    """
```

## インポート規則
```python
# 標準ライブラリ
import pygame

# 設定モジュール（全インポート）
from config import *

# 同一プロジェクト内のモジュール
from screens import draw_title_screen, draw_game_over_screen
from player import Player
from enemy import EnemyT, EnemyH, President
```

## クラス設計パターン
- **pygame.sprite.Sprite継承**: すべてのゲームオブジェクト
- **super().__init__()**: 親クラスの初期化必須
- **self.image, self.rect**: Pygameスプライトの基本属性
- **update(), draw()メソッド**: 標準的なゲームオブジェクトメソッド

## コメント規約
```python
# 日本語での詳細な説明を推奨
# 目的と処理内容を明記

# 将来的な実装のプレースホルダー
# player = Player(...)  # 後で実装
# enemies = pygame.sprite.Group()  # 敵グループ管理
```