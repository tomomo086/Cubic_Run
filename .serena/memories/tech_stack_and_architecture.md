# 技術スタックとアーキテクチャ

## 使用技術
- **Python**: 3.x系（仮想環境使用）
- **Pygame**: メインゲームエンジン
- **開発環境**: Windows デスクトップ

## アーキテクチャパターン
### モジュール構成（予定）
- `main.py`: ゲームループとメインロジック
- `config.py`: 全設定定数の一元管理
- `player.py`: プレイヤークラス（pygame.sprite.Sprite継承）
- `enemy.py`: 敵キャラクタークラス群
- `item.py`: アイテムクラス
- `stage.py`: ステージ・地形管理
- `screens.py`: 画面描画関数群

### 設計パターン
- **State Pattern**: ゲーム状態管理（TITLE, PLAYING, GAME_OVER, GAME_CLEAR）
- **Sprite Groups**: Pygameのスプライトシステム活用
- **Configuration Management**: config.pyによる定数一元管理

### 主要な設定値
```python
# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "Security Run"

# プレイヤー設定
PLAYER_SPEED = 5
PLAYER_JUMP_STRENGTH = -15
PLAYER_INITIAL_LIVES = 3

# 物理設定
GRAVITY = 0.8
TILE_SIZE = 40

# ゲーム状態
GAME_STATE_TITLE = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
GAME_STATE_GAME_CLEAR = 3
```

## 仮想環境
- プロジェクトルートに `venv/` フォルダが存在
- Pygameの依存関係を分離管理