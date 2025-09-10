#!/usr/bin/env python3
"""
シンプルなプレースホルダー画像ファイル生成スクリプト
Pygameが無くても動作する最小限の1x1 PNG生成
"""

import os

# 最小限のPNG画像データ（1x1ピクセル、透明）
# 実際のゲームでは色付きの四角形として描画される
def create_minimal_png():
    """最小限の透明PNG（1x1ピクセル）データを返す"""
    # PNG header + IHDR chunk + IDAT chunk + IEND chunk
    png_data = bytes([
        0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,  # PNG signature
        0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,  # IHDR chunk start
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,  # width=1, height=1
        0x08, 0x06, 0x00, 0x00, 0x00, 0x1F, 0x15, 0xC4,  # RGBA, compression, etc + CRC
        0x89, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,  # IDAT chunk start
        0x54, 0x78, 0x9C, 0x63, 0x00, 0x01, 0x00, 0x00,  # compressed data
        0x05, 0x00, 0x01, 0x0D, 0x0A, 0x2D, 0xB4, 0x00,  # CRC
        0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,  # IEND chunk
        0x42, 0x60, 0x82                                   # IEND CRC
    ])
    return png_data

def main():
    """プレースホルダー画像ファイルを生成"""
    
    # assetsフォルダ作成
    if not os.path.exists('assets'):
        os.makedirs('assets')
        print("assetsフォルダを作成しました")
    
    # 必要な画像ファイル一覧
    image_files = [
        'player.png',    # プレイヤー画像
        'enemy_t.png',   # 警備員T画像
        'enemy_h.png',   # 警備員H画像
        'boss.png',      # 社長画像
        'item.png'       # アイテム画像
    ]
    
    # 最小限のPNG画像データを取得
    png_data = create_minimal_png()
    
    # 各画像ファイルを生成
    for filename in image_files:
        filepath = os.path.join('assets', filename)
        with open(filepath, 'wb') as f:
            f.write(png_data)
        print(f"{filename} を作成しました")
    
    print("\nプレースホルダー画像の生成が完了しました！")
    print("注意: これらは1x1ピクセルの透明画像です。")
    print("ゲーム内ではconfig.pyのTILE_SIZEに自動スケーリングされます。")

if __name__ == "__main__":
    main()