# 開発ガイドライン

## プロジェクトの特徴

### 指示書ベース開発
- `instructions/`フォルダに詳細な実装指示書が格納されている
- 各ファイルは実装すべき内容の詳細な設計書として機能
- コメントで日本語による詳細な説明が記載されている

### 設計パターン
- **Configuration Pattern**: `config.py`で全設定を一元管理
- **State Machine**: ゲーム状態の明確な管理（TITLE→PLAYING→GAME_OVER/CLEAR）
- **Sprite System**: Pygameのスプライトグループを活用したオブジェクト管理

## 実装時の注意点

### 1. Pygame固有の考慮事項
```python
# 必ずpygame.init()を最初に実行
pygame.init()

# 画像読み込み時はconvert_alpha()を使用（パフォーマンス向上）
self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()

# フレームレート制御（60FPS推奨）
clock.tick(60)
```

### 2. 座標系の理解
- Pygameは左上が原点(0,0)
- Y座標は下向きが正の値
- ジャンプは負の値でY方向の速度を設定

### 3. 衝突判定
```python
# Rectオブジェクトを使用した衝突判定
if player.rect.colliderect(enemy.rect):
    player.take_damage()
```

### 4. 画像の扱い
```python
# 画像の反転（左右移動時）
self.image = pygame.transform.flip(self.original_image, True, False)

# 画像のスケーリング
self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
```

## 推奨開発順序
1. **config.py**: 全定数の定義
2. **screens.py**: 基本的な画面描画関数
3. **main.py**: ゲームループと状態管理
4. **player.py**: プレイヤークラスの実装
5. **stage.py**: 地形・ステージ管理
6. **enemy.py**: 敵キャラクター実装
7. **item.py**: アイテムシステム
8. **統合テスト**: 全体の動作確認

## デバッグ手法
```python
# デバッグ用の描画（開発時のみ）
pygame.draw.rect(screen, RED, player.rect, 2)  # 当たり判定の可視化

# コンソール出力でのデバッグ
print(f"Player pos: ({player.rect.x}, {player.rect.y})")
print(f"Lives: {player.lives}")
```