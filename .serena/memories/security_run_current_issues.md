# Cubic Run 現在の問題と解決策

## 🚨 現在の問題

### 1. 残機が勝手に減る問題
- **症状**: プレイヤーが動いているだけで残機が減少
- **推定原因**: 
  - プレイヤー初期位置(100, 400)と敵の初期位置が重複
  - main.pyのreset_game()で敵配置が不適切

### 2. ゴールが見えない問題
- **症状**: ゴール（緑色ブロック）の位置がわからない
- **推定原因**:
  - stage.pyのlevel_layout[0]行目の'G'位置が見えにくい
  - ゴールのレイアウト配置が画面外または判別困難

## 🔧 修正が必要なファイル

### stage.py修正内容
```python
# 現在のレイアウト（問題あり）
self.level_layout: list[str] = [
    "                    G                   ",  # 0行目 - 見えにくい
    # ...中略...
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 15行目 - 地面
]

# 修正案
self.level_layout: list[str] = [
    "                                        ",  # 0
    # ...中略...
    "                                      G ",  # 14行目 - 右端に明確配置
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 15行目 - 地面
]
```

### main.py修正内容
```python
# reset_game()関数内の修正案
def reset_game():
    # プレイヤーを安全な位置に
    player = Player(50, 500)  # 左端、地面上
    
    # 敵を離れた位置に配置
    enemy_t = EnemyT(400, 520, 350, 450)  # 中央付近
    enemy_h = EnemyH(600, 520, 550, 650)  # 右側
```

## 🎯 修正手順
1. stage.pyのゴール位置を右端に移動
2. main.pyのプレイヤー・敵初期位置を調整
3. 動作テストでバランス確認

## 📝 テスト観点
- プレイヤーが開始時に敵と衝突しないか
- ゴールが視覚的に明確に見えるか
- 正常なゲームフローで進行できるか