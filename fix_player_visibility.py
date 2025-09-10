#!/usr/bin/env python3
"""
プレイヤーの描画を確実に見えるようにする修正
透明画像の代わりに色付き四角形で描画
"""

# player.pyの画像読み込み部分を一時的に無効化して色描画に変更
import os

# player.pyのバックアップを作成
if not os.path.exists('player.py.backup'):
    os.rename('player.py', 'player.py.backup')

# 修正版player.pyを作成（画像の代わりに色付き四角形を描画）
player_code = '''# ファイル名: player.py (修正版 - 色付き四角形で描画)
# 目的: プレイヤーキャラクター（警備員）のクラス実装

import pygame
from config import *  # config.pyから必要な定数をインポート

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        
        # 画像の代わりに色付きSurfaceを作成（確実に見える）
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)  # 青色で塗りつぶし
        self.original_image = self.image  # 元の画像を保存（反転用）
        
        # Rectオブジェクト
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # 速度
        self.change_x: float = 0  # 横方向の速度
        self.change_y: float = 0  # 縦方向の速度
        
        # 残機
        self.lives: int = PLAYER_INITIAL_LIVES
        
        # ジャンプ状態
        self.on_ground: bool = False  # プレイヤーが地面にいるかどうか
        
        # 無敵状態
        self.invincible: bool = False
        self.invincible_timer: int = 0
    
    def go_left(self):
        """左移動"""
        self.change_x = -PLAYER_SPEED
        # 反転は色だけなので省略
    
    def go_right(self):
        """右移動"""
        self.change_x = PLAYER_SPEED
        # 反転は色だけなので省略
    
    def stop(self):
        """移動停止"""
        self.change_x = 0
    
    def jump(self):
        """ジャンプ"""
        if self.on_ground:  # 地面にいる場合のみジャンプ可能
            self.change_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False
    
    def update(self, platforms: list[pygame.Rect]):
        """更新処理"""
        # 重力の適用
        self.change_y += GRAVITY
        
        # X座標の更新と境界チェック
        self.rect.x += self.change_x
        if self.rect.left < 0:
            self.rect.left = 0  # 左境界チェック
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH  # 右境界チェック
        
        # Y座標の更新
        self.rect.y += self.change_y
        
        # プラットフォームとの衝突判定
        self.on_ground = False  # 最初に地面にいない状態にリセット
        for platform in platforms:
            if self.rect.colliderect(platform):
                # 上から落ちてきた場合（地面に着地）
                if self.change_y > 0:  # 下向きに移動中
                    self.rect.bottom = platform.top
                    self.change_y = 0
                    self.on_ground = True
        
        # 無敵タイマーの更新
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            if self.invincible_timer == 0:
                self.invincible = False
    
    def take_damage(self):
        """ダメージ処理"""
        if not self.invincible:
            self.lives -= 1
            self.invincible = True
            self.invincible_timer = INVINCIBILITY_DURATION_FRAMES
    
    def draw(self, screen: pygame.Surface):
        """描画処理"""
        screen.blit(self.image, self.rect)
'''

with open('player.py', 'w', encoding='utf-8') as f:
    f.write(player_code)

print("✅ player.pyを修正しました（色付き四角形で描画）")
print("✅ 元のファイルはplayer.py.backupに保存されています")
print("🎮 再度ゲームを実行してください: python main.py")