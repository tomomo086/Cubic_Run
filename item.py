# ファイル名: item.py
# 目的: 強化アイテム（リポDのようなドリンク）のクラス実装

import pygame
from config import *  # config.pyから必要な定数をインポート

class Item(pygame.sprite.Sprite):
    """強化アイテムクラス"""
    def __init__(self, x: int, y: int, item_type: str = "invincibility"):
        super().__init__()
        
        # 画像の読み込みと設定
        self.image = pygame.image.load(ITEM_IMAGE_PATH).convert_alpha()  # 画像を読み込み、アルファチャンネルを保持
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))  # 画像をTILE_SIZEにスケーリング
        
        # Rectオブジェクト
        self.rect = self.image.get_rect(topleft=(x, y))  # 画像の位置とサイズを定義
        
        # アイテムの種類
        self.item_type: str = item_type  # アイテムの種類（例: "invincibility"）
        
        # 取得済みフラグ
        self.collected: bool = False  # プレイヤーに取得されたかどうかを示すフラグ
    
    def draw(self, screen: pygame.Surface):
        """描画処理"""
        if not self.collected:  # アイテムがまだ取得されていない場合のみ描画する
            screen.blit(self.image, self.rect)
    
    def collect(self):
        """取得処理"""
        self.collected = True  # アイテムが取得されたことをマーク
        self.kill()  # このSpriteを所属するすべてのSpriteグループから削除する
        
        # アイテム取得時のフィードバック（デバッグ用）
        print(f"Item '{self.item_type}' collected!")