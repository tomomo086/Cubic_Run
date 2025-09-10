# ファイル名: enemy.py
# 目的: 敵キャラクター（警備員T、警備員H、社長）のクラス実装

import pygame
from config import *  # config.pyから必要な定数をインポート

class Enemy(pygame.sprite.Sprite):
    """敵の基底クラス"""
    def __init__(self, x: int, y: int, speed: float, image_path: str, walk_range_start: int, walk_range_end: int):
        super().__init__()
        
        # 警備員らしいグラフィックで描画
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((0, 0, 0, 0))  # 透明背景
        
        if 'enemy_t' in image_path.lower():
            # 細い警備員T（黒い制服）
            pygame.draw.rect(self.image, (50, 50, 50), (10, 5, 20, 35))  # 体
            pygame.draw.circle(self.image, (255, 220, 177), (20, 10), 6)  # 頭
            pygame.draw.rect(self.image, (255, 255, 255), (12, 15, 16, 8))  # シャツ
            pygame.draw.rect(self.image, (0, 0, 255), (14, 17, 12, 4))  # ネクタイ（青）
        elif 'enemy_h' in image_path.lower():
            # ずんぐり警備員H（グレー制服）
            pygame.draw.rect(self.image, (100, 100, 100), (8, 5, 24, 35))  # 体
            pygame.draw.circle(self.image, (255, 220, 177), (20, 10), 7)  # 頭
            pygame.draw.rect(self.image, (255, 255, 255), (10, 15, 20, 10))  # シャツ
            pygame.draw.rect(self.image, (255, 0, 0), (15, 18, 10, 4))  # ネクタイ（赤）
        elif 'boss' in image_path.lower():
            # 社長（高級スーツ）
            pygame.draw.rect(self.image, (20, 20, 60), (10, 5, 20, 35))  # ダークスーツ
            pygame.draw.circle(self.image, (255, 220, 177), (20, 10), 6)  # 頭
            pygame.draw.rect(self.image, (255, 255, 255), (12, 15, 16, 8))  # 高級シャツ
            pygame.draw.rect(self.image, (255, 215, 0), (14, 17, 12, 4))  # ゴールドタイ
        else:
            # デフォルト警備員
            pygame.draw.rect(self.image, (50, 50, 50), (10, 5, 20, 35))  # 体
            pygame.draw.circle(self.image, (255, 220, 177), (20, 10), 6)  # 頭
        
        self.original_image = self.image.copy()  # 元の画像を保存
        
        # Rectオブジェクト
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # 速度
        self.speed = speed
        
        # 移動方向（1:右, -1:左）
        self.direction = 1  # 初期は右方向
        
        # 移動範囲
        self.walk_range_start = walk_range_start  # 敵が左端に到達するX座標
        self.walk_range_end = walk_range_end      # 敵が右端に到達するX座標
        
        # 状態フラグ
        self.is_defeated = False  # プレイヤーに倒されたかどうか
    
    def update(self):
        """更新処理"""
        if self.is_defeated:
            return  # 倒されたら更新処理をスキップ
        
        # 移動
        self.rect.x += self.speed * self.direction
        
        # 移動範囲のチェックと方向転換
        if self.direction == 1 and self.rect.right >= self.walk_range_end:
            self.direction = -1
            # 方向転換時は画像はそのまま（色付き四角形のため反転不要）
            pass
        elif self.direction == -1 and self.rect.left <= self.walk_range_start:
            self.direction = 1
            # 方向転換時は画像はそのまま（色付き四角形のため反転不要）
            pass
    
    def defeat(self):
        """プレイヤーによる踏みつけ処理"""
        self.is_defeated = True
        self.kill()  # このSpriteを所属するすべてのSpriteグループから削除


class EnemyT(Enemy):
    """細長の警備員T"""
    def __init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):
        super().__init__(x, y, ENEMY_SPEED_T, ENEMY_T_IMAGE_PATH, walk_range_start, walk_range_end)


class EnemyH(Enemy):
    """ずんぐりむっくりの警備員H"""
    def __init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):
        super().__init__(x, y, ENEMY_SPEED_H, ENEMY_H_IMAGE_PATH, walk_range_start, walk_range_end)


class President(Enemy):
    """全身スーツの男（社長）"""
    def __init__(self, x: int, y: int, walk_range_start: int, walk_range_end: int):
        super().__init__(x, y, BOSS_SPEED, BOSS_IMAGE_PATH, walk_range_start, walk_range_end)
        # 社長固有の追加プロパティや挙動があればここに記述