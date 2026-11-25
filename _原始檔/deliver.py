"""把 sec/*.png 與 gif/enc 整理成交付資料夾（語錄卡 v5）。"""
import os, shutil, base64, io
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
B = "/Users/ningchang/Library/Mobile Documents/com~apple~CloudDocs/○煦暖曆/04_內容企劃/_多產品/落地頁改版設計_1122/"
V = 'v6'; BASE = f'11.25_語錄卡_落地頁改版_{V}'; NAME = BASE + '_卡片統一只用1到45號'
O = B + NAME
SEC = [('s03', '03_誰適合語錄卡', 0), ('s03b', '03b_聖誕節前到貨_金光_GIF', 1), ('s04', '04_數字列', 0),
       ('s05', '05_45張語錄卡牆', 0), ('s05a', '05a_打開收藏盒抽一張_GIF', 1), ('s06', '06_一張卡拆解_8張輪播_GIF', 1),
       ('s06a', '06a_讀完立在盒上_GIF', 1), ('s07', '07_手機碰收藏盒NFC_GIF', 1), ('s08', '08_翻卡挑一句送人_GIF', 1),
       ('s09', '09_看見停下前行呼吸索引', 0), ('s10', '10_五色收藏盒', 0), ('s11', '11_規格', 0), ('s12', '12_轉折', 0)]
for sub in ['說明圖_1080寬', '動圖_MP4備用', '_原始檔']:
    os.makedirs(f'{O}/{sub}', exist_ok=True)
names = []
for sid, nm, g in SEC:
    if g:
        shutil.copy(f'{D}/gif/enc/{sid}.gif', f'{O}/說明圖_1080寬/{nm}.gif')
        shutil.copy(f'{D}/gif/enc/{sid}.mp4', f'{O}/動圖_MP4備用/{nm}.mp4')
        names.append((sid, nm + '.gif', g))
    else:
        Image.open(f'{D}/sec/{sid}.png').convert('RGB').save(f'{O}/說明圖_1080寬/{nm}.jpg', quality=90)
        names.append((sid, nm + '.jpg', g))
title = f'語錄卡落地頁 {V}'
head = f'<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>body{{margin:0;background:#888}}main{{max-width:432px;margin:0 auto;background:#fff}}img,video{{display:block;width:100%}}</style><main>'
dyn = head + '\n'.join(f'<img src="說明圖_1080寬/{n}">' for _, n, _ in names) + '</main>'
open(f'{O}/{BASE}_整頁預覽_動態.html', 'w').write(dyn)
open(f'{O}/index.html', 'w').write(dyn)
parts = []
for sid, n, g in names:
    if g:
        b = base64.b64encode(open(f'{D}/gif/enc/{sid}.mp4', 'rb').read()).decode()
        parts.append(f'<video autoplay muted loop playsinline src="data:video/mp4;base64,{b}"></video>')
    else:
        im = Image.open(f'{O}/說明圖_1080寬/{n}'); im = im.resize((864, round(im.height * 864 / im.width)), Image.LANCZOS)
        bio = io.BytesIO(); im.save(bio, 'JPEG', quality=86)
        parts.append(f'<img src="data:image/jpeg;base64,{base64.b64encode(bio.getvalue()).decode()}">')
open(f'{O}/{BASE}_整頁預覽_單檔整合.html', 'w').write(head + ''.join(parts) + '</main>')
ims = []
for sid, n, g in names:
    if g:
        fr = {'s03b': '010', 's05a': '030', 's06a': '040', 's08': '020'}.get(sid, '001')
        ims.append(Image.open(f'{D}/gif/secframes/{sid}/{fr}.png').convert('RGB'))
    else:
        ims.append(Image.open(f'{O}/說明圖_1080寬/{n}').convert('RGB'))
H = sum(i.height for i in ims); st = Image.new('RGB', (1080, H)); y = 0
for i in ims: st.paste(i, (0, y)); y += i.height
st = st.resize((540, H // 2), Image.LANCZOS)
st.save(f'{O}/{BASE}_整頁預覽_靜態第一格.jpg', quality=82)
for f in ['build_page.py', 'page.html', 'fonts_cream.otf', 'shot.py', 'deliver.py', 'prep_photo.py', 'prep_cards.py', 'quotes_50.json']:
    shutil.copy(f'{D}/{f}', f'{O}/_原始檔/{f}')
os.makedirs(f'{O}/_原始檔/gif', exist_ok=True)
for f in ['clips_q.py', 'nfc_notext.py', 'render_gif.py', 'enc.sh', 'caps_q_cards.json']:
    shutil.copy(f'{D}/gif/{f}', f'{O}/_原始檔/gif/{f}')
shutil.copytree(f'{D}/img', f'{O}/_原始檔/img', dirs_exist_ok=True)
print(O)
