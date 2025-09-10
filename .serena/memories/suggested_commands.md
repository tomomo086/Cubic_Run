# 推奨コマンド一覧

## Python仮想環境の操作
```cmd
# 仮想環境をアクティベート（Windows）
venv\Scripts\activate

# 仮想環境を無効化
deactivate
```

## Pygame関連のコマンド
```cmd
# Pygameのインストール
pip install pygame

# 依存関係の確認
pip list

# Pygameの動作確認
python -m pygame.examples.aliens
```

## ゲーム開発・実行コマンド
```cmd
# メインゲームの実行（実装後）
python main.py

# 設定確認（実装後）
python -c "from config import *; print(f'Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}')"
```

## Windows固有のコマンド
```cmd
# ディレクトリ一覧
dir
dir /s    # サブディレクトリも含む

# ファイル検索
where python
where pip

# プロセス確認
tasklist | findstr python

# 環境変数確認
echo %PATH%
```

## デバッグ・テストコマンド
```cmd
# Python構文チェック
python -m py_compile main.py

# Pythonの対話モード起動
python -i

# 詳細なエラー情報付きで実行
python -v main.py
```

## 開発ワークフロー
1. 仮想環境をアクティベート
2. 必要な依存関係をインストール
3. instructionsフォルダの指示書に従ってコード実装
4. pygame.init()でPygameを初期化
5. ゲームループを実行
6. デバッグとテスト