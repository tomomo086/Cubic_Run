# ファイル名: screens.py
# 目的: タイトル画面、ゲームオーバー画面、ゲームクリア画面の描画と基本的なテキスト表示

import pygame
from config import *  # config.pyから必要な定数をインポート

# フォント設定（グローバル変数として宣言、遅延初期化）
title_font = None
message_font = None

def initialize_fonts():
    """フォントの遅延初期化"""
    global title_font, message_font
    if title_font is None:  # まだ初期化されていない場合のみ実行
        title_font_size: int = 74
        title_font = pygame.font.Font(FONT_PATH, title_font_size)
        message_font_size: int = 36
        message_font = pygame.font.Font(FONT_PATH, message_font_size)

def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, color: tuple[int, int, int], x: int, y: int, center: bool = False, antialias: bool = True):
    """テキスト描画のヘルパー関数"""
    text_surface = font.render(text, antialias, color)  # テキストをレンダリング。antialiasでアンチエイリアシングを有効/無効化
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)  # 指定された(x, y)座標をテキストの中心に設定
    else:
        text_rect.topleft = (x, y)  # 指定された(x, y)座標をテキストの左上に設定
    screen.blit(text_surface, text_rect)  # 画面に描画

def draw_title_screen(screen: pygame.Surface):
    """タイトル画面の描画関数"""
    initialize_fonts()  # フォントが初期化されていることを確認
    screen.fill(BLACK)  # 画面全体を黒で塗りつぶす
    
    # ゲームタイトル
    title_text_y = SCREEN_HEIGHT // 2 - 50  # 画面中央より少し上に配置
    draw_text(screen, "CUBIC RUN", title_font, WHITE, SCREEN_WIDTH // 2, title_text_y, center=True)
    
    # 開始メッセージ
    message_text_y = SCREEN_HEIGHT // 2 + 50  # 画面中央より少し下に配置
    draw_text(screen, "Press ENTER to Start", message_font, WHITE, SCREEN_WIDTH // 2, message_text_y, center=True)

def draw_game_over_screen(screen: pygame.Surface):
    """ゲームオーバー画面の描画関数"""
    initialize_fonts()  # フォントが初期化されていることを確認
    screen.fill(BLACK)  # 画面全体を黒で塗りつぶす
    
    # 「GAME OVER」メッセージ
    game_over_text_y = SCREEN_HEIGHT // 2 - 50
    draw_text(screen, "GAME OVER", title_font, RED, SCREEN_WIDTH // 2, game_over_text_y, center=True)
    
    # 再試行/終了メッセージ
    restart_quit_text_y = SCREEN_HEIGHT // 2 + 50
    draw_text(screen, "Press R to Restart or Q to Quit", message_font, WHITE, SCREEN_WIDTH // 2, restart_quit_text_y, center=True)

def draw_game_clear_screen(screen: pygame.Surface):
    """ゲームクリア画面の描画関数"""
    initialize_fonts()  # フォントが初期化されていることを確認
    screen.fill(BLACK)  # 画面全体を黒で塗りつぶす
    
    # 「GAME CLEAR!」メッセージ
    game_clear_text_y = SCREEN_HEIGHT // 2 - 50
    draw_text(screen, "GAME CLEAR!", title_font, GREEN, SCREEN_WIDTH // 2, game_clear_text_y, center=True)
    
    # 再試行/終了メッセージ
    restart_quit_text_y = SCREEN_HEIGHT // 2 + 50
    draw_text(screen, "Press R to Restart or Q to Quit", message_font, WHITE, SCREEN_WIDTH // 2, restart_quit_text_y, center=True)