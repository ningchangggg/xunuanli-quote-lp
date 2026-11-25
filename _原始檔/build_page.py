"""語錄卡落地頁 v5（2026-11-25）：區塊結構照幹話曆／鮮花 v5（受眾卡＋對話框＋內頁卡＋貼紙＋旁白條 → 聖誕到貨 → 數字列 → 卡片牆 →
HOW TO USE ×4 穿插一張卡拆解 → 專屬視覺 → 款式 → 規格 → 轉折），視覺換成語錄卡自己的語言：
米白卡紙底、圓角語錄卡、摩卡絨布色帶（收藏盒內的黑絨布）、NFC 光圈章（取代花邊章／爆炸框）、小卡式名牌。
色票沿用語錄卡 IG 輪播：墨 #3A2621、摩卡 #5C3F39、玫瑰灰 #A07A70、酒紅 #7A2136、米白 #F7F4ED。
字：中文全部凝書體（不加粗、不描邊），英文小標 Helvetica 寬字距。產出 page.html，432 寬。"""
import os, json, random
D = os.path.dirname(os.path.abspath(__file__))
V = 'v5'
Q = json.load(open(f'{D}/quotes_50.json'))

# 五色收藏盒（官網款式名；色碼取自 CYU01361 實拍）
BOX = [('晴日雲藍', '#9DB4C8'), ('晚風藤紫', '#B3A1C6'), ('暖霧茶棕', '#B8A891'), ('靜夜墨黑', '#2F2B2A'), ('暮色莓紅', '#7E2F42')]

P = [
    dict(n='01', who='需要一句話的人', h='滑了一整晚手機，<br>心還是靜不下來', img='p1', card=13,
         s='隨手<mark>抽一張</mark>，讓一句話<mark>剛好回答</mark>今天的你。'),
    dict(n='02', who='想留點空白給自己', h='睡前十分鐘，<br>只想留給自己', img='p2', card=41,
         s='一句中英語錄配一幅攝影，<mark>慢慢讀完</mark>再睡。'),
    dict(n='03', who='交換禮物', h='不知道送什麼，<br>又不想送得太普通', img='p3', card=39,
         s='五色收藏盒挑一個，打開就是 <mark>45 句溫柔</mark>。'),
    dict(n='04', who='聖誕禮物', h='卡片不知道寫什麼？<br>讓它替你說', img='p4', card=30,
         s='在他需要一句話的時候，<mark>替你陪在身邊</mark>。'),
]
# 版面：泡泡、內頁卡、貼紙位置（避開臉和手上的卡）
L = [
    dict(say='left:12px;top:16px', tail='right:40px', card='left:10px;bottom:16px;transform:rotate(-5deg)',
         stk=('moon', '#A07A70', 'right:18px;bottom:24px;transform:rotate(8deg)'), rot=-.8),
    dict(say='right:12px;top:16px', tail='left:40px', card='right:10px;bottom:16px;transform:rotate(5deg)',
         stk=('star', '#5C3F39', 'left:20px;bottom:30px;transform:rotate(-8deg)'), rot=.8),
    dict(say='left:12px;bottom:16px', tail='right:44px', card='right:10px;top:18px;transform:rotate(5deg)',
         stk=('gift', '#7A2136', 'left:22px;top:22px;transform:rotate(-10deg)'), rot=-.8),
    dict(say='left:10px;bottom:16px;font-size:17px', tail='left:44px', card='right:8px;top:18px;transform:rotate(-4deg)',
         stk=('heart', '#B5423A', 'left:22px;top:22px;transform:rotate(8deg)'), rot=.8),
]

ICON = {
    'moon': '<path d="M26 7a14 14 0 1 0 7 25A12 12 0 0 1 26 7z"/><circle cx="31" cy="12" r="1.6"/><circle cx="34" cy="20" r="1.1"/>',
    'star': '<path d="M20 5l4.3 9.2 10 1.1-7.5 6.8 2.1 9.9L20 27l-8.9 5 2.1-9.9-7.5-6.8 10-1.1z"/>',
    'gift': '<rect x="7" y="16" width="26" height="18" rx="2"/><rect x="5" y="11" width="30" height="7" rx="2"/>'
            '<rect x="18" y="11" width="4" height="23" fill="#7A2136"/><path d="M20 11 C15 3 9 6 12 10 C14 12 18 11 20 11Z M20 11 C25 3 31 6 28 10 C26 12 22 11 20 11Z"/>',
    'heart': '<path d="M20 33 C9 25 5 19 5 13.5 C5 9 8.5 6 12.5 6 C16 6 18.5 8 20 11 C21.5 8 24 6 27.5 6 C31.5 6 35 9 35 13.5 C35 19 31 25 20 33Z"/>',
}

def sticker(kind, color, pos):
    return f'<div class="stk" style="background:{color};{pos}"><svg viewBox="0 0 40 40" width="30" height="30" fill="#fff">{ICON[kind]}</svg></div>'

def ring(txt, size=124, fill='#FBF3EC', rot=-6, fs=19):
    """NFC 光圈章：實心圓＋三圈由內往外變淡的光圈（像手機碰盒子的感應光圈）。"""
    return (f'<div class="ring" style="width:{size}px;height:{size}px"><svg viewBox="0 0 100 100" width="{size}" height="{size}">'
            f'<circle cx="50" cy="50" r="49" fill="none" stroke="#A07A70" stroke-width=".7" opacity=".35"/>'
            f'<circle cx="50" cy="50" r="45" fill="none" stroke="#A07A70" stroke-width=".9" opacity=".6"/>'
            f'<circle cx="50" cy="50" r="40.5" fill="{fill}" stroke="#3A2621" stroke-width="1.1"/>'
            f'<circle cx="50" cy="50" r="35.5" fill="none" stroke="#7A2136" stroke-width=".55" stroke-dasharray="1.4 2.2"/></svg>'
            f'<div class="rt" style="transform:rotate({rot}deg);font-size:{fs}px"><div>{txt}</div></div></div>')

CSS = '''
@font-face{font-family:Cream;src:url("fonts_cream.otf")}
:root{--paper:#F7F4ED;--ink:#3A2621;--text:#5E4A44;--mocha:#5C3F39;--rose:#A07A70;--wine:#7A2136;--blush:#EBCFC3;--line:#E3D8CC;--gold:#F1D48C;--card:#FFFDF9}
*{box-sizing:border-box;margin:0;padding:0}
body{width:432px;font-family:Cream,serif;color:var(--ink);-webkit-font-smoothing:antialiased;background:var(--paper)}
b,strong,h2,h3{font-weight:normal}
section{position:relative;overflow:hidden;background-color:var(--paper);background-image:radial-gradient(rgba(160,122,112,.07) .8px,transparent .9px);background-size:7px 7px;padding:36px 22px 40px}
.en{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-weight:500;letter-spacing:.2em}
mark{color:inherit;background:linear-gradient(transparent 60%,rgba(201,140,128,.34) 60%);padding:0 1px}
.eb{font-size:15px;color:var(--wine);letter-spacing:.14em;text-align:center}
h2{font-size:28px;line-height:1.42;text-align:center;margin-top:8px;letter-spacing:.05em}
h2 .u{background:linear-gradient(transparent 62%,rgba(201,140,128,.34) 62%)}
.lead{font-size:14.5px;line-height:1.8;text-align:center;margin-top:12px;color:var(--text);letter-spacing:.04em}
.ring{position:relative;margin:0 auto}.ring svg{position:absolute;inset:0}
.rt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;line-height:1.28;text-align:center;color:var(--ink);letter-spacing:.04em}
/* 圓角卡片 panel */
.pn{position:relative;background:var(--card);border-radius:18px;padding:8px;box-shadow:0 8px 22px rgba(58,38,33,.13),0 0 0 1px rgba(160,122,112,.14)}
.pic{position:relative;background-size:cover;background-position:center;overflow:hidden;border-radius:12px}
.tag{position:absolute;left:-10px;top:-18px;z-index:6;background:var(--mocha);color:#FBF6EF;border-radius:10px;padding:5px 16px 7px 16px;font-size:22px;transform:rotate(-3deg);box-shadow:0 4px 10px rgba(58,38,33,.22);letter-spacing:.06em}
.tag:after{content:"";position:absolute;inset:3px;border-radius:7px;border:1px solid rgba(235,207,195,.45);pointer-events:none}
.tag small{font-size:10.5px;color:var(--blush);margin-right:8px;vertical-align:4px;letter-spacing:.14em}
.say{position:absolute;background:var(--card);border:1.3px solid var(--ink);border-radius:18px;padding:9px 15px 10px;font-size:18px;line-height:1.45;z-index:4;white-space:nowrap;letter-spacing:.03em;box-shadow:0 3px 10px rgba(40,25,20,.12)}
.say:after{content:"";position:absolute;width:15px;height:15px;background:var(--card);border-right:1.3px solid var(--ink);border-bottom:1.3px solid var(--ink)}
.say.dn:after{bottom:-8.5px;transform:rotate(45deg)}
.say.up:after{top:-8.5px;transform:rotate(-135deg)}
.card{position:absolute;width:150px;z-index:3}
.card img{display:block;width:100%;filter:drop-shadow(0 6px 10px rgba(0,0,0,.32))}
.stk{position:absolute;width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;z-index:4;box-shadow:0 0 0 3px #fff,0 4px 10px rgba(0,0,0,.2)}
.nar{background:var(--mocha);color:#FBF6EF;border-radius:0 0 12px 12px;margin-top:-1px;padding:12px 16px 13px;font-size:15px;line-height:1.6;letter-spacing:.04em;white-space:nowrap}
.nar mark{background:none;color:var(--blush);padding:0}
/* s03 */
#s03 .ring{margin-top:16px}
#s03 .pn{margin-top:38px}
#s03 .pic{height:438px;border-radius:12px 12px 0 0}
/* s03b */
#s03b{padding:8px 22px 34px}
.xm{position:relative;overflow:hidden;background:#B5423A;border-radius:12px;box-shadow:0 8px 20px rgba(80,30,20,.2);padding:20px 12px 22px;text-align:center;color:#fff;outline:2px solid #E2BE6E;outline-offset:-9px}
.xm .sm{font-size:10px;letter-spacing:.32em;color:#F3D99B}
.xm .big{font-size:34px;letter-spacing:.14em;margin-top:5px;background:linear-gradient(180deg,#FFF6DA 10%,#F1CF7E 55%,#D9A94A 90%);-webkit-background-clip:text;color:transparent}
.xm .sh{position:absolute;top:-30%;bottom:-30%;width:90px;left:-40%;transform:skewX(-22deg);background:linear-gradient(90deg,transparent,rgba(255,236,180,.6),transparent);animation:sweep 2.5s linear infinite}
.xm .sp{position:absolute;width:14px;height:14px;margin:-7px;opacity:0;background:radial-gradient(circle,#FFF4C8 0 18%,transparent 20%),linear-gradient(0deg,transparent 45%,#FFE7A0 45% 55%,transparent 55%),linear-gradient(90deg,transparent 45%,#FFE7A0 45% 55%,transparent 55%);animation:tw 2.5s linear infinite}
@keyframes sweep{0%{left:-40%}55%{left:120%}100%{left:120%}}
@keyframes tw{0%,100%{opacity:0;transform:scale(.4)}12%{opacity:1;transform:scale(1.15) rotate(20deg)}26%{opacity:0;transform:scale(.4)}}
/* s04 */
#s04{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:8px 22px 40px}
#s04>div{background:var(--card);border-radius:14px;box-shadow:0 5px 14px rgba(58,38,33,.1),0 0 0 1px rgba(160,122,112,.14);text-align:center;padding:16px 4px 14px}
#s04>div:nth-child(2){background:var(--mocha);color:#FBF6EF}
#s04 .n{font-size:40px;line-height:1;color:var(--wine)}
#s04>div:nth-child(2) .n{color:var(--blush)}
#s04 .n small{font-size:20px;margin-left:2px}
#s04 .c{font-size:13.5px;margin-top:8px;line-height:1.45;color:var(--text)}
#s04>div:nth-child(2) .c{color:#EFE4DC}
/* s05 wall */
#s05 .pn{margin-top:26px;padding:0;background:var(--ink);height:500px;overflow:hidden}
.wall img{position:absolute;width:104px;filter:drop-shadow(0 3px 6px rgba(0,0,0,.45))}
#s05 .ring{position:absolute;right:-14px;top:-30px;margin:0;z-index:6}
/* how */
.how .hd{text-align:center}
.how .no{display:inline-block;background:var(--card);border:1.2px solid var(--wine);color:var(--wine);border-radius:20px;padding:5px 14px 5px 17px;font-size:11px}
.how h3{font-size:26px;line-height:1.42;margin-top:14px;letter-spacing:.05em}
.how p.d{font-size:14.5px;line-height:1.8;color:var(--text);margin-top:10px;letter-spacing:.04em}
.how .pn{margin-top:24px}
.how .ph{height:462px;background-size:cover;background-position:center;border-radius:12px 12px 0 0}
.how .bar{display:flex;align-items:center;gap:10px;background:var(--mocha);color:#fff;padding:11px 14px;border-radius:0 0 12px 12px}
.how .bar .st{color:var(--blush);font-size:11.5px}
.how .bar .cn{font-size:16px;flex:1;letter-spacing:.06em}
.how .bar .ee{font-size:10px;color:#CDB8AF}
.how .sfx{position:absolute;z-index:6}
/* s06 */
#s06 .pn{margin-top:24px;padding:0}
#s06 .cap{background:#F3E9E2;border-radius:18px 18px 0 0;border-bottom:1px solid var(--line);height:64px;padding-top:9px;font-size:16px;line-height:1.55;text-align:center;letter-spacing:.05em}
#s06 .cap small{display:block;font-size:10.5px;color:var(--wine);letter-spacing:.18em}
#s06 .pg{position:relative;height:250px}
#s06 .pim{position:absolute;left:24px;top:26px;width:340px;height:208px;background-size:contain;background-repeat:no-repeat;background-position:center;filter:drop-shadow(0 8px 14px rgba(40,25,20,.28))}
#s06 .lg{display:grid;grid-template-columns:1fr 1fr;gap:12px 10px;padding:6px 16px 18px}
#s06 .lg div{display:flex;gap:8px;align-items:flex-start}
#s06 .lg b{flex:none;width:20px;height:20px;border-radius:50%;background:var(--wine);color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-family:"Helvetica Neue",Arial,sans-serif;font-weight:500;margin-top:1px}
#s06 .lg span{font-size:15px;line-height:1.35;letter-spacing:.04em}
#s06 .lg small{display:block;font-size:12px;color:var(--text);margin-top:3px;letter-spacing:.03em}
/* s09 index */
#s09 .pn{margin-top:24px;padding:26px 16px 14px}
#s09 .tt{display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px double var(--ink);padding-bottom:9px}
#s09 .tt .a{font-size:21px;letter-spacing:.06em}#s09 .tt .b{font-size:10px;color:var(--wine)}
#s09 .row{display:grid;grid-template-columns:46px repeat(3,1fr);gap:0 6px;align-items:start;padding:12px 0 10px;border-bottom:1px dashed #D8CCBF}
#s09 .row:last-child{border-bottom:none}
#s09 .se{text-align:center;padding-top:14px}
#s09 .se b{display:block;font-size:19px;line-height:1.15;color:var(--wine);letter-spacing:.02em}
#s09 .se small{display:block;font-size:7.5px;margin-top:5px;color:var(--text);letter-spacing:.16em}
#s09 .fl{text-align:center}
#s09 .fl img{width:100%;display:block;filter:drop-shadow(0 3px 5px rgba(40,25,20,.25))}
#s09 .fl .nm{font-size:11.5px;margin-top:6px;letter-spacing:0;white-space:nowrap}
#s09 .fl .dt{font-size:8.5px;color:var(--rose);margin-top:3px;letter-spacing:.16em}
#s09 .ft{display:flex;align-items:center;height:78px;border-top:3px double var(--ink);font-size:15px;color:var(--text);letter-spacing:.05em;padding-left:4px}
#s09 .seal{position:absolute;right:-12px;bottom:-16px;width:108px;height:108px;z-index:5;transform:rotate(-10deg)}
#s09 .seal .ring{width:108px;height:108px}
/* s10 */
#s10 .pn{margin-top:24px}
#s10 .pic{height:260px}
#s10 .chips{display:grid;grid-template-columns:repeat(5,1fr);margin-top:8px;border-top:1px solid var(--line)}
#s10 .chips div{text-align:center;padding:11px 0 4px;font-size:13.5px;letter-spacing:.02em;border-left:1px dashed var(--line)}
#s10 .chips div:first-child{border-left:none}
#s10 .chips i{display:block;width:34px;height:18px;margin:0 auto 7px;border-radius:4px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.12),0 0 0 1px rgba(58,38,33,.2)}
/* s11 */
#s11 .pn{margin-top:24px}
#s11 .pic{height:300px}
#s11 table{width:100%;border-collapse:collapse;margin-top:4px}
#s11 td{padding:11px 8px;border-top:1px dashed #D8CCBF;font-size:14px;line-height:1.55;letter-spacing:.03em;vertical-align:top}
#s11 td:first-child{width:62px;color:var(--wine)}
#s11 tr:first-child td{border-top:none}
/* s12 */
#s12 .pic{height:457px}
#s12 .say{left:14px;top:16px;font-size:20px}
#s12 .end{position:absolute;right:14px;bottom:16px;z-index:4;background:var(--mocha);color:#FBF6EF;border-radius:10px;padding:7px 15px 9px;font-size:17px;transform:rotate(3deg);text-align:center;letter-spacing:.06em;box-shadow:0 4px 10px rgba(40,25,20,.22)}
#s12 .end .en{font-size:9.5px;letter-spacing:.22em;display:block;color:var(--blush);margin-bottom:2px}
'''

def s03():
    h = '''<section id="s03"><div class="eb">誰適合語錄卡？</div>
<h2>聖誕禮物 x 交換禮物<br><span class="u">讓一句話替你說出口</span></h2>''' + ring('抽一張<br>給自己')
    for x, l in zip(P, L):
        h += f'''<div class="pn" style="transform:rotate({l['rot']}deg)">
<div class="tag"><small class="en">NO.{x['n']}</small>{x['who']}</div>
<div class="pic" style="background-image:url(img/{x['img']}.jpg)">
<div class="say {'dn' if 'top' in l['say'] else 'up'}" style="{l['say']}" data-t="{l['tail']}">{x['h']}</div>
<div class="card" style="{l['card']}"><img src="img/cards/{x['card']:02d}.png"></div>
{sticker(*l['stk'])}</div>
<div class="nar">{x['s']}</div></div>'''
    return h + '</section>'

def s03b():
    sp = ''.join(f'<i class="sp" style="left:{x}%;top:{y}%;animation-delay:{d}s"></i>' for x, y, d in
                 [(8, 18, 0), (90, 22, .5), (93, 74, 1.0), (6, 78, 1.5), (50, 8, 2.0)])
    return f'<section id="s03b"><div class="xm"><div class="sh"></div>{sp}<div class="en sm">CHRISTMAS DELIVERY</div><div class="big">聖誕節前到貨</div></div></section>'

def s04():
    return '''<section id="s04"><div><div class="n">45</div><div class="c">張中英雙語<br>語錄卡</div></div>
<div><div class="n">45</div><div class="c">幅精選<br>攝影畫面</div></div>
<div><div class="n">5<small>色</small></div><div class="c">收藏盒<br>挑一個顏色</div></div></section>'''

def s05():
    random.seed(11)
    order = [n for n in range(1, 46)]; random.shuffle(order)  # 一盒 45 張：只用 1–45 號
    imgs = ''; k = 0
    for r in range(8):
        for c in range(4):
            x = c * 104 - 30 + (r % 2) * 46 + random.uniform(-6, 6)
            y = r * 64 - 22 + random.uniform(-5, 5)
            imgs += f'<img src="img/cards/{order[k]:02d}.png" style="left:{x:.0f}px;top:{y:.0f}px;transform:rotate({random.uniform(-9,9):.1f}deg)">'
            k += 1
    return f'''<section id="s05"><div class="eb">45 張，45 種心情</div>
<h2>在需要一句話的時候，<br><span class="u">抽一張給自己</span></h2>
<div class="lead">有寫給難過的你，也有寫給想往前走的你，<br>每一張都是今年重新挑選的。</div>
<div style="position:relative"><div class="pn"><div class="wall">{imgs}</div></div>{ring('45 張<br>不重複', 104, '#FBF3EC', 8, 17)}</div></section>'''

def how(n, sid, h, d, clip, cn, ee, sfx, sfx_pos):
    return f'''<section id="{sid}" class="how"><div class="hd"><span class="no en">HOW TO USE {n:02d}</span>
<h3>{h}</h3><p class="d">{d}</p></div>
<div class="pn"><div class="ph" data-clip="{clip}" style="background-image:url(gif/clips/{clip}/001.jpg)"></div>
<div class="sfx" style="{sfx_pos}">{sfx}</div>
<div class="bar"><span class="st en">STEP {n:02d}</span><span class="cn">{cn}</span><span class="ee en">{ee}</span></div></div></section>'''

def s06():
    caps = json.load(open(f'{D}/gif/caps_q_cards.json'))
    lg = [('1', '中文語錄', '一句話，說進心裡'), ('2', '英文對照', '同一句話，兩種語感'),
          ('3', '精選攝影', '每張都是一幅風景'), ('4', '柔和圓角', '拿在手上剛剛好')]
    lgh = ''.join(f'<div><b>{k}</b><span>{a}<small>{b}</small></span></div>' for k, a, b in lg)
    return f'''<section id="s06"><div class="eb">一張卡片有什麼？</div>
<h2>一句話，<br><span class="u">配一幅剛好的風景</span></h2>
<div class="pn"><div class="cap" data-caps="q_cards">{caps[0]}</div>
<div class="pg"><div class="pim" data-clip="q_cards" style="background-image:url(gif/clips/q_cards/001.png)"></div></div>
<div class="lg">{lgh}</div></div></section>'''

def s09():
    rows = [('看見', 'SEE', [(6, '而是慶祝你存在'), (30, '你被安穩的愛著呢'), (39, '你送出去的每顆糖')]),
            ('停下', 'PAUSE', [(8, '允許自己出錯'), (29, '我知道你最近很累'), (13, '焦慮不是惡魔')]),
            ('前行', 'MOVE', [(16, '船停在港口最安全'), (23, '別等一切完美'), (11, '自己寫的劇本')]),
            ('呼吸', 'BREATHE', [(37, '慢慢走吧'), (41, '好好睡一覺'), (22, '我願對自己溫柔')])]
    body = ''
    for se, en, cards in rows:
        body += f'<div class="row"><div class="se"><b>{se}</b><small class="en">{en}</small></div>'
        body += ''.join(f'<div class="fl"><img src="img/cards/{n:02d}.png"><div class="nm">{t}</div><div class="dt en">NO.{n:02d}</div></div>' for n, t in cards)
        body += '</div>'
    return f'''<section id="s09" style="padding-bottom:46px"><div class="eb">看見・停下・前行・呼吸</div>
<h2>今天的你，<br><span class="u">需要哪一句？</span></h2>
<div class="pn"><div class="tt"><span class="a">語錄卡 2027</span><span class="b en">DAILY QUOTE CARDS</span></div>
{body}<div class="ft">還有 33 張，等你慢慢抽</div><div class="seal">{ring('<span class="en" style="font-size:7.5px;letter-spacing:.2em;display:block;color:#7A2136;margin-bottom:3px">NEW 2027</span>全新<br>收錄', 108, '#FBF3EC', -8, 18)}</div></div></section>'''

def s10():
    chips = ''.join(f'<div><i style="background:{c}"></i>{n}</div>' for n, c in BOX)
    return f'''<section id="s10"><div class="eb">收藏盒顏色</div>
<h2>五種顏色，<br><span class="u">選一個收進你的日常</span></h2>
<div class="pn"><div class="pic" style="background-image:url(img/s10.jpg)"></div>
<div class="chips">{chips}</div></div></section>'''

def s11():
    rows = [('尺寸', '卡片 9 × 5.4 公分，柔和圓角'), ('內容', '45 張，每張一句中英雙語語錄，<br>配一幅精選攝影'),
            ('收藏盒', '五色可選，可以直接從盒中抽卡'), ('NFC', '手機感應收藏盒，打開專屬內容頁，<br>iPhone 與 Android 都能用'),
            ('重量', '158 g（含外盒 250 g，<br>外盒 8.1 × 12.6 × 6.1 公分）')]
    tr = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows)
    return f'''<section id="s11"><div class="eb">規格</div>
<h2>一盒 45 張，<br><span class="u">放在手邊剛剛好</span></h2>
<div class="pn"><div class="pic" style="background-image:url(img/s11.jpg)"></div><table>{tr}</table></div></section>'''

def s12():
    return '''<section id="s12" style="padding-bottom:48px"><div class="pn"><div class="pic" style="background-image:url(img/s12.jpg)">
<div class="say dn" data-t="left:34px">需要的時候，<br>它一直都在</div>
<div class="end"><span class="en">SEE YOU TOMORROW</span>明天，再抽一張</div></div></div></section>'''

def build():
    body = (s03() + s03b() + s04() + s05()
        + how(1, 's05a', '打開收藏盒，<br>隨手抽一張', '不用挑，抽到哪一句，<br>就是今天要對你說的話。', 'q_draw', '抽一張', 'DRAW', ring('抽！', 84, '#FBF3EC', -8, 21), 'right:-12px;top:-28px')
        + s06()
        + how(2, 's06a', '讀完了，<br>把它立在盒子上', '今天這一句，<br>一整天抬頭就看得到。', 'q_stand', '立在盒上', 'STAND', ring('今天<br>這一句', 84, '#FBF3EC', 6, 16), 'left:-12px;top:-28px')
        + how(3, 's07', '手機碰一下收藏盒，<br>打開專屬內容頁', '每張卡都有一段延伸解讀，<br>iPhone 與 Android 都能感應。', 'q_nfc', '碰一下', 'NFC', ring('嗶～', 84, '#FBF3EC', -6, 21), 'right:-12px;top:-28px')
        + how(4, 's08', '一張一張翻，<br>挑一句送給他', '抽到特別有感的那張，<br>就送給剛好需要它的人。', 'q_flip', '送一句', 'SHARE', ring('送你', 84, '#FBF3EC', 6, 20), 'left:-12px;top:-28px')
        + s09() + s10() + s11() + s12())
    js = '''<script>document.querySelectorAll('.say[data-t]').forEach((e,i)=>{const c='t'+i;e.classList.add(c);const s=document.createElement('style');s.textContent=`.${c}:after{${e.dataset.t}}`;document.head.appendChild(s)})</script>'''
    html = f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=432"><title>語錄卡落地頁 {V}</title><style>{CSS}</style></head><body>{body}{js}</body></html>'
    open(f'{D}/page.html', 'w').write(html)
    print('ok')

if __name__ == '__main__':
    build()
