"""語錄卡卡面：從專屬內容頁截圖（IG 封面工作檔 cards/card_NN.png，831×510，卡在 x3–830、y2–507，圓角約 40）裁成圓角透明 PNG。
另外做 06 一頁拆解的 8 張輪播（每張 1.2 秒＝15fps×18 格）與上方語錄字幕。"""
import os, json, shutil
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.abspath(__file__))
SRC = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/01_廣告投放/語錄卡/圖文/IG輪播_4比5/工作檔/封面單品情境/cards/"
Q = json.load(open(D + '/quotes_50.json'))   # 專屬內容頁 alt 文字：{"1": "第一行\n第二行…"}
def card(n, w=600):
    im = Image.open(f'{SRC}card_{n:02d}.png').convert('RGB').crop((3, 2, 830, 507))
    s = 4; m = Image.new('L', (im.width * s, im.height * s), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width * s - 1, im.height * s - 1), radius=40 * s, fill=255)
    m = m.resize(im.size, Image.LANCZOS); im = im.convert('RGBA'); im.putalpha(m)
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
os.makedirs(D + '/img/cards', exist_ok=True)
for n in range(1, 51): card(n).save(f'{D}/img/cards/{n:02d}.png')
# 06 輪播
DAYS = [6, 30, 16, 37, 39, 8, 23, 46]
od = D + '/gif/clips/q_cards'; shutil.rmtree(od, ignore_errors=True); os.makedirs(od)
caps = []; k = 0
for n in DAYS:
    im = card(n, 800)
    first = Q[str(n)].split('\n')[0].rstrip('，,')
    cap = f'<small class="en">NO.{n:02d}</small>{first}'
    for _ in range(18):
        k += 1; im.save(f'{od}/{k:03d}.png'); caps.append(cap)
json.dump(caps, open(D + '/gif/caps_q_cards.json', 'w'), ensure_ascii=False)
print(k, caps[::18])
