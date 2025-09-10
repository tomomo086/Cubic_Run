# ファイル名: stage.py
# 目的: ゲームのステージ（地形、障害物、ゴール地点）の管理と描画

import pygame
from config import *  # config.pyから必要な定数をインポート

class Stage:
    def __init__(self):
        # ステージレイアウトの定義（文字列のリスト）
        self.level_layout: list[str] = [
            "                                        ",  # 0
            "                                        ",  # 1
            "                                        ",  # 2
            "                                        ",  # 3
            "                                        ",  # 4
            "                                        ",  # 5
            "                                        ",  # 6
            "           XX                           ",  # 7
            "                                        ",  # 8
            "                          XX            ",  # 9
            "                                        ",  # 10
            "      XX                                ",  # 11
            "                                        ",  # 12
            "                                   XX   ",  # 13
            "X       X          XX                 G ",  # 14
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # 15 (地面)
        ]
        # 各文字の意味:
        # 'X': 地面/ブロック (衝突判定あり)
        # ' ': 空中 (衝突判定なし)
        # 'G': ゴール地点 (衝突判定あり、プレイヤーが到達するとゲームクリア)
        
        # プラットフォームのRectオブジェクトリスト
        self.platforms: list[pygame.Rect] = []
        self.goal_rect: pygame.Rect | None = None
        
        # ステージレイアウトからプラットフォームを生成
        self._create_platforms_from_layout()
    
    def _create_platforms_from_layout(self):
        """ステージレイアウトからプラットフォームのRectオブジェクトを生成"""
        for row_index, row in enumerate(self.level_layout):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if tile == 'X':
                    # 地面/ブロック
                    platform_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    self.platforms.append(platform_rect)
                elif tile == 'G':
                    # ゴール地点
                    self.goal_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
    
    def draw(self, screen: pygame.Surface):
        """ステージの描画"""
        # 背景の描画
        screen.fill(BLACK)
        
        # ステージレイアウトから各タイルを描画
        for row_index, row in enumerate(self.level_layout):
            for col_index, tile in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if tile == 'X':
                    # 地面/ブロックを茶色で描画
                    pygame.draw.rect(screen, BROWN, (x, y, TILE_SIZE, TILE_SIZE))
                elif tile == 'G' and self.goal_rect:
                    # 会社の金庫らしいゴール
                    pygame.draw.rect(screen, (192, 192, 192), (x, y, TILE_SIZE, TILE_SIZE))  # シルバー金庫
                    pygame.draw.rect(screen, (105, 105, 105), (x, y, TILE_SIZE, TILE_SIZE), 4)  # 濃いグレー枠
                    # 金庫のダイヤル
                    pygame.draw.circle(screen, (255, 215, 0), (x+TILE_SIZE//2, y+TILE_SIZE//2), 8)  # ゴールドダイヤル
                    pygame.draw.circle(screen, (0, 0, 0), (x+TILE_SIZE//2, y+TILE_SIZE//2), 6, 2)  # 黒い目盛り
                    # 金庫のハンドル
                    pygame.draw.rect(screen, (255, 215, 0), (x+TILE_SIZE//2-2, y+TILE_SIZE//2+10, 4, 6))  # ハンドル
    
    def get_platforms(self) -> list[pygame.Rect]:
        """プラットフォームのリストを取得"""
        return self.platforms
    
    def is_goal_reached(self, player_rect: pygame.Rect) -> bool:
        """ゴール到達判定"""
        if self.goal_rect:
            return player_rect.colliderect(self.goal_rect)
        return False
    
    def is_in_hole(self, player_rect: pygame.Rect) -> bool:
        """穴落ち判定"""
        return player_rect.top > HOLE_FALL_Y