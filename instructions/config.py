# ファイル名: `config.py`

# 目的:
# このファイルは、ゲーム全体の動作を制御するすべての定数と設定を一元的に管理します。これにより、ゲームのバランス調整や機能変更が容易になります。SLMは、これらの定数をPythonの変数として正確に定義する必要があります。

# 詳細な指示:

# 1. 画面設定 (Screen Configuration):
#     *   ゲームウィンドウのサイズとタイトルを定義します。
#     *   `SCREEN_WIDTH: int = 800`  # ゲーム画面の幅（ピクセル単位）
#     *   `SCREEN_HEIGHT: int = 600` # ゲーム画面の高さ（ピクセル単位）
#     *   `CAPTION: str = "Security Run"` # ゲームウィンドウのタイトル文字列

# 2. プレイヤー設定 (Player Configuration):
#     *   プレイヤーキャラクターの移動、ジャンプ、残機、無敵時間に関する定数を定義します。
#     *   `PLAYER_SPEED: int = 5` # プレイヤーの水平移動速度（ピクセル/フレーム）
#     *   `PLAYER_JUMP_STRENGTH: int = -15` # プレイヤーのジャンプ力（上方向への初速度、負の値で上方向）
#     *   `PLAYER_INITIAL_LIVES: int = 3` # プレイヤーの初期残機数
#     *   `INVINCIBILITY_DURATION_FRAMES: int = 120` # 強化アイテム取得後の無敵時間（フレーム数、例: 2秒間 @ 60FPS）

# 3. 敵キャラクター設定 (Enemy Configuration):
#     *   様々な敵キャラクターの移動速度に関する定数を定義します。
#     *   `ENEMY_SPEED_DEFAULT: int = 2` # 敵のデフォルトの移動速度
#     *   `ENEMY_SPEED_T: int = 3` # 警備員Tの移動速度
#     *   `ENEMY_SPEED_H: int = 1` # 警備員Hの移動速度
#     *   `BOSS_SPEED: float = 2.5` # 社長の移動速度（浮動小数点数も可能）

# 4. ゲーム物理設定 (Game Physics Configuration):
#     *   ゲーム内の物理挙動（重力など）に関する定数を定義します。
#     *   `GRAVITY: float = 0.8` # 重力の加速度（ピクセル/フレーム^2）

# 5. ステージ設定 (Stage Configuration):
#     *   ステージの構成要素（タイルサイズ、穴の判定など）に関する定数を定義します。
#     *   `TILE_SIZE: int = 40` # ステージのタイルのサイズ（ピクセル単位）
#     *   # 注意: HOLE_FALL_Yは画面設定の後に定義する必要があります
#     *   # `HOLE_FALL_Y: int = 650` # プレイヤーが穴に落ちたと判定されるY座標の閾値（画面下部 + マージン）

# 6. 色定義 (Color Definitions - RGB Tuples):
#     *   Pygameで使用する標準的な色のRGB値をタプルとして定義します。
#     *   `WHITE: tuple[int, int, int] = (255, 255, 255)`
#     *   `BLACK: tuple[int, int, int] = (0, 0, 0)`
#     *   `BLUE: tuple[int, int, int] = (0, 0, 255)`
#     *   `RED: tuple[int, int, int] = (255, 0, 0)`
#     *   `GREEN: tuple[int, int, int] = (0, 255, 0)`
#     *   `BROWN: tuple[int, int, int] = (139, 69, 19)` # 地面の色など

# 7. ゲーム状態定義 (Game State Definitions):
#     *   ゲームの異なる状態を識別するための整数定数を定義します。これらは `main.py` でゲームの状態遷移を管理するために使用されます。
#     *   `GAME_STATE_TITLE: int = 0` # タイトル画面の状態
#     *   `GAME_STATE_PLAYING: int = 1` # ゲームプレイ中の状態
#     *   `GAME_STATE_GAME_OVER: int = 2` # ゲームオーバー画面の状態
#     *   `GAME_STATE_GAME_CLEAR: int = 3` # ゲームクリア画面の状態

# 8. アセットパス (Asset Paths - Placeholders):
#     *   ゲームで使用する画像やフォントファイルへの相対パスを定義します。これらのパスは、プロジェクトの `assets` フォルダを基準とします。
#     *   `PLAYER_IMAGE_PATH: str = "assets/player.png"` # プレイヤー画像のファイルパス
#     *   `ENEMY_T_IMAGE_PATH: str = "assets/enemy_t.png"` # 警備員T画像のファイルパス
#     *   `ENEMY_H_IMAGE_PATH: str = "assets/enemy_h.png"` # 警備員H画像のファイルパス
#     *   `BOSS_IMAGE_PATH: str = "assets/boss.png"` # 社長画像のファイルパス
#     *   `ITEM_IMAGE_PATH: str = "assets/item.png"` # アイテム画像のファイルパス
#     *   `FONT_PATH: str | None = None` # 使用するフォントのファイルパス（NoneでPygameのデフォルトフォント）

# 9. 追加のステージ設定 (Additional Stage Configuration):
#     *   画面設定に依存する定数をここで定義します。
#     *   `HOLE_FALL_Y: int = 650` # プレイヤーが穴に落ちたと判定されるY座標の閾値（SCREEN_HEIGHT + 50相当）

# 考慮事項:
# *   これらの定数は、他のPythonファイルから `from config import *` のようにインポートして使用することを想定します。
# *   画像やフォントのパスは、実際のファイル構造に合わせて調整する必要があります。SLMは、これらのパスが有効であることを前提にコードを生成します。
# *   `assets` フォルダをプロジェクトルート（`C:\Users\tomon\dev\projects\SecurityRun`）に作成し、指定された画像ファイルを配置することを強く推奨します。
