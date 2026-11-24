"""語錄卡落地頁 HOW TO USE 03：IG 封面 NFC 點盒換卡換盒色動畫，拿掉封面文案層（透明），15fps 輸出 930×1163。"""
import sys, os, pathlib
from PIL import Image
W = pathlib.Path("/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/語錄卡/圖文/IG輪播_4比5/工作檔/封面單品情境")
sys.path.insert(0, str(W)); os.chdir(W)
import make_cover_NFC_換盒色 as V   # 匯入時就把 SEQ、L、bg 換成換盒色版
M = V.M
OUT = pathlib.Path(__file__).resolve().parent / 'clips' / 'q_nfc'; OUT.mkdir(parents=True, exist_ok=True)
txt = Image.new('RGBA', (2160, 2700), (0, 0, 0, 0))
FPS = 15; n = round(M.L * FPS)
for f in range(n):
    M.frame(f / FPS, txt).resize((930, 1163), Image.LANCZOS).save(OUT / f'{f+1:03d}.jpg', quality=92)
    if f % 15 == 0: print('frame', f, '/', n, flush=True)
print('done', n)
