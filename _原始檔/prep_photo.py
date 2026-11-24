"""語錄卡落地頁照片裁切（麻豆 0809 照片有 EXIF 旋轉，先轉正）。box＝(x0, y0, w) 比例，高度依輸出比例算。"""
import os
from PIL import Image, ImageEnhance, ImageOps
D = os.path.dirname(os.path.abspath(__file__))
M = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/語錄卡/毛片/麻豆_照片_0809/"
def f(n): return next(M + x for x in sorted(os.listdir(M)) if x.startswith('CYU0' + n))
C = {
 # name: (src, x0, y0, w, out_w, out_h, sat)
 'p1': (f('1384'), 0.0, 0.0, 1.0, 930, 1100, 1.04),
 'p2': (f('1980'), 0.0, 0.10, 1.0, 930, 1100, 1.04),
 'p3': (f('1405'), 0.0, 0.08, 1.0, 930, 1100, 1.04),
 'p4': (f('2008'), 0.0, 0.0, 1.0, 930, 1100, 1.04),
 's10': (f('1361'), 0.0, 0.0, 1.0, 930, 650, 1.04),
 's11': ("/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/語錄卡/圖文/IG輪播_4比5/工作檔/封面單品情境/底圖/C0193_7.5s.png", 0.0, 0.24, 1.0, 930, 750, 1.04),  # 麻豆影片 C0193 7.5 秒（IG 封面底圖）
 's12': (f('1976'), 0.0, 0.06, 1.0, 930, 1150, 1.04),
}
def run(sel=None):
    os.makedirs(D + '/img', exist_ok=True)
    for k, (src, x0, y0, w, ow, oh, sat) in C.items():
        if sel and k not in sel: continue
        im = ImageOps.exif_transpose(Image.open(src)).convert('RGB'); W, H = im.size
        cw = W * w; ch = cw * oh / ow
        if ch > H: ch = H; cw = ch * ow / oh
        bx, by = W * x0, H * y0
        if by + ch > H: by = H - ch
        if bx + cw > W: bx = W - cw
        c = im.crop((round(bx), round(by), round(bx + cw), round(by + ch))).resize((ow, oh), Image.LANCZOS)
        if sat != 1: c = ImageEnhance.Color(c).enhance(sat)
        c.save(f'{D}/img/{k}.jpg', quality=90)
        print(k, im.size, (round(bx), round(by), round(cw), round(ch)))
if __name__ == '__main__':
    import sys; run(sys.argv[1:])
